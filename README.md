flask && dockerfile from:
https://auth0.com/blog/developing-restful-apis-with-python-and-flask/

USAGE:

podman build -t cashman .

podman run --name cashman -d -p 5000:5000 cashman
