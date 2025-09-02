# API random writer

This random writer is designed as a "user" of the
dockerized web server
[Flask API](https://github.com/TomasKindahl/flask-API)
alternatively of
[NodeJS API](https://github.com/TomasKindahl/node-API).

## Running the random writer on its own

Starting it on its own needs
[Python requests](https://docs.python-requests.org/en/latest/user/install/#python-m-pip-install-requests),
either by using pip

```
python -m pip install requests
```

or by installing it via your Linux distro repository,
in Debian like distros the package name is
`python3-requests`, if not installed automatically,
installable through:

```
sudo apt update
sudo apt install python3-requests
```

## Running the random writer in Docker

You can also build and run the random writer in docker.
Then you need to adjust the Dockerfile so that it calls
the appropriate web address, like:

```
CMD ["python", "apiwriter.py", "http://localhost:5010"]
```

You can build it using the commands (for any
<code><i><b>n</b></i></code>):

<pre>
docker build -t apiwriter:v<i><b>n</b></i>
docker run -d -p 5010:8001 apiwriter:v<i><b>n</b></i>
</pre>

