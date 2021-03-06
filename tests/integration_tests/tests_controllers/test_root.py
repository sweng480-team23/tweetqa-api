from flask.testing import FlaskClient


def test_root(app: FlaskClient):
    response = app.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b'"The TweetQA Api is running!"\n'
