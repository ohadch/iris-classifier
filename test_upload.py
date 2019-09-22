from utils.upload import allowed_file


def test_allowed_file():
    assert allowed_file('png')
    assert allowed_file('jpg')
    assert allowed_file('jpeg')
    assert not allowed_file('xls')
