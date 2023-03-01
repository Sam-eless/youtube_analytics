from utils.plvideo import PLVideo
import pytest

video = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')


def test_init():
    assert video.url_link == "https://www.youtube.com/watch?v=BBotskuyw_M"
    assert video.title_pl == "Литература"


def test_str():
    assert video.__str__() == f'{video.title} ({video.title_pl})'
