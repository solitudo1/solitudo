# 🚀 快速开始指南

## ✅ 部署完成!

你的个人主页项目已成功部署到 `D:\solitudo\Frontend` 目录。

## 📌 当前配置

- **GitHub 用户**: solitudo1
- **GitHub 主页**: https://github.com/solitudo1
- **应用状态**: ✅ 正在运行
- **访问地址**: http://127.0.0.1:5000

## 🎯 如何使用

### 方法 1: 双击启动 (推荐)
直接双击以下任一文件:
- `start.bat` (Windows 批处理)
- `start.ps1` (PowerShell)

### 方法 2: 命令行启动
```bash
cd D:\solitudo\Frontend
python app.py
```

然后在浏览器中打开: **http://127.0.0.1:5000**

## 🎨 自定义你的主页

### 1. 修改个人信息
编辑 `config.json` 文件:
```json
{
  "name": "你的名字",
  "bio": "你的简介",
  "github_url": "https://github.com/solitudo1"
}
```

### 2. 添加个人介绍
编辑 `Introduction.md` 文件,用 Markdown 格式编写你的个人介绍。

### 3. 修改主题颜色
在 `config.json` 中调整:
```json
"theme": {
  "primary_color": "#6a11cb",      // 主色调
  "secondary_color": "#2575fc"     // 辅助色
}
```

### 4. 更换背景图片
将新的背景图片放在根目录,并在 `config.json` 中修改:
```json
"background": {
  "image": "your-background.jpg"
}
```

### 5. 添加联系方式
在 `config.json` 的 `contact` 部分添加你的社交账号链接。

## 📦 部署到互联网

### 选项 1: 生成静态文件 (最简单)
```bash
python build_static.py
```
生成的 `index.html` 可以直接上传到:
- GitHub Pages
- Vercel
- Netlify
- 任何静态网站托管服务

### 选项 2: 使用 Flask 平台部署
- PythonAnywhere
- Heroku
- Railway
- DigitalOcean App Platform

## 🔧 常见问题

### Q: 如何停止服务器?
A: 在运行服务器的终端窗口按 `Ctrl+C`

### Q: 端口被占用怎么办?
A: 修改 `app.py` 文件最后一行,更改端口号:
```python
app.run(host='0.0.0.0', port=5000, debug=True)  # 改为其他端口
```

### Q: 如何获取私有仓库信息?
A: 在 `config.json` 中添加 GitHub Token:
```json
"github_token": "your_github_token_here"
```

### Q: 深色/浅色模式如何切换?
A: 在 `config.json` 中设置 `dark_mode`:
- `"auto"` - 跟随系统
- `"dark"` - 强制深色
- `"light"` - 强制浅色

## 📁 重要文件说明

- `config.json` - 主配置文件 ⭐
- `Introduction.md` - 个人介绍内容
- `app.py` - Flask 应用主文件
- `background.jpg` - 背景图片
- `templates/index.html` - 网页模板
- `build_static.py` - 静态文件生成脚本

## 🎉 开始使用吧!

现在你可以在浏览器中访问 **http://127.0.0.1:5000** 查看你的个人主页!

如有任何问题,请参考 `DEPLOYMENT_GUIDE.md` 或原始项目的 `README.md`。
