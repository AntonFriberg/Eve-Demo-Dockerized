Eve-Demo-Dockerized
========

A fully featured RESTful Web API powered by Eve_. Based on official Eve-Demo_.

If you need a gentle introduction to the wondeful world of RESTful WEB APIs,
check out my EuroPython 2012 talk: `Developing RESTful Web APIs with Python,
Flask and MongoDB
<https://speakerdeck.com/nicola/developing-restful-web-apis-with-python-flask-and-mongodb>`_

There is also a sample client application available. It uses the Requests
library to consume the demo. In fact it has been quickly hacked together to
reset the API every once in a while. Check it out at
https://github.com/pyeve/eve-demo-client.
 
*Note*. The demo is currently running v0.0.4 of the Eve framework. Eve-Demo is
only updated when major Eve updates are released. Please refer to the official
Eve repository for an up-to-date features list. 

.. _Eve: http://python-eve.org
.. _Eve
.. _run.py: https://github.com/pyeve/eve-demo/blob/master/run.py
.. _settings.py: https://github.com/pyeve/eve-demo/blob/master/settings.py

# Eve-Demo-Dockerized

A fully featured RESTful Web API powered by Eve. Based on official Eve-Demo.

## Getting Started

Simply navigate inside the project folder and run
```
docker-compose up
```

### Prerequisites

What things you need to install the software and how to install them

* Docker >= 17.06.0-ce
* docker-compose >= 1.14.0

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Deploy in production environment at your own risk. Consult official Eve (Flask) and Docker documentation before deploying. 

## Built With

* [Eve](http://python-eve.org) - The web framework used for easy rest-api development
* [MongoDB](https://www.mongodb.com/) - Database used by default by Eve
* [Docker](https://rometools.github.io/rome/) - Software container platform
* [Docker Compose](https://docs.docker.com/compose/) - Easy management of Docker containers

## Authors

* **Eve Developers** - *Initial work* - [Eve-Demo](https://github.com/pyeve/eve-demo/)
* **Anton Friberg** - *Dockerization* - [Profile](https://github.com/AntonFriberg/)

## License

This project is based on previous work see [LICENSE](LICENSE) file for more information.

## Acknowledgments

* Hat tip to anyone who's code was used
