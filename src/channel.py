import os
import json

import googleapiclient
from googleapiclient.discovery import build


class Channel:


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала.
Дальше все данные будут подтягиваться по API."""
        self.api_key = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey = self.api_key)
        self.__channel_id = channel_id
        self.get_channel_info()


    def __str__(self):
        """Магия str"""
        return f"{self.title} ({self.url})"


    def __add__(self, other):
        """Магия + """
        return self.subscribers + other.subscribers


    def __sub__(self, other):
        """Магия - """
        return self.subscribers - other.subscribers


    def __lt__(self, other):
        """Магия < """
        return self.subscribers < other.subscribers


    def __le__(self, other):
        """Магия <="""
        return self.subscribers <= other.subscribers


    def __gt__(self, other):
        """Магия > """
        return self.subscribers > other.subscribers


    def __ge__(self, other):
        """Магия >="""
        return self.subscribers >= other.subscribers

    @property


    def channel_id(self):
        """Геттер ID"""
        return self.__channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.youtube.channels().list
(id = self.channel_id, part = 'snippet,statistics').execute()))


    def get_channel_info(self):
        """Получение инфо о канале"""
        youtube = googleapiclient.discovery.build("youtube",
"v3", developerKey = self.api_key)
        request = youtube.channels().list(part =
"snippet,statistics", id = self.__channel_id)
        response = request.execute()
        if 'items' in response:
            channel_data = response['items'][0]
            self.id = self.__channel_id
            self.title = channel_data['snippet']['title']
            self.description = channel_data['snippet']['description']
            self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
            self.subscribers = int(channel_data['statistics']
['subscriberCount'])
            self.video_count = int(channel_data['statistics']['videoCount'])
            self.view_count = int(channel_data['statistics']['viewCount'])
        else:
            print("Channel not found.")

    @classmethod
    def get_service(cls):
        """Возврат объекта для работы с API YT"""
        api_key = os.getenv('YT_API_KEY')
        return build("youtube", "v3", developerKey = api_key)


    def to_json(self, filename):
        """Конверт в json"""
        data = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "link": self.url,
            "subscribers": self.subscribers,
            "video_count": self.video_count,
            "view_count": self.view_count
     }

        with open(filename, "w") as json_file:
            json.dump(data, json_file, indent = 2)
