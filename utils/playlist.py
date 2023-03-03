from datetime import timedelta
# from utils.plvideo import PLVideo
from utils.channel import Channel
class PlayList(PLVideo):

    def __init__(self, pl_id):
        super().__init__(pl_id)
        self.pl_info = Channel.get_service().playlists().list(part='snippet', id=pl_id, ).execute()
        self.title_pl = self.pl_info['items'][0]['snippet']['title']
        self.url_link = "https://www.youtube.com/playlist?list=" + self.video_id
        # self.pl_title = 1
        # self.url_link = 1

    @property
    def total_duration(self):
        pass


    def show_best_video(self):
        pass




pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')

pl.title
# Редакция. АнтиТревел

tl.url
# https://www.youtube.com/playlist?list=PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb

duration = pl.total_duration
print(duration)
# 3:41:01
print(type(duration))
# <class 'datetime.timedelta'>
print(duration.total_seconds())
# 13261.0

pl.show_best_video()
# https://youtu.be/9Bv2zltQKQA