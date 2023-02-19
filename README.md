# flask
- https://auth0.com/blog/developing-restful-apis-with-python-and-flask/

# dockerfile
- basic web authentication: from flask_httpauth import HTTPBasicAuth


# built app with podman

```
podman build -t cashman .
podman run --name cashman -d -p 5000:5000 cashman
```

# run flask app for developing
```
./bootstrap.sh
```

# use app by curl from cmd line
```
curl http://localhost:5000/outcomes --user "roy:roy"
curl -X POST -H "Content-Type: application/json" -d '{  "description": "found",  "amount": 1200.0 }' http://localhost:5000/incomes --user "roy:roy" 
```
