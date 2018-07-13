# -*- coding: utf-8 -*-

"""
    Eve API
    ~~~~~~~~

    A simple API powered by Eve REST API.

"""
from eve import Eve

app = Eve()


@app.route('/hello')
def hello_world():
    return 'hello world!'
