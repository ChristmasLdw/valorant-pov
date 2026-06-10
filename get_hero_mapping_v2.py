#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用浏览器获取无畏契约所有英雄的ID和名称对应关系
"""

import json
import subprocess
import time

def get_heroes_via_browser():
    """通过浏览器获取英雄列表"""
    heroes = []
    
    print("正在通过浏览器获取英雄列表...")
    
    for i in range(1, 30):
        # 打开指定heroId的页面
        url = f"https://val.qq.com/game-data.html?pageType=1&&heroId={i}"
        cmd = f'''
            export PATH="/Users/christmasldw/.workbuddy/binaries/node/versions/22.12.0/bin:$PATH" && unset NODE_OPTIONS
            agent-browser open "{url}"
            sleep 2
            agent-browser eval "document.querySelector('h4')?.textContent || ''"
        '''
        
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
            name = result.stdout.strip()
            if name:
                heroes.append({"id": i, "name": name})
                print(f"  {i:2d}. {name}")
            else:
                print(f"  {i:2d}. (未获取到)")
        except Exception as e:
            print(f"  {i:2d}. Error: {e}")
        
        time.sleep(0.5)
    
    return heroes

def main():
    heroes = get_heroes_via_browser()
    
    print(f"\n获取到 {len(heroes)} 个英雄")
    
    # 保存到文件
    with open("/Users/christmasldw/WorkBuddy/2026-05-16-task-1/hero_mapping.json", "w", encoding="utf-8") as f:
        json.dump(heroes, f, ensure_ascii=False, indent=2)
    
    print("映射已保存到 hero_mapping.json")
    
    return heroes

if __name__ == "__main__":
    main()
