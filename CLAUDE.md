# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是罗淦（Gan Luo）的个人学术主页，基于 AcadHomepage 模板构建，使用 Jekyll 静态网站生成器。该网站托管在 GitHub Pages 上，主要展示学术研究成果、论文发表、教育背景等信息。

## 核心架构

这个仓库里实际上是两个完全独立的子站点，分别构建后拼接部署到同一个 GitHub Pages 域名下：

| 子站点 | 目录 | 技术栈 | 线上路径 |
|---|---|---|---|
| 主页 | 仓库根目录 | Jekyll (Ruby) + AcadHomepage 主题 | `/GanLuo.github.io/` |
| 博客（含 wiki） | `blog/` | Astro + astro-theme-pure 主题 | `/GanLuo.github.io/blog/` |

两者源码、依赖、主题完全不共享，`.github/workflows/jekyll.yml` 会分别构建后把 `blog/dist` 拷进 Jekyll 的 `_site/blog`，整体一起部署。本地可以用根目录的 `./build_all.sh`（只构建）或 `./serve_all.sh`（构建 + 起本地服务器并自动打开浏览器，路径和线上一致）一键跑两者。

### Jekyll 网站结构（主页部分）
- **_pages/about.md**: 主页核心内容文件，包含个人简介、研究成果、教育背景等所有主要信息
- **_config.yml**: 网站全局配置文件，包含作者信息、Google Scholar ID、网站元数据等
- **_layouts/**: 页面布局模板
- **_includes/**: 可复用的页面组件
- **_sass/**: SCSS 样式文件
- **assets/**: 静态资源（CSS、JS、图片等）

### Wiki（`blog/src/content/wiki/`、`blog/src/pages/wiki/`）
个人笔记/知识库，不是独立项目，而是照抄 `astro-theme-pure` 主题自带的 `docs` collection 模式在 `blog/` 里加的一个 `wiki` collection——和博客共用同一套主题、同一个 Astro 项目、同一份 pagefind 搜索索引。（之前评估过做成独立的 Astro + Starlight 项目，样式上手动对齐过 blog，但最终选了这个方案，Starlight 那套已经删掉了。）
- 内容目录：`blog/src/content/wiki/notes/`，每个 `.md`/`.mdx` 文件一篇笔记，frontmatter 只需要 `title`（必填）、`description`（可选）、`order`（排序，数字越小越靠前）
- 路由页面：`blog/src/pages/wiki/`（`index.astro` 落地页、`[...id].astro` 详情页、`WikiContents.astro` 侧边栏目录组件），结构照抄自 `blog/src/pages/docs/`
- **侧边栏分类不是自动生成的**：新增笔记如果用了新的顶层目录（现在只有 `notes`），要去 `WikiContents.astro` 里的 `wikiCategories` 对象手动加一行映射，否则不会出现在侧边栏分类里
- 线上路径：`/GanLuo.github.io/blog/wiki/`；blog 顶部导航栏（`site.config.ts` 的 `header.menu`）有 "Wiki" 入口
- 本地开发：`cd blog && bun dev`，构建：`cd blog && bun run build`（和博客是同一个命令，wiki 页面随博客一起构建）

### 学术内容管理
- **CV_GanLuo/**: LaTeX 格式的学术简历源文件
  - `cv.tex`: 主文件
  - `cv.pdf`: 编译后的PDF文件
  - 各个 `.tex` 文件: 简历的不同章节（教育、经历、发表、教学、奖项等）
- **images/**: 网站图标和个人照片

### Google Scholar 集成
网站通过 GitHub Actions 自动爬取并更新 Google Scholar 引用数据：
- 数据存储在 `google-scholar-stats` 分支的 `gs_data_shieldsio.json`
- 通过 Liquid 模板语言在页面中动态显示引用数
- 使用 `<span class='show_paper_citations' data='PAPER_ID'>` 显示单篇论文引用

## 开发命令

### 本地开发
```bash
# 安装依赖
bundle install

# 启动本地开发服务器（带实时重载）
bash run_server.sh
# 或直接使用
bundle exec jekyll liveserve

# 标准Jekyll命令构建
bundle exec jekyll serve

# 构建静态网站
bundle exec jekyll build
```

### 一键构建/预览全部子站点
```bash
# 只构建，产物合并到 _site/
./build_all.sh

# 构建 + 本地起服务器预览（路径与线上一致），默认 8000 端口
./serve_all.sh
```

### LaTeX 简历编译
```bash
cd CV_GanLuo
pdflatex cv.tex
# 或使用 latexmk 自动编译
latexmk -pdf cv.tex
```

## 内容更新工作流

### 更新个人主页内容
1. 编辑 `_pages/about.md` 文件
2. 使用 Markdown 和 HTML 混合语法
3. 论文引用显示格式：`<span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span>`
4. 支持 Liquid 模板语法用于动态内容

### 更新学术简历
1. 修改 `CV_GanLuo/` 目录下相应的 `.tex` 文件
2. 重新编译生成 PDF：`pdflatex cv.tex`
3. 确保 `cv.pdf` 更新后提交到仓库

### 配置 Google Scholar 自动更新
1. 在 `_config.yml` 中设置正确的 `repository` 名称
2. 在 GitHub 仓库的 Secrets 中添加 `GOOGLE_SCHOLAR_ID`
3. GitHub Actions 会每天 08:00 UTC 自动更新引用数据
4. 手动触发：推送到 main 分支

## 关键配置说明

### _config.yml 重要字段
- `title`: 网页标题（当前："Gan Luo (罗淦)"）
- `author.email`: 联系邮箱
- `author.googlescholar`: Google Scholar 主页链接
- `google_scholar_stats_use_cdn`: 是否使用 CDN（建议国内用户设为 true）
- `repository`: GitHub 仓库名（用于 Google Scholar 数据获取）

### 发布流程
1. 推送代码到 GitHub main 分支
2. GitHub Actions 自动构建并部署到 GitHub Pages
3. 网站自动更新到 https://luoxiaogan.github.io/luogan.github.io/

## 项目特色功能

### 自动化功能
- **Google Scholar 引用自动更新**: 通过 GitHub Actions 定时爬取
- **Jekyll 自动构建部署**: 推送即部署，无需手动构建
- **响应式设计**: 自动适配不同屏幕尺寸

### 学术展示特性
- **论文列表**: 支持显示论文标题、作者、会议/期刊、链接
- **实时引用数**: 集成 Google Scholar API 显示引用统计
- **CV 下载**: 提供 PDF 格式简历下载
- **访问统计**: 集成 MapMyVisitors 显示访问者地理分布

## 常见维护场景

### 添加新论文
在 `_pages/about.md` 的相应章节添加：
```markdown
- **论文标题**\\
作者列表\\
**_会议/期刊名称_**\\
[[Arxiv](链接)], [[Code](链接)]
```

### 更新个人信息
修改 `_config.yml` 中的 `author` 部分和 `_pages/about.md` 中的个人简介

### 调试引用数显示
1. 检查 GitHub Actions 运行状态
2. 确认 `google-scholar-stats` 分支是否有最新数据
3. 验证论文 ID 是否正确（从 Google Scholar 页面获取）