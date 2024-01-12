"""Run me from parent folder with python -m app.app"""

from flask import Flask, request, render_template

from app.modules.text_splitter import split_text, DEFAULT_MAX_LENGTH, remove_timestamps

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    parts = []
    max_length = DEFAULT_MAX_LENGTH
    remove_timestamp = False

    if request.method == "POST":
        text = request.form["text"]
        max_length_input = request.form.get("max_length", "")
        remove_timestamp = "remove_timestamps" in request.form

        if remove_timestamp:
            text = remove_timestamps(text)

        if max_length_input.isdigit():
            max_length = int(max_length_input)

        parts = split_text(text, max_length=max_length)

    return render_template(
        "index.html",
        text=text,
        max_length=max_length,
        parts=parts,
        remove_timestamp=remove_timestamp,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)
