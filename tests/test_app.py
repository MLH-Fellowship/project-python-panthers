import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Python Panther Portfolio</title>" in html
        assert '<img src="./static/img/josh.jpg"' in html
        assert '<img src="./static/img/maansi.jfif"' in html
        assert '<img src="./static/img/juli.jpg"' in html

    def test_timeline(self):
        html = self.client.get("/timeline").get_data(as_text=True)
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        assert '<button type="submit">' in html


    def test_malformed_timeline_post(self):
        response = self.client.post("/api/timeline_post", data=
{"email": "john@example.com", "context": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html


        response = self.client.post("/api/timeline_post", data=
{"name": "John Doe", "email": "john@example.com", "context": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        response = self.client.post("/api/timeline_post", data=
{"name": "John Doe", "email": "not-an-email", "context": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
