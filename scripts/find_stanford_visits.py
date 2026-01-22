#!/usr/bin/env python3
"""
找出来自 Stanford / Palo Alto 的访问记录
使用 Unix timestamp 计算准确时间差
"""

import json
from datetime import datetime, timezone, timedelta
import re
import time

def find_stanford_visits(json_file='visitor_stats.json'):
    # 读取 JSON 数据
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 当前时间
    now = datetime.now()
    now_timestamp = time.time()

    # 定义时区
    tz_beijing = timezone(timedelta(hours=8))      # 北京时间 UTC+8
    tz_pacific = timezone(timedelta(hours=-8))     # 太平洋标准时间 PST UTC-8 (Stanford)

    print(f"当前北京时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    # 计算 Stanford 当前时间
    now_utc = datetime.now(timezone.utc)
    now_stanford = now_utc.astimezone(tz_pacific)
    print(f"当前 Stanford 时间: {now_stanford.strftime('%Y-%m-%d %H:%M:%S')} (PST)")
    print(f"当前 Unix 时间戳: {int(now_timestamp)}")
    print(f"数据爬取时间: {data.get('scrape_time', 'N/A')}")
    print("=" * 70)

    # 从 raw_data 获取所有时间戳
    raw_data = data.get('raw_data', {})
    all_timestamps = {}
    for key, value in raw_data.items():
        if isinstance(value, list) and len(value) > 0:
            entry = value[0]
            if 'timestamp' in entry and 'date' in entry:
                all_timestamps[entry['date']] = entry['timestamp']

    # 从 countries 数组中查找 Stanford 访问记录
    countries = data.get('countries', [])
    stanford_visits = []

    i = 0
    while i < len(countries):
        entry = countries[i]
        country_text = entry.get('country', '')

        # 检查是否包含 Stanford 或 Palo Alto
        if 'Stanford' in country_text or 'Palo Alto' in country_text:
            visitor_info = country_text
            browser = entry.get('visits', '')
            os_info = entry.get('unique', '')

            # 查找下一条记录获取时间
            visit_time_str = None
            visit_timestamp = None

            if i + 1 < len(countries):
                next_entry = countries[i + 1]
                time_text = next_entry.get('country', '')
                if 'TimeVisited on' in time_text:
                    time_match = re.search(r'TimeVisited on(.+)', time_text)
                    if time_match:
                        visit_time_str = time_match.group(1).strip()
                        # 从 raw_data 中查找对应的 timestamp
                        visit_timestamp = all_timestamps.get(visit_time_str)

            stanford_visits.append({
                'location': visitor_info,
                'browser': browser,
                'os': os_info,
                'time_str': visit_time_str,
                'timestamp': visit_timestamp
            })

        i += 1

    # 打印 Stanford/Palo Alto 访问记录
    print(f"\n找到 {len(stanford_visits)} 条 Stanford/Palo Alto 访问记录:\n")

    for idx, visit in enumerate(stanford_visits, 1):
        print(f"[{idx}] 原始时间: {visit['time_str']}")
        print(f"    浏览器: {visit['browser']}, 系统: {visit['os']}")

        if visit['timestamp']:
            # 使用 timestamp 计算
            hours_ago = (now_timestamp - visit['timestamp']) / 3600
            # 将 timestamp 转换为各时区时间
            utc_time = datetime.fromtimestamp(visit['timestamp'], tz=timezone.utc)
            beijing_time = utc_time.astimezone(tz_beijing)
            stanford_time = utc_time.astimezone(tz_pacific)
            print(f"    Unix 时间戳: {visit['timestamp']}")
            print(f"    北京时间: {beijing_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"    Stanford 时间: {stanford_time.strftime('%Y-%m-%d %H:%M:%S')} (PST)")
            print(f"    距离现在: {hours_ago:.2f} 小时前")
        else:
            print(f"    (未找到对应的 timestamp)")
        print()

    # 按时间从近到远排序（timestamp 大的在前）
    stanford_visits_sorted = sorted(
        [v for v in stanford_visits if v['timestamp']],
        key=lambda x: x['timestamp'],
        reverse=True
    )

    # 列出所有 Stanford/Palo Alto 访问
    print("=" * 70)
    print("所有 Stanford/Palo Alto 访问记录 (从近到远):")
    print("=" * 70)

    for idx, visit in enumerate(stanford_visits_sorted, 1):
        hours_ago = (now_timestamp - visit['timestamp']) / 3600
        utc_time = datetime.fromtimestamp(visit['timestamp'], tz=timezone.utc)
        beijing_time = utc_time.astimezone(tz_beijing)
        stanford_time = utc_time.astimezone(tz_pacific)
        # 提取位置信息
        location = "Stanford" if "Stanford" in visit['location'] else "Palo Alto"
        print(f"{idx:2}. [{location:9}] {stanford_time.strftime('%Y-%m-%d %H:%M')} | 北京: {beijing_time.strftime('%m-%d %H:%M')} | {hours_ago:.1f}h ago | {visit['browser']}/{visit['os']}")

    print(f"\n总计: {len(stanford_visits_sorted)} 次来自 Stanford/Palo Alto 的访问")


if __name__ == '__main__':
    find_stanford_visits()
