#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
下载 val.qq.com 网站的所有英雄和地图图片
"""

import os
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# 图片保存目录
BASE_DIR = "/Users/christmasldw/WorkBuddy/2026-05-16-task-1/val_images"

# 英雄大图 URL 模式
HERO_BIGPIC_URLS = [
    f"https://game.gtimg.cn/images/val/agamezlk/bigpic/{i:02d}.png"
    for i in range(1, 30)
]

# 英雄肖像 URL 模式
HERO_PORTRAIT_URLS = [
    f"https://game.gtimg.cn/images/val/agamezlk/portrait/{i:02d}.png"
    for i in range(1, 30)
]

# 地图封面
MAP_NAMES = [
    "corrode", "bind", "haven", "split", "ascent", 
    "icebox", "breeze", "fracture", "pearl", "lotus", 
    "sunset", "abyss"
]

MAP_COVER_URLS = [
    f"https://game.gtimg.cn/images/val/agamezlk/map/{map_name}/cover.PNG"
    for map_name in MAP_NAMES
]

def download_image(url, save_path):
    """
    下载单个图片
    """
    try:
        # 创建目录
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # 下载图片
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=30) as response:
            with open(save_path, 'wb') as f:
                f.write(response.read())
        
        print(f"✓ 下载成功: {os.path.basename(save_path)}")
        return True, save_path
    
    except urllib.error.HTTPError as e:
        print(f"✗ HTTP错误 {e.code}: {url}")
        return False, url
    except Exception as e:
        print(f"✗ 下载失败: {url} - {str(e)}")
        return False, url

def download_all_images():
    """
    下载所有图片
    """
    print("=" * 60)
    print("开始下载 val.qq.com 图片")
    print("=" * 60)
    
    # 下载英雄大图
    print("\n[1/3] 下载英雄大图...")
    hero_bigpic_dir = os.path.join(BASE_DIR, "heroes", "bigpic")
    os.makedirs(hero_bigpic_dir, exist_ok=True)
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for url in HERO_BIGPIC_URLS:
            filename = os.path.basename(url)
            save_path = os.path.join(hero_bigpic_dir, filename)
            future = executor.submit(download_image, url, save_path)
            futures.append(future)
        
        success_count = 0
        for future in as_completed(futures):
            success, _ = future.result()
            if success:
                success_count += 1
    
    print(f"英雄大图下载完成: {success_count}/{len(HERO_BIGPIC_URLS)}")
    
    # 下载英雄肖像
    print("\n[2/3] 下载英雄肖像...")
    hero_portrait_dir = os.path.join(BASE_DIR, "heroes", "portrait")
    os.makedirs(hero_portrait_dir, exist_ok=True)
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for url in HERO_PORTRAIT_URLS:
            filename = os.path.basename(url)
            save_path = os.path.join(hero_portrait_dir, filename)
            future = executor.submit(download_image, url, save_path)
            futures.append(future)
        
        success_count = 0
        for future in as_completed(futures):
            success, _ = future.result()
            if success:
                success_count += 1
    
    print(f"英雄肖像下载完成: {success_count}/{len(HERO_PORTRAIT_URLS)}")
    
    # 下载地图封面
    print("\n[3/3] 下载地图封面...")
    maps_dir = os.path.join(BASE_DIR, "maps")
    os.makedirs(maps_dir, exist_ok=True)
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for url in MAP_COVER_URLS:
            # 从URL中提取地图名称
            map_name = url.split("/")[-2]
            filename = f"{map_name}_cover.PNG"
            save_path = os.path.join(maps_dir, filename)
            future = executor.submit(download_image, url, save_path)
            futures.append(future)
        
        success_count = 0
        for future in as_completed(futures):
            success, _ = future.result()
            if success:
                success_count += 1
    
    print(f"地图封面下载完成: {success_count}/{len(MAP_COVER_URLS)}")
    
    print("\n" + "=" * 60)
    print("所有图片下载完成！")
    print(f"保存位置: {BASE_DIR}")
    print("=" * 60)

if __name__ == "__main__":
    start_time = time.time()
    download_all_images()
    elapsed_time = time.time() - start_time
    print(f"\n总耗时: {elapsed_time:.2f} 秒")
