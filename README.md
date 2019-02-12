# flask-periodic-table-template-demo

Based on code that was originally in:

* <https://github.com/ccs-cs20-w19/flask-periodic-demo-heroku>

We are showing how to build a web app that can take words and produce spellings of those words using chemical element symbols from the periodic table.

This version adds using Templates in Flask

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

  http://127.0.0.1:5000/make/someword

# Deployed on Heroku

This app is deployed on Heroku here:

https://flask-periodic-demo-heroku.herokuapp.com/

To show periodic table elements for a word, use:

https://flask-periodic-demo-heroku.herokuapp.com/make/someword


https://flask-periodic-demo-heroku.herokuapp.com/make/CCS

https://flask-periodic-demo-heroku.herokuapp.com/make/UCSB
