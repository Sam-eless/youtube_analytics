import os
import json
from googleapiclient.discovery import build


class Channel:
    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, id: str):
        self.__id = id
        self.json = ""
        self.to_json()
        self.title = self.json['items'][0]['snippet']['title']
        self.chanel_description = self.json["items"][0]['snippet']['description']
        self.url = "https://www.youtube.com/channel/" + self.__id
        self.video_count = self.json["items"][0]["statistics"]["videoCount"]
        self.channel_number_of_views = self.json["items"][0]["statistics"]["viewCount"]

    @property
    def id(self):
        return self.__id

    def print_info(self):
        """Вывод информации о канале"""
        print(self.json)

    def save_json_in_file(self, path):
        """Сохранение всех атрибутов объекта channel, кроме json, в файл по адресу path"""
        json_text = {}
        for i in self.__dict__:
            if i != 'json':
                json_text[i] = self.__dict__[i]
        json_text = str(json_text).replace(',', ',\n')
        json_text = '[' + json_text + '] \n'
        # json_text = json.dumps(json_text, indent=4)
        with open(path, "w", encoding="UTF-8") as file:
            file.write(json_text + '\n')

    def to_json(self):
        """Создание объекта для работы с API YouTube"""
        channel = self.get_service().channels().list(id=self.__id, part='snippet,statistics').execute()
        self.json = channel

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube"""
        with build('youtube', 'v3', developerKey=cls.api_key) as youtube:
            return youtube
