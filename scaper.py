import json
import os
import subprocess

# 10 Chủ đề bạn muốn tập trung
TOPICS = ["Startup Tech", "AI Tools", "Coding Life", "Digital Marketing", "Fintech News", 
          "Productivity Hacks", "Blockchain", "Gadgets 2026", "UIUX Design", "E-commerce Tips"]

def get_tiktok_videos(query):
    print(f"Đang quét chủ đề: {query}...")
    # Lệnh gọi yt-dlp để lấy 100 video có lượt view cao nhất (giả lập qua search)
    cmd = [
        'yt-dlp',
        f"ytsearch100:tiktok {query}",
        '--get-id',
        '--match-filter', "duration < 60",
        '--flat-playlist'
    ]
    try:
        result = subprocess.check_output(cmd).decode('utf-8')
        video_ids = result.strip().split('\n')
        return [vid for vid in video_ids if len(vid) > 5] # Lọc ID hợp lệ
    except:
        return []

data = {}
for topic in TOPICS:
    ids = get_tiktok_videos(topic)
    if ids:
        data[topic] = ids

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Đã cập nhật data.json!")