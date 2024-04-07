import pytest
from app import app as flask_app


@pytest.fixture
def app():
    """
    Returns the Flask app object.
    """
    yield flask_app


@pytest.fixture
def client(app):
    """
    Returns a test client for the Flask application.

    Parameters:
    - app: The Flask application object.

    Returns:
      A test client for the Flask application.
    """
    return app.test_client()


def test_index_get(client):
    """
    Test the GET request for the index route.

    Args:
      client: The Flask test client.

    Returns:
      None
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"text" in response.data  # Check for a keyword in your rendered template


def test_index_post(client):
    """
    Test the POST request to the index route.

    Args:
      client: The Flask test client.

    Returns:
      None

    Raises:
      AssertionError: If any of the assertions fail.
    """
    response = client.post(
        "/",
        data={
            "text": "Sample text",
            "max_length": "100",
            "remove_timestamps": True,
        },  # Take out the remove_timestamps key to check for value="False" assetion
    )
    assert response.status_code == 200
    assert b"Sample text" in response.data
    assert b"100" in response.data
    # assert that remove_timestamps returns the boolean value False
    assert (
        b'<input type="hidden" id="remove_timestamp_value" value="True">'
        in response.data
    )
