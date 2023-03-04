from datetime import timedelta

from utils.playlist import PlayList

pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')


def test_init():
    assert pl.url_link == 'https://www.youtube.com/playlist?list=PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb'
    assert pl.title == 'Редакция. АнтиТревел'


def test_total_duration():
    assert isinstance(pl.total_duration, timedelta) is True
    assert pl.total_duration.total_seconds() == 13261.0


def test_show_best_video():
    assert pl.show_best_video() == "https://www.youtube.com/watch?v=9Bv2zltQKQA"
