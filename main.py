from utils.channel import Channel
from utils.video import Video
from utils.plvideo import PLVideo
import os
from googleapiclient.discovery import build
from pprint import pprint

# lofi_girl = Channel('UCSJ4gkVC6NrvII8umztf0Ow')
# # lofi_girl.print_info()
# print(lofi_girl)

# vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

# получаем значения атрибутов
# print(vdud.title)
# # вДудь
# print(vdud.number_of_videos)
# # 163
# print(vdud.url_link)
# https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA

# менять не можем
# vdud.id = 'Новое название'
# AttributeError: property 'channel_id' of 'Channel' object has no setter

# # можем получить объект для работы с API вне класса
# print(Channel.get_service())
# # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>
#
#
# # создать файл 'vdud.json' в данными по каналу
# vdud.save_to_json_file('vdud.json')

# Homework 3
# print(vdud)
#
# print(vdud < lofi_girl)
# print(vdud > lofi_girl)
# print(lofi_girl + vdud)

id = '9lO06Zxhu88'
video1 = Video(id)
# print(video1)
pl_id = "PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD"

# api_key: str = os.getenv('YT_API_KEY')
# youtube = build('youtube', 'v3', developerKey=api_key)
# video = youtube.playlists().list(part='snippet', id=pl_id, ).execute()
# # video = youtube.playlistItems().list(part="snippet", playlistId=pl_id).execute()
# pprint(video)


# print(video1)

video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
# pprint(video2.pl_info)
print(video2)
# pprint(video2.video_info)
