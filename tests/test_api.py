import requests

def test_get_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()

    assert "userId" in data
    assert "title" in data


def test_get_post_negative():
    url = "https://jsonplaceholder.typicode.com/posts/999999"

    response = requests.get(url)

    assert response.status_code == 404
