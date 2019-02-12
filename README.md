# flask-periodic-demo-heroku

Demo Flask Periodic Table on Heroku

Minimum viable product demo integrating wordmaker and Flask, with deployment on Heroku


# Dependencies

You will need to use "pip install ..." to install these modules

```
pip install flask
pip install gunicorn
```

# To Run

You should run from the command line, not from inside IDLE

```
$ export FLASK_APP=hello.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/
```

Then put a web browser to `http://127.0.0.1:5000/`

To show periodic table elements for a word, use:

  http://127.0.0.1:5000/someword

# Deployed on Heroku

This app is deployed on Heroku here:

https://flask-periodic-demo-heroku.herokuapp.com/

To show periodic table elements for a word, use:

https://flask-periodic-demo-heroku.herokuapp.com/someword


https://flask-periodic-demo-heroku.herokuapp.com/CCS

https://flask-periodic-demo-heroku.herokuapp.com/UCSB
