import os

from googleapiclient.discovery import build
from pprint import pprint


class Channel:
    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('YT_API_KEY')
    # создать специальный объект для работы с API
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str):
        self.id = channel_id

    def print_info(self):
        channel = Channel.youtube.channels().list(id=self.id, part='snippet,statistics').execute()
        pprint(channel)
