flask && dockerfile:

https://auth0.com/blog/developing-restful-apis-with-python-and-flask/

basic web authentication: from flask_httpauth import HTTPBasicAuth


USAGE:

podman build -t cashman .

podman run --name cashman -d -p 5000:5000 cashman


curl http://localhost:5000/outcomes --user "roy:roy"

curl -X POST -H "Content-Type: application/json" -d '{  "description": "vyplata",  "amount": 1200.0 }' http://localhost:5000/incomes --user "roy:roy" 
