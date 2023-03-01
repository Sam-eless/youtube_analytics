from utils.video import Video
from utils.channel import Channel


class PLVideo(Video):
    def __init__(self,video_id: str, pl_id: str) -> None:
        super().__init__(video_id)
        self.pl_id = pl_id
        # self.pl_info = Channel.get_service().playlistItems().list(part="snippet", playlistId=pl_id).execute()
        self.pl_info = Channel.get_service().playlists().list(part='snippet', id=pl_id, ).execute()
        self.title_pl = self.pl_info['items'][0]['snippet']['title']

    def __str__(self):
        return f'{self.title} ({self.title_pl})'