import unittest
import os
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.getjson()
        assert "timeline_post" in json
        assert len(json["timeline_post"]) == 0

        def test_malformed_timeline_post(self):
            response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "this is a test"})
            assert response.status_code == 400
            html = response.get_data(as_text=True)
            assert "400 Bad Request" in html

            response = self.client.post("/api/timeline_post", data={"name": "john doe", "email": "john@example.com", "content": ""})
            assert response.status_code == 400
            html = response.get_data(as_text=True)
            assert "400 Bad Request" in html

            response = self.client.post("/api/timeline_post", data={"name": "john doe", "email": "not an email" , "content": "this is a test"})
            assert response.status_code == 400
            html = response.get_data(as_text=True)
            assert "400 Bad Request" in html
            


        