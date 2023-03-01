from utils.video import Video
import pytest

video1 = Video('9lO06Zxhu88')


def test_init():
    assert video1.url_link == "https://www.youtube.com/watch?v=9lO06Zxhu88"
    assert video1.title == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'


def test_str():
    assert video1.__str__() == f'Youtube-видео: {video1.title}'
