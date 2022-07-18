# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app
from app import TimelinePost

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        textresponse = response.get_data(as_text=True)
        assert "<title>Python Panther Portfolio</title>" in textresponse
        # TODO Add more tests relating to the home page
        assert '<img src="./static/img/juli.jpg"' in textresponse
        assert '<img src="./static/img/josh.jpg"' in textresponse
        assert '<img src="./static/img/maansi.jfif"' in textresponse

        assert "<h1 class=\"full-name\">Josh</h1>" in textresponse
        assert "<h1 class=\"full-name\">Maansi</h1>" in textresponse
        assert "<h1 class=\"full-name\">Juliette</h1>" in textresponse


    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        # TODO Add more tests relating to the /api/timeline_post GET and POST apis
        # TODO Add more tests relating to the timeline page
        textresponse = response.get_data(as_text=True)
        print("the text response: ",textresponse, sep="---")
        

    def test_timeline_page(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert '<button type="submit" class="timeline-button">' in html
        assert '<input name="name" type="text" class="timeline-input" placeholder="Name">' in html
        assert '<input name="email" type="text" class="timeline-input" placeholder="Email">' in html
        assert '<input name="content" type="text" class="timeline-input" placeholder="Message">' in html

    def test_malformed_timeline_post(self):
        response = self.client.post("/api/timeline_post", data = {
            "name": "John Doe",
            "email": "john@example.com",
            "content": ""
        })
        assert response.status_code == 400
        textresponse = response.get_data(as_text=True)
        assert "Invalid content" in textresponse

        response = self.client.post("/api/timeline_post", data = {
            "email": "john@example.com",
            "content": "Hello world, I\'m John!"
        })
        
        assert response.status_code == 400
        textresponse = response.get_data(as_text=True)
        assert "Invalid name" in textresponse

        response = self.client.post("/api/timeline_post", data = {
            "name": "John Doe",
            "email": "wrong_format",
            "content": "Hello world, I\'m John!"
        })
        assert response.status_code == 400
        textresponse = response.get_data(as_text=True)
        assert "Invalid email" in textresponse