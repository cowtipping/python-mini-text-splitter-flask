# Text Splitter
A Python mini project.

Paste in a text document and the app will split it into multiple parts. It was built with YouTube transcripts in mind, hence the additional option to remove timestamps.

## Demo

TODO: [add link, gif]

## Local Installation

These instructions assume you have **Python** and **pip** installed already. If you don't (and I find that very hard to believe), [go here and grab it](https://www.python.org/). Python 3.4+ comes with pip installed already.

**Clone the repo:**

Pick your poison.  
HTTPS `https://github.com/cowtipping/python-mini-text-splitter-flask.git`  
SSH `git@github.com:cowtipping/python-mini-text-splitter-flask.git`

**Install dependencies:**

`pip install -r requirements.txt`

**Run the from root directory:**

`python app.py`

It will spin up a server pointing to port 5001. You can change the port number in `app.py`

View app by visiting `http://127.0.0.1:5001/` in your web browser. If you've changed the port number then replace 5001 with your port number.

## Tests

Run tests from root directory:

`pytest` or `python -m pytest`  
`pytest -v` or `python -m pytest -v` will give you a slightly more verbose output.

## Motivation

- I was pasting YouTube transcripts into chatbots to summarise them, and some were too long.
- I made this tool to split up transcripts into smaller chunks to cut and paste in over a series of messages, ordering the chatbot to summarise it after I had pasted all the messages.
- As there are already YouTube summarisers which do this job much better, I didn't put much more effort in than that and used it as a catalyst for trying **Flask** for the first time.