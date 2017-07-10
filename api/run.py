# -*- coding: utf-8 -*-

"""
    Eve API
    ~~~~~~~~

    A simple API powered by Eve REST API.

"""

import os
from eve import Eve

app = Eve()

if __name__ == '__main__':
    app.run(debug=True)
