---
title: 如何添加新笔记
description: 这个 wiki 的使用方式
order: 1
---

在 `blog/src/content/wiki/notes/` 下新建一个 `.md` 或 `.mdx` 文件即可，frontmatter 只需要 `title`（必填）和 `description`（可选）：

```md
---
title: 笔记标题
description: 一句话描述
order: 1
---

正文内容...
```

和独立的 `wiki/` 项目（Starlight）不同，这个 wiki 页面是 `astro-theme-pure` 主题自带的 `docs` collection 模式照抄出来的一个 `wiki` collection，和博客共用同一套主题、同一个 Astro 项目、同一份 pagefind 搜索索引。

本地预览：

```bash
cd blog && bun dev
```
