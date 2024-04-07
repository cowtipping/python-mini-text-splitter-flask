from app.modules.text_analysis import count_characters, count_words


def test_count_characters():
    assert count_characters("") == 0
    assert count_characters("Hello, World!") == 13
    assert count_characters("Lorem ipsum dolor sit amet") == 26
    assert count_characters("12345") == 5
    assert count_characters("Hello, World! 12345") != 10


def test_count_words():
    assert count_words("") == 0
    assert count_words("Hello, World!") == 2
    assert count_words("Lorem ipsum dolor sit amet") == 5
    assert count_words("12345") == 1
    assert count_words("Hello, World! 12345") == 3
    assert count_words("Hello, World! 12345") != 2
