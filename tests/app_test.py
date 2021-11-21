from controllers import app

def test_root():
    tester = app.app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b'"The TweetQA Api is running!"\n'