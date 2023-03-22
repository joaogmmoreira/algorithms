from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('test', 'a')

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 1)

    assert encrypt_message('encrypt', 3) == 'cne_tpyr'
    assert encrypt_message('message', 4) == 'ega_ssem'
    assert encrypt_message('arara', 5) == 'arara'
