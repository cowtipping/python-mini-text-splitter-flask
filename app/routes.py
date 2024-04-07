from flask import render_template, request
from app import app
from app.modules.text_splitter import split_text, DEFAULT_MAX_LENGTH, remove_timestamps
from app.modules.text_analysis import count_words, count_characters


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Renders the index page and processes the form.

    Handles the HTTP GET and POST requests for the index page.
    Retrieves the form data, processes the text, and calculates word and character counts.
    If an error occurs, it prints the error message and can be extended to render an error page or return an error response.

    Returns:
        The rendered index.html template with the processed text, maximum length, text parts, remove timestamp flag,
        word count, and character count.
    """
    original_text = ""
    parts = []
    max_length = DEFAULT_MAX_LENGTH
    remove_timestamp = False
    word_count = 0
    character_count = 0

    try:
        if request.method == "POST":
            original_text = request.form["text"]
            text_to_process = original_text
            max_length_input = request.form.get("max_length", "")
            remove_timestamp = "remove_timestamps" in request.form

            if remove_timestamp:
                text_to_process = remove_timestamps(text_to_process)

            if max_length_input.isdigit():
                max_length = int(max_length_input)

            parts = split_text(text_to_process, max_length=max_length)

            word_count = count_words(text_to_process)
            character_count = count_characters(text_to_process)

    except Exception as e:
        print(f"An error occurred: {e}")
        # TODO: Render an error page or return a response with an error message

    return render_template(
        "index.html",
        text=original_text,
        max_length=max_length,
        parts=parts,
        remove_timestamp=remove_timestamp,
        word_count=word_count,
        character_count=character_count,
    )
