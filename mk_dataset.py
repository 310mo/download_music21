import json
import os
import subprocess

json_file = 'MUSIC21_solo_videos.json'
with open(json_file, 'r') as f:
    df = json.load(f)

video_dir = 'video'
audio_dir = 'audio'
os.makedirs(video_dir, exist_ok=True)
os.makedirs(audio_dir, exist_ok=True)

for inst in df['videos'].keys():
    os.makedirs(os.path.join(video_dir, inst), exist_ok=True)
    os.makedirs(os.path.join(audio_dir, inst), exist_ok=True)

    for youtubeid in df['videos'][inst]:
        video_path = os.path.join(video_dir, inst, youtubeid+'.mp4')
        audio_path = os.path.join(audio_dir, inst, youtubeid+'.wav')

        download_cmd =  'youtube-dl --sleep-interval 15 -f mp4'+' -o '+video_path+' https://www.youtube.com/watch?v='+youtubeid
        subprocess.call(download_cmd.split())

        if os.path.exists(video_path):
            audio_cmd = 'ffmpeg -i ' + video_path + ' ' + audio_path
            subprocess.call(audio_cmd.split())