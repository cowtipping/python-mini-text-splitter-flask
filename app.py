from flask import Flask, request, render_template_string
from text_splitter import split_text, DEFAULT_MAX_LENGTH, remove_timestamps

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

        # Remove timestamps if option is selected
        if remove_timestamp:
            text = remove_timestamps(text)

        # Update max_length if provided by user
        if max_length_input.isdigit():
            max_length = int(max_length_input)

        parts = split_text(text, max_length=max_length)

    return render_template_string(
        """
        <html>
            <head>
                <style>
                    .text-part {
                        border: 1px solid #000;
                        padding: 10px;
                        margin: 10px 0;
                        position: relative;
                    }
                    .copy-button {
                        position: absolute;
                        top: 10px;
                        right: 10px;
                    }
                </style>
            </head>
            <body>
                <h1>Text Splitter</h1>
                    <form method="post">
                        <label for="text">Text:</label><br>
                        <textarea name="text">{{ text }}</textarea><br>
                        <label for="max_length">Max Length:</label>
                        <input type="text" name="max_length" value="{{ max_length }}"><br>
                        <input type="checkbox" name="remove_timestamps" id="remove_timestamp" {{ 'checked' if remove_timestamp else '' }}>
                        <label for="remove_timestamp">Remove Timestamps</label><br>
                        <input type="submit" value="Submit">
                    </form>
                <h2>Results</h2>
                {% for part in parts %}
                    <div class="text-part">
                        <button class="copy-button" id="copy-button-{{ loop.index }}" onclick="copyToClipboard('part{{ loop.index }}', '{{ loop.index }}')">Copy</button>
                        <h3>Part {{ loop.index }}</h3>
                        <p id="part{{ loop.index }}">{{ part }}</p>
                    </div>
                {% endfor %}
                <script>
                    function copyToClipboard(elementId, buttonId) {
                        var text = document.getElementById(elementId).innerText;
                        var button = document.getElementById('copy-button-' + buttonId);
                        navigator.clipboard.writeText(text).then(function() {
                            // Change button text to indicate success
                            button.innerHTML = 'Copied to clipboard!';
                            // Change it back after 2 seconds
                            setTimeout(function() {
                                button.innerHTML = 'Copy';
                            }, 2000);
                        }).catch(function(err) {
                            console.error('Error in copying text: ', err);
                        });
                    }
                </script>
            </body>
        </html>
        """,
        text=text,
        max_length=max_length,
        parts=parts,
        remove_timestamp=remove_timestamp,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)
