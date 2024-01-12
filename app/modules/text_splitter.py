import re

DEFAULT_MAX_LENGTH = 20_000


def split_text(text, max_length=DEFAULT_MAX_LENGTH):
    """
    Splits a text string into parts of up to max_length characters without breaking words.

    :param text: The text string to be split.
    :param max_length: The maximum length of each part.
    :return: A list of text parts.
    """
    parts = []
    while text:
        # If the remaining text is shorter than the max length, add it as a part
        if len(text) <= max_length:
            parts.append(text)
            break

        # Find the nearest space before the max_length
        split_index = text.rfind(" ", 0, max_length)

        # If no space is found, default to max_length
        if split_index == -1:
            split_index = max_length

        # Add the part and trim the text
        parts.append(text[:split_index])
        text = text[split_index:].lstrip()

    return parts


def remove_timestamps(text):
    """
    Removes timestamps from the text more selectively.
    Timestamps are typically isolated and followed by text or at the beginning of a line.
    """
    timestamp_pattern = r"(^|\s)\d{1,2}:\d{2}(?::\d{2})?(\s|$)"
    return re.sub(timestamp_pattern, " ", text)
