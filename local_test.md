# Jekyll 本地构建指南

## 快速启动

在项目目录下执行：

```bash
bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

然后在浏览器访问：http://127.0.0.1:4000

按 `Ctrl+C` 停止服务器。

---

## 环境配置（首次使用）

### 1. 安装 Ruby 环境管理工具

```bash
brew install rbenv ruby-build
```

### 2. 初始化 rbenv

```bash
rbenv init
```

重启终端或执行：

```bash
source ~/.zprofile
```

### 3. 安装 Ruby

```bash
rbenv install 3.1.2
rbenv local 3.1.2
```

验证版本：

```bash
ruby -v  # 应显示 ruby 3.1.2
```

### 4. 安装依赖

```bash
gem install bundler:2.2.19
bundle install
bundle add webrick  # Ruby 3.0+ 需要
```

---

## 常用命令

### 启动服务器（后台运行）

```bash
bundle exec jekyll serve --host 127.0.0.1 --port 4000 &
```

### 启动服务器（自动刷新）

```bash
bundle exec jekyll serve --host 127.0.0.1 --port 4000 --livereload
```

### 仅构建网站（不启动服务器）

```bash
bundle exec jekyll build
```

### 清理生成的文件

```bash
bundle exec jekyll clean
```

---

## 故障排除

### 问题：找不到 bundler 版本

```bash
gem install bundler:2.2.19
```

### 问题：缺少 webrick

```bash
bundle add webrick
```

### 问题：Ruby 版本不对

```bash
eval "$(rbenv init - zsh)"
ruby -v  # 检查版本
```

### 问题：端口被占用

更换端口：

```bash
bundle exec jekyll serve --host 127.0.0.1 --port 4001
```

---

## 配置代理（可选）

如果网络需要代理：

```bash
export https_proxy=http://127.0.0.1:7890
export http_proxy=http://127.0.0.1:7890
export all_proxy=socks5://127.0.0.1:7890
```

---

## 注意事项

- 修改 `_config.yml` 后需要重启服务器
- 修改其他文件（如文章、页面）会自动刷新
- 生成的网站在 `_site` 目录下
- 本地地址：http://127.0.0.1:4000