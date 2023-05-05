# 项目名称：RansomwareDetect

## 项目简介
RansomwareDetect是基于诱饵文件的勒索软件检测程序，通过在勒索软件最先访问的文件夹中插入诱饵文件，当勒索软件对诱饵文件进行加密时，RansomwareDetect会检测到加密行为并进行报警。

项目整体UI借助了[PyOneDark Qt Widgets Modern GUI - With PySide6](https://github.com/Wanderson-Magalhaes/PyOneDark_Qt_Widgets_Modern_GUI.git)，
并且添加了适配PyOneDark的自定义Widget

部分UI使用了[PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets.git)

监控诱饵文件使用了[watchdog](https://github.com/gorakhargosh/watchdog.git)

读取诱饵文件使用了[python-magic](https://github.com/ahupp/python-magic.git)

## 安装说明
1. 确保已安装 Python 3.10，并配置好环境变量。
2. 下载或克隆该仓库到本地。
3. 打开命令行，进入项目目录。
4. 运行以下命令安装依赖项：
```pip install -r requirements.txt```
5. 运行以下命令启动应用程序：
```python main.py```

## 项目结构
```
│  .gitignore 使用git时忽略的文件
│  config.json 程序配置文件，包含陷阱文件和数据库链接
│  icon.ico 程序图标
│  LICENSE 许可证
│  main.py 程序入口
│  qt_core.py 简化Qt的导入
│  README.md 项目说明文档
│  requirements.txt 依赖项
│  settings.json 程序设置
├─app
│  └─slots 程序槽函数
│     │  database_page_slots.py 数据库页面槽函数
│     │  init_page_slots.py 诱饵文件配置页面槽函数
│     └─ monitor_page_slots.py 监控页面槽函数
├─gui 程序UI相关
│  ├─core 核心功能
│  │  │  functions.py 读取图片和图标
│  │  │  json_settings.py 读取程序的设置
│  │  └─ json_themes.py 读取并配置主题
│  ├─images 图片
│  │  ├─svg_icons 
│  │  └─svg_images
│  ├─themes 主题
│  │  ├─ bright.json 明亮主题
│  │  │  default.json 暗色主题
│  │  └─ dracula.json 德古拉主题
│  ├─uis
│  │  ├─columns 左边和右边的列
│  │  │  │  left_column.ui
│  │  │  │  right_column.ui
│  │  │  │  ui_left_column.py
│  │  │  └─ ui_right_column.py  
│  │  ├─pages 主页面
│  │  │  │  main_pages.ui
│  │  │  └─ ui_main_pages.py
│  │  └─windows 
│  │      └─main_window 主窗口
│  │          │  functions_main_window.py
│  │          │  setup_main_window.py 主要在这里添加组件
│  │          └─ ui_main.py         
│  └─widgets 自定义Widget
└─util 工具
   │  CPUThread.py CPU和内存监控线程
   │  file_function.py 计算文件熵值和文件头哈希
   │  fsutil.py 文件系统工具fsutil
   │  get_file_type.py 读取文件类型
   │  MonitorThread.py 监控线程
   │  PandasModel.py TableView中的pandas模型
   └─ __call_function__.py 调用MessageBox
```
> **Warning**: 下面是原PyOneDark项目的部分说明
![PyOneDark - Capa](https://user-images.githubusercontent.com/60605512/127739671-653eccb8-49da-4244-ae48-a8ae9b9b6fb2.png)

> ## :gift: **//// DONATE ////**
> ## 🔗 Donate (Gumroad): https://gum.co/mHsRC
> This interface is free for any use, but if you are going to use it commercially, consider helping to maintain this project and others with a donation by Gumroado at the link above. This helps to keep this and other projects active.

> **Warning**: this project was created using PySide6 and Python 3.9, using previous versions can cause compatibility problems.

