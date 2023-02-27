from utils.channel import Channel
import pytest

lofi_girl = Channel('UCSJ4gkVC6NrvII8umztf0Ow')
vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')


def test_add():
    assert lofi_girl + vdud == int(vdud.number_of_subscriber) + int(lofi_girl.number_of_subscriber)
    with pytest.raises(ValueError):
        var = lofi_girl.__add__(100) == 'Передан не экземпляр класса Channel'


def test_lt():
    bool_val = lofi_girl < vdud
    assert bool_val is False
    with pytest.raises(ValueError):
        var = lofi_girl.__lt__(100) == 'Передан не экземпляр класса Channel'


def test_gt():
    bool_val = lofi_girl > vdud
    assert bool_val is True
    with pytest.raises(ValueError):
        var = lofi_girl.__gt__(100) == 'Передан не экземпляр класса Channel'


def test_str():
    assert vdud.__str__() == f'Youtube-канал: {vdud.title}'
