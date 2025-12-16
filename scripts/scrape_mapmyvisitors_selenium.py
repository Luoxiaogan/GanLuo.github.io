#!/usr/bin/env python3
"""
MapMyVisitors 数据爬虫脚本 (Selenium 版本)
使用 Selenium 处理动态加载内容
从 https://mapmyvisitors.com/web/1bw90 爬取访问统计数据

依赖安装:
pip install selenium webdriver-manager
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json
import time
from datetime import datetime


def scrape_visitor_stats_selenium(url="https://mapmyvisitors.com/web/1bw90"):
    """
    使用 Selenium 爬取 MapMyVisitors 统计数据

    Args:
        url: MapMyVisitors 统计页面 URL

    Returns:
        dict: 包含统计数据的字典
    """
    print(f"正在启动浏览器并爬取: {url}")

    # 配置 Chrome 选项
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 无头模式
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36')

    driver = None
    try:
        # 初始化 WebDriver
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

        # 访问页面
        driver.get(url)

        # 等待页面加载
        print("等待页面加载...")
        time.sleep(5)  # 给足够时间让 JavaScript 执行

        # 收集数据
        stats = {
            'scrape_time': datetime.now().isoformat(),
            'url': url,
        }

        # 提取统计数字
        try:
            # 方法1：通过页面文本提取
            page_text = driver.find_element(By.TAG_NAME, 'body').text

            # 提取关键数字
            import re
            pageviews_match = re.search(r'Total Pageviews[:\s]+(\d+[,\d]*)', page_text, re.IGNORECASE)
            if pageviews_match:
                stats['total_pageviews'] = int(pageviews_match.group(1).replace(',', ''))

            visits_match = re.search(r'Total Visits[:\s]+(\d+[,\d]*)', page_text, re.IGNORECASE)
            if visits_match:
                stats['total_visits'] = int(visits_match.group(1).replace(',', ''))

            today_match = re.search(r"Today['\"]?s? Pageviews[:\s]+(\d+)", page_text, re.IGNORECASE)
            if today_match:
                stats['today_pageviews'] = int(today_match.group(1))

            print(f"\n找到数据:")
            print(f"  总访问量: {stats.get('total_pageviews', 'N/A')}")
            print(f"  总访问次数: {stats.get('total_visits', 'N/A')}")
            print(f"  今日访问: {stats.get('today_pageviews', 'N/A')}")

        except Exception as e:
            print(f"提取统计数字失败: {e}")

        # 提取国家/地区数据
        try:
            # 尝试多种可能的选择器
            country_elements = driver.find_elements(By.CSS_SELECTOR, 'table tr, .country-row, [class*="country"]')

            if country_elements:
                stats['countries'] = []
                print(f"\n找到 {len(country_elements)} 个国家/地区元素")

                for elem in country_elements[:20]:  # 限制前20个
                    text = elem.text.strip()
                    if text and len(text) > 0:
                        # 简单解析（根据实际页面结构调整）
                        parts = text.split()
                        if len(parts) >= 2:
                            stats['countries'].append({
                                'raw_text': text,
                                'data': parts
                            })

        except Exception as e:
            print(f"提取国家数据失败: {e}")

        # 截图保存（可选）
        try:
            screenshot_path = 'mapmyvisitors_screenshot.png'
            driver.save_screenshot(screenshot_path)
            print(f"\n页面截图已保存: {screenshot_path}")
        except Exception as e:
            print(f"保存截图失败: {e}")

        # 保存完整 HTML
        try:
            with open('mapmyvisitors_page.html', 'w', encoding='utf-8') as f:
                f.write(driver.page_source)
            print("页面 HTML 已保存: mapmyvisitors_page.html")
        except Exception as e:
            print(f"保存 HTML 失败: {e}")

        return stats

    except Exception as e:
        print(f"爬取失败: {e}")
        import traceback
        traceback.print_exc()
        return None

    finally:
        if driver:
            driver.quit()
            print("\n浏览器已关闭")


def save_to_json(data, filename='visitor_stats_selenium.json'):
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

    print("\n" + "="*60)
    print("MapMyVisitors 访问统计 (Selenium)")
    print("="*60)

    print(f"\n爬取时间: {data.get('scrape_time', 'N/A')}")

    if 'total_pageviews' in data:
        print(f"\n📊 总访问量: {data['total_pageviews']:,}")
    if 'total_visits' in data:
        print(f"👥 总访问次数: {data['total_visits']:,}")
    if 'today_pageviews' in data:
        print(f"📅 今日访问: {data['today_pageviews']}")

    if 'countries' in data and data['countries']:
        print(f"\n🌍 国家/地区统计:")
        for i, country in enumerate(data['countries'][:10], 1):
            print(f"  {i}. {country.get('raw_text', 'N/A')}")

    print("\n" + "="*60)


if __name__ == '__main__':
    print("MapMyVisitors Selenium 爬虫")
    print("="*60)
    print("注意: 首次运行会自动下载 ChromeDriver")
    print("="*60 + "\n")

    # 爬取数据
    stats = scrape_visitor_stats_selenium()

    # 打印统计
    print_stats(stats)

    # 保存到 JSON 文件
    if stats:
        save_to_json(stats)
        print("\n✅ 完成！数据已保存，还生成了截图和 HTML 文件用于调试")
    else:
        print("\n❌ 爬取失败")

    print("\n提示: 可以查看生成的 mapmyvisitors_page.html 文件来分析页面结构")
