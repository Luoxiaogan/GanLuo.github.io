#!/usr/bin/env python3
"""
MapMyVisitors 数据爬虫脚本
从 https://mapmyvisitors.com/web/1bw90 爬取访问统计数据
"""

import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime
import urllib3

# 禁用 SSL 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def scrape_visitor_stats(url="https://mapmyvisitors.com/web/1bw90"):
    """
    爬取 MapMyVisitors 统计数据

    Args:
        url: MapMyVisitors 统计页面 URL

    Returns:
        dict: 包含统计数据的字典
    """
    print(f"正在爬取: {url}")

    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    try:
        # 发送请求（禁用 SSL 验证以避免证书问题）
        response = requests.get(url, headers=headers, timeout=10, verify=False)
        response.raise_for_status()

        # 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        stats = {
            'scrape_time': datetime.now().isoformat(),
            'url': url,
        }

        # 尝试提取统计数字（这些通常在页面的特定元素中）
        # 根据页面结构调整选择器

        # 方法1：查找包含数字的文本
        text_content = soup.get_text()

        # 提取总访问量
        pageviews_match = re.search(r'Total Pageviews[:\s]+(\d+[,\d]*)', text_content, re.IGNORECASE)
        if pageviews_match:
            stats['total_pageviews'] = pageviews_match.group(1).replace(',', '')

        # 提取总访问次数
        visits_match = re.search(r'Total Visits[:\s]+(\d+[,\d]*)', text_content, re.IGNORECASE)
        if visits_match:
            stats['total_visits'] = visits_match.group(1).replace(',', '')

        # 提取今日访问
        today_match = re.search(r"Today['\"]?s? Pageviews[:\s]+(\d+)", text_content, re.IGNORECASE)
        if today_match:
            stats['today_pageviews'] = today_match.group(1)

        # 方法2：查找可能包含 JSON 数据的 script 标签
        scripts = soup.find_all('script')
        for script in scripts:
            if script.string and 'pageviews' in script.string.lower():
                # 尝试提取 JSON 数据
                try:
                    # 查找类似 var data = {...} 的模式
                    json_match = re.search(r'var\s+\w+\s*=\s*(\{.*?\});', script.string, re.DOTALL)
                    if json_match:
                        data = json.loads(json_match.group(1))
                        stats['raw_data'] = data
                except:
                    pass

        # 方法3：提取表格数据（国家/地区统计）
        tables = soup.find_all('table')
        if tables:
            stats['countries'] = []
            for table in tables:
                rows = table.find_all('tr')
                for row in rows[1:]:  # 跳过表头
                    cols = row.find_all(['td', 'th'])
                    if len(cols) >= 2:
                        country_data = {
                            'country': cols[0].get_text(strip=True),
                            'visits': cols[1].get_text(strip=True) if len(cols) > 1 else None,
                        }
                        if len(cols) > 2:
                            country_data['unique'] = cols[2].get_text(strip=True)
                        stats['countries'].append(country_data)

        # 保存原始 HTML（可选，用于调试）
        # stats['raw_html'] = response.text[:1000]  # 只保存前1000字符

        return stats

    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None
    except Exception as e:
        print(f"解析失败: {e}")
        return None


def save_to_json(data, filename='visitor_stats.json'):
    """保存数据到 JSON 文件"""
    if data:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"数据已保存到: {filename}")
        return True
    return False


def print_stats(data):
    """打印统计数据"""
    if not data:
        print("没有数据可显示")
        return

    print("\n" + "="*50)
    print("MapMyVisitors 访问统计")
    print("="*50)

    print(f"\n爬取时间: {data.get('scrape_time', 'N/A')}")
    print(f"页面 URL: {data.get('url', 'N/A')}")

    if 'total_pageviews' in data:
        print(f"\n总访问量: {data['total_pageviews']}")
    if 'total_visits' in data:
        print(f"总访问次数: {data['total_visits']}")
    if 'today_pageviews' in data:
        print(f"今日访问: {data['today_pageviews']}")

    if 'countries' in data and data['countries']:
        print(f"\n国家/地区统计 (前10):")
        for i, country in enumerate(data['countries'][:10], 1):
            print(f"  {i}. {country.get('country', 'N/A')}: {country.get('visits', 'N/A')} 访问")

    print("="*50 + "\n")


if __name__ == '__main__':
    # 爬取数据
    stats = scrape_visitor_stats()

    # 打印统计
    print_stats(stats)

    # 保存到 JSON 文件
    if stats:
        save_to_json(stats, 'visitor_stats.json')
        print("\n提示: 如果某些数据未能提取，可能需要使用 Selenium 来处理动态加载的内容")
