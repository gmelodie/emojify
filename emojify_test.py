import emojify

def test_happy():
    test = "I am happy"
    expected = "I am \u1F60"

    actual = emojify.emojify(test)
    assert actual == expected


def test_sad():
    test = "I am sad"
    expected = "I am \uFE0F"

    actual = emojify.emojify(test)
    assert actual == expected


def test_confused():
    test = "I am confused"
    expected = "I am \uF615"

    actual = emojify.emojify(test)
    assert actual == expected
