#!/bin/bash

curl --request GET http://104.131.10.43:5000/api/timeline_post

curl --request POST http://104.131.10.43:5000//api/timeline_post -d 'name=Wei&email=wei.he@mlh.io&content=Testing my endpoints with postman.'

curl http://104.131.10.43:5000/api/timeline_post
