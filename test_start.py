import pytest


def soma_1(num):
    return int(num) + 1


""" Passando um inteiro e somando 1 """


def test_soma_1():
    assert soma_1(41) == 42


""" Passando uma inteiro que está como string(mas é um número)
conseguimos converter para int """


def test_soma_1_numero_como_string():
    assert soma_1("41") == 42


""" Passando um string que não tem como ser convertida para inteiro
vai apontar um erro
 """


def test_soma_1_palavra():
    with pytest.raises(ValueError):
        soma_1("Denis")
