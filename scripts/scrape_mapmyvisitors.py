#!/usr/bin/env python3
"""
MapMyVisitors 数据爬虫脚本（增量更新版）
从 https://mapmyvisitors.com/web/1bw90 爬取访问统计数据
每次运行会合并新旧数据，保留所有历史记录
"""

import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime
import urllib3
import os

# 禁用 SSL 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 数据文件路径
DATA_FILE = 'visitor_stats.json'


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


def load_existing_data(filename=DATA_FILE):
    """加载已有的数据"""
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return None
    return None


def merge_data(old_data, new_data):
    """
    合并新旧数据，实现增量更新
    - raw_data: 按 timestamp 去重合并
    - countries: 使用新数据（最近的访问记录）
    - 统计数字: 使用新数据
    """
    if not old_data:
        return new_data

    if not new_data:
        return old_data

    merged = {
        'scrape_time': new_data.get('scrape_time'),
        'url': new_data.get('url'),
        'total_pageviews': new_data.get('total_pageviews'),
        'today_pageviews': new_data.get('today_pageviews'),
    }

    # 合并 raw_data（按 timestamp 去重）
    old_raw = old_data.get('raw_data', {})
    new_raw = new_data.get('raw_data', {})

    # 使用 timestamp 作为唯一标识
    all_records = {}

    # 先加入旧数据
    for key, value in old_raw.items():
        if isinstance(value, list) and len(value) > 0:
            ts = value[0].get('timestamp')
            if ts:
                all_records[ts] = {key: value}

    # 再加入新数据（会覆盖相同 timestamp 的记录）
    for key, value in new_raw.items():
        if isinstance(value, list) and len(value) > 0:
            ts = value[0].get('timestamp')
            if ts:
                all_records[ts] = {key: value}

    # 合并回 raw_data 格式
    merged_raw = {}
    for ts, record in all_records.items():
        merged_raw.update(record)

    merged['raw_data'] = merged_raw

    # countries 使用新数据（包含最近的访问者详情）
    # 但我们也保留一份历史记录
    merged['countries'] = new_data.get('countries', [])

    # 保存历史 countries 记录（去重）
    old_countries_history = old_data.get('countries_history', [])
    new_countries = new_data.get('countries', [])

    # 提取新的访问记录（只保留有位置信息的）
    for entry in new_countries:
        country_text = entry.get('country', '')
        if 'NewVisitor from' in country_text and entry not in old_countries_history:
            old_countries_history.append(entry)

    merged['countries_history'] = old_countries_history

    return merged


def save_to_json(data, filename=DATA_FILE):
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
    print("=" * 60)
    print("MapMyVisitors 增量爬虫")
    print("=" * 60)

    # 加载已有数据
    old_data = load_existing_data()
    if old_data:
        old_count = len(old_data.get('raw_data', {}))
        print(f"已加载历史数据: {old_count} 条记录")
    else:
        old_count = 0
        print("未找到历史数据，将创建新文件")

    # 爬取新数据
    new_stats = scrape_visitor_stats()

    if new_stats:
        new_count = len(new_stats.get('raw_data', {}))
        print(f"本次爬取: {new_count} 条记录")

        # 合并数据
        merged_stats = merge_data(old_data, new_stats)
        merged_count = len(merged_stats.get('raw_data', {}))

        # 打印统计
        print_stats(merged_stats)

        # 保存合并后的数据
        save_to_json(merged_stats)

        # 显示增量信息
        added_count = merged_count - old_count
        print(f"\n{'=' * 60}")
        print(f"增量更新完成!")
        print(f"  历史记录: {old_count} 条")
        print(f"  新增记录: {added_count} 条")
        print(f"  总计记录: {merged_count} 条")
        print(f"{'=' * 60}")
    else:
        print("爬取失败，保留原有数据")
