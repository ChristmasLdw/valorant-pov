#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
获取无畏契约所有英雄的ID和名称对应关系
"""

import json
import subprocess
import time

def get_hero_name(hero_id):
    """获取指定ID的英雄名称"""
    # 使用curl获取页面内容
    url = f"https://val.qq.com/game-data.html?pageType=1&&heroId={hero_id}"
    cmd = f'curl -s "{url}" | iconv -f GBK -t UTF-8 | grep -oP "(?<=<h4[^>]*>)[^<]+"'
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        if result.stdout:
            return result.stdout.strip()
    except Exception as e:
        print(f"Error getting hero {hero_id}: {e}")
    return None

def main():
    heroes = []
    
    print("正在获取英雄列表...")
    for i in range(1, 30):
        name = get_hero_name(i)
        if name:
            heroes.append({"id": i, "name": name})
            print(f"  {i:2d}. {name}")
        else:
            print(f"  {i:2d}. (未获取到)")
        time.sleep(0.2)  # 避免请求过快
    
    print(f"\n获取到 {len(heroes)} 个英雄")
    
    # 保存到文件
    with open("/Users/christmasldw/WorkBuddy/2026-05-16-task-1/hero_mapping.json", "w", encoding="utf-8") as f:
        json.dump(heroes, f, ensure_ascii=False, indent=2)
    
    print("映射已保存到 hero_mapping.json")
    
    return heroes

if __name__ == "__main__":
    main()
