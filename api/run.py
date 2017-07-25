# -*- coding: utf-8 -*-

"""
    Eve API
    ~~~~~~~~

    A simple API powered by Eve REST API.

"""
from eve import Eve

app = Eve()

# Simple hook example see Eve documentation for more


def codemotion(endpoint, response): # pylint: disable=W0613
    for document in response['_items']:
        document['CODEMOTION'] = 'IS SO FREAKING COOL!'

# pylint: disable=E1101
app.on_fetched_resource += codemotion
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
