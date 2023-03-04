from datetime import timedelta
import isodate
from utils.channel import Channel


class PlayList:

    def __init__(self, pl_id):
        self.pl_id = pl_id
        self.pl_info = Channel.get_service().playlists().list(part='snippet', id=pl_id).execute()
        self.title = self.pl_info['items'][0]['snippet']['title']
        self.url_link = "https://www.youtube.com/playlist?list=" + self.pl_id
        self.pl_videos = Channel.get_service().playlistItems().list(playlistId=self.pl_id, part='contentDetails',
                                                                    maxResults=50, ).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.pl_videos['items']]
        self.video_response = Channel.get_service().videos().list(part='contentDetails,statistics',
                                                                  id=','.join(self.video_ids)).execute()

    @property
    def total_duration(self):
        """Возвращает суммарную длительность плейлиста
        в виде объекта класса datetime.timedelta"""
        total_duration = timedelta(0, 0, 0)
        for video in self.video_response['items']:
            # Длительности YouTube-видео представлены в ISO 8601 формате
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration

    def show_best_video(self):
        """Печатает и возвращает ссылку на самое популярное видео
        из плейлиста (по количеству лайков)."""
        id_top_video = None
        count_likes = 0
        for video_id in self.video_ids:
            video_info = Channel.get_service().videos().list(part='snippet,statistics', id=video_id).execute()
            iter_count = int(video_info['items'][0]['statistics']['likeCount'])
            if iter_count > count_likes:
                count_likes = iter_count
                id_top_video = video_id
        print("https://www.youtube.com/watch?v=" + id_top_video)
        return "https://www.youtube.com/watch?v=" + id_top_video
