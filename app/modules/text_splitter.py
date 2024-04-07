import re

DEFAULT_MAX_LENGTH = 30_000


def split_text(text, max_length=DEFAULT_MAX_LENGTH):
    """
    Splits a text string into parts of up to max_length characters without breaking words.

    :param text: The text string to be split.
    :param max_length: The maximum length of each part.
    :return: A list of text parts.
    """
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    if not isinstance(max_length, int):
        raise ValueError("max_length must be an integer")

    parts = []
    while text:
        if len(text) <= max_length:
            parts.append(text)
            break

        split_index = text.rfind(" ", 0, max_length)

        if split_index == -1:
            split_index = max_length

        parts.append(text[:split_index])
        text = text[split_index:].lstrip()

    return parts


def remove_timestamps(text):
    """
    Removes timestamps from the text.
    For YT videos, timestamps are typically isolated and followed by text or at the beginning of a line.
    """
    if not isinstance(text, str):
        raise ValueError("text must be a string")

    timestamp_pattern = r"(^|\s)\d{1,2}:\d{2}(?::\d{2})?(\s|$)"
    return re.sub(timestamp_pattern, " ", text)
