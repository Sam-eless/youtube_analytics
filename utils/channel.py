import os
import json
from googleapiclient.discovery import build


class Channel:
    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str):
        self.__id = channel_id
        self.channel = self.get_service().channels().list(id=self.__id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.chanel_description = self.channel["items"][0]['snippet']['description']
        self.url_link = "https://www.youtube.com/channel/" + self.__id
        self.number_of_subscriber = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.number_of_videos = self.channel["items"][0]["statistics"]["videoCount"]
        self.number_of_views = self.channel["items"][0]["statistics"]["viewCount"]

    @property
    def id(self):
        """Возвращает id канала."""
        return self.__id

    def print_info(self):
        """Вывод информации о канале"""
        print(self.channel_info())

    def channel_info(self, path=None):
        """Сохранение всех атрибутов объекта channel, кроме json, в файл по адресу path"""
        channel_info = {}
        for i in self.__dict__:
            if i != 'channel':
                channel_info[i] = self.__dict__[i]
        channel_info = json.dumps(channel_info, indent=4, ensure_ascii=False)
        return channel_info

    def save_to_json_file(self, path):
        with open(path, "w", encoding="UTF-8") as file:
            file.write(self.channel_info(path) + ',\n')

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с API YouTube"""
        with build('youtube', 'v3', developerKey=cls.api_key) as youtube:
            return youtube
