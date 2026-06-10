# Valorant POV - Valorant游戏POV数据工具

## 项目简介
Valorant 游戏 POV（Point of View）数据处理和展示工具。

## 功能
- POV 数据抓取
- 英雄映射管理
- 图片资源下载
- 数据可视化展示

## 技术栈
- Python 脚本（数据处理）
- 静态页面展示
- JSON 数据存储

## 文件说明
- `index.html` - 前端展示页面
- `get_hero_mapping*.py` - 英雄映射脚本
- `download_val_images.py` - 图片下载脚本
- `*.json` - 数据文件
- `val_images/` - 英雄图片资源
- `xlsx_extract/` - Excel 数据提取

## 本地运行
```bash
# 运行数据处理脚本
python3 get_hero_mapping_v2.py

# 静态页面直接打开
open index.html
```

## 部署
静态文件直接复制到服务器 `/var/www/valorant-pov/`

## 修改指南
- 添加新英雄时运行映射脚本
- 更新数据后重新生成 JSON
- 图片资源放在 `val_images/` 目录

## 注意事项
- Python 脚本需要相关依赖（requests, pandas 等）
- 图片下载需要网络连接
