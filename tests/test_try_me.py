from coolproject.lib import try_me

def test_try():
    assert try_me(13,8,21) == True
    assert try_me(13,9,23) == False
