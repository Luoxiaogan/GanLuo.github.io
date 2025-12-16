# MapMyVisitors 爬虫脚本使用指南

这个目录包含了两个版本的 MapMyVisitors 数据爬虫脚本。

## 脚本文件

1. **scrape_mapmyvisitors.py** - 基础版本（推荐日常使用）
   - 使用 `requests` + `BeautifulSoup`
   - 轻量、快速
   - 已测试可用

2. **scrape_mapmyvisitors_selenium.py** - 增强版本（需要时使用）
   - 使用 `Selenium` 处理动态内容
   - 更完整的数据提取
   - 会保存截图和完整 HTML

## 安装依赖

### 基础版本
```bash
pip install requests beautifulsoup4 urllib3
```

### Selenium 版本
```bash
pip install selenium webdriver-manager
```

## 使用方法

### 基础版本（推荐）
```bash
cd scripts
python3 scrape_mapmyvisitors.py
```

输出：
- 控制台打印统计数据
- 生成 `visitor_stats.json` 文件

### Selenium 版本
```bash
cd scripts
python3 scrape_mapmyvisitors_selenium.py
```

输出：
- 控制台打印统计数据
- 生成 `visitor_stats_selenium.json` 文件
- 生成 `mapmyvisitors_screenshot.png` 截图
- 生成 `mapmyvisitors_page.html` 完整页面

## 当前可提取的数据

基础版本已验证可以提取：
- ✅ 总访问量 (Total Pageviews)
- ✅ 今日访问 (Today's Pageviews)
- ⚠️ 国家/地区统计（部分可用，可能需要 Selenium 版本）

## 定时任务设置

### macOS/Linux - 使用 cron

编辑 crontab：
```bash
crontab -e
```

添加定时任务（每天早上 8 点执行）：
```bash
0 8 * * * cd /Users/luogan/Desktop/大四上/文件存放/个人主页/scripts && /usr/bin/python3 scrape_mapmyvisitors.py >> scrape.log 2>&1
```

### 手动执行脚本并保存日志
```bash
cd scripts
python3 scrape_mapmyvisitors.py >> scrape_log_$(date +\%Y\%m\%d).txt 2>&1
```

## 数据文件

生成的 JSON 文件格式示例：
```json
{
  "scrape_time": "2025-12-15T20:16:57.316758",
  "url": "https://mapmyvisitors.com/web/1bw90",
  "total_pageviews": "1782",
  "today_pageviews": "3"
}
```

## 故障排除

### SSL 错误
- 基础版本已配置 `verify=False` 禁用 SSL 验证
- 如果仍有问题，使用 Selenium 版本

### 数据提取不完整
- 页面可能使用 JavaScript 动态加载
- 切换到 Selenium 版本
- 检查生成的 HTML 文件分析页面结构

### Chrome/ChromeDriver 问题（Selenium）
- 首次运行会自动下载 ChromeDriver
- 确保系统已安装 Chrome 浏览器
- 如果自动下载失败，手动下载 ChromeDriver

## 统计页面

直接访问: [https://mapmyvisitors.com/web/1bw90](https://mapmyvisitors.com/web/1bw90)

## 注意事项

1. 爬虫仅用于个人统计数据获取
2. 请遵守网站的使用条款
3. 建议设置合理的爬取频率（如每天一次）
4. 数据仅供参考，以官网显示为准
