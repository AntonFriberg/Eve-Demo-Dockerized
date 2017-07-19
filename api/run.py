# -*- coding: utf-8 -*-

"""
    Eve API
    ~~~~~~~~

    A simple API powered by Eve REST API.

"""

import os
from eve import Eve

app = Eve()

# Simple hook example see Eve documentation for more
def codemotion(endpoint, response):
    for document in response['_items']:
        document['CODEMOTION'] = 'IS SO FREAKING COOL!'

app.on_fetched_resource += codemotion

if __name__ == '__main__':
    app.run(debug=True)
