import os
import json
from googleapiclient.discovery import build


class Channel:


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала.
Дальше все данные будут подтягиваться по API."""
        self.api_key = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey = self.api_key)
        self.channel_id = channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.youtube.channels().list(id
    = self.channel_id, part = 'snippet, statistics').execute()))