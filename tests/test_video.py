from utils.video import Video
import pytest

video = Video('9lO06Zxhu88')


def test_init():
    assert video.url_link == "https://www.youtube.com/watch?v=9lO06Zxhu88"
    assert video.title == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'


def test_str():
    assert video.__str__() == f'Youtube-видео: {video.title}'


def test_except_init():
    video1 = Video("broken_video_id")
    assert video1.video_id == "broken_video_id"
    assert video1.video_info is None
    assert video1.title is None
