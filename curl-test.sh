echo "current requests:"
curl http://localhost:5000/api/timeline_post

echo "making a POST request"
curl --request POST http://localhost:5000/api/timeline_post -d 'name=juli&email=juli@gmail.com&content=hi hello there'

echo "requests with addition of new POST request"
curl http://localhost:5000/api/timeline_post