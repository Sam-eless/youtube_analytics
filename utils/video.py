from utils.channel import Channel


class Video:
    def __init__(self, video_id: str) -> None:
        """Инициализатор. Если пользователь передал id, с которым невозможно получить данные о видео по API,
         то у экземпляра инициализируется только свойство video_id, а остальные поля принимают значение None."""
        self.video_id = video_id
        try:
            self.video_info = Channel.get_service().videos().list(id=self.video_id, part='snippet,statistics').execute()
            self.title = self.video_info['items'][0]['snippet']['title']
            self.number_of_video_views = self.video_info['items'][0]['statistics']['viewCount']
            self.number_of_likes = self.video_info['items'][0]["statistics"]['likeCount']
            self.url_link = "https://www.youtube.com/watch?v=" + self.video_id
        except Exception:
            self.video_info = None
            self.title = None
            self.number_of_video_views = None
            self.number_of_likes = None
            self.url_link = None

    def __str__(self):
        """Выводит название видео на Ютуб"""
        return f'Youtube-видео: {self.title}'
