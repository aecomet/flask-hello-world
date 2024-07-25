# flask-hello-world

flask sample app

## How to use

```sh
pyenv local 3.12.4

# upgrade pip
pip install --upgrade pip

# install pipenv
# pipenv includes a role of venv
pip install pipenv

# create virtualenv with ppipenv command
pipenv install

# run virtualenv
pipenv shell

# show virtualenv path
pipenv --venv

# install package
pip install flask

# export package versions
pip freeze > requirements.txt
pipenv requirements > requirements-pipenv.txt
```

## Development with flask

```sh
# hoge ... root app (NG: flask.py because it conflicts original flask module)
flask --app hoge run

# As a shortcut, if the file is named app.py or wsgi.py, you don’t have to use --app.
flask run

# watch mode
flask run --debug
```

### Use gunicorn

```sh
pip install gunicorn

# simple use
gunicorn myapp.main:app

# with config
gunicorn -c myapp/gunicorn.conf.py myapp.main:app
```

## Trouble shooting

```sh
Shell for UNKNOWN_VIRTUAL_ENVIRONMENT already activated.
No action taken to avoid nested environments.
# => restart your shell
```