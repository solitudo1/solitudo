# 个人主页 - solitudo1

这是一个基于 Flask 的现代化个人主页应用,已配置为使用 GitHub 用户 **solitudo1** 的信息。

## 🚀 快速开始

### 1. 启动应用

在项目目录下运行:

```bash
python app.py
```

然后访问: **http://127.0.0.1:5000**

### 2. 配置文件

个人信息已配置在 `config.json` 文件中:

- **GitHub**: https://github.com/solitudo1
- **深色模式**: 自动跟随系统
- **主题颜色**: 紫色渐变 (#6a11cb → #2575fc)

你可以根据需要修改 `config.json` 来自定义:
- 个人信息 (name, bio)
- 主题配色
- 联系方式
- 背景图片等

### 3. 自定义介绍

编辑 `Introduction.md` 文件来添加你的个人介绍内容。

## 📁 项目结构

```
Frontend/
├── app.py                 # Flask 主应用
├── config.json            # 配置文件(已配置 solitudo1)
├── Introduction.md        # 个人介绍文件
├── background.jpg         # 背景图片
├── templates/             # HTML 模板
├── default/               # 默认配置和资源
├── requirements.txt       # Python 依赖
└── build_static.py        # 静态文件构建脚本
```

## 🛠️ 功能特点

- ✨ 美观的现代化界面设计
- 📱 完全响应式,适配各种设备
- 🎨 支持深色/浅色模式自动切换
- 📊 自动展示 GitHub 个人信息和项目
- 📈 GitHub 活动数据可视化
- 🔄 最近项目自动更新

## 🌐 部署选项

### 本地运行(开发)
```bash
python app.py
```

### 生成静态文件
```bash
python build_static.py
```

生成的 `index.html` 可以直接部署到 GitHub Pages、Vercel、Netlify 等平台。

## 📝 注意事项

- 确保已安装所有依赖: `pip install -r requirements.txt`
- 如需获取私有仓库信息,可在 `config.json` 中添加 `github_token`
- 背景图片位于 `default/background.jpg`,已复制到根目录

## 🔗 相关链接

- GitHub: https://github.com/solitudo1
- 原始项目: https://github.com/SRInternet/Home_Page
