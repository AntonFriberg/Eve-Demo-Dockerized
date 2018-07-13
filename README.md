# Eve-Demo-Dockerized

A fully featured RESTful Web API powered by Eve. Based on official Eve-Demo.

If you need a gentle introduction to the wondeful world of RESTful WEB APIs,
check out Nicola's EuroPython 2012 talk

[Developing RESTful Web APIs with Python, Flask and MongoDB](https://speakerdeck.com/nicola/developing-restful-web-apis-with-python-flask-and-mongodb)

## Getting Started

Simply navigate inside the project folder and run
```
docker-compose up
```

### Prerequisites

What things you need to install the software and how to install them

* docker >= 18.03.1-ce
* docker-compose >= 1.20

## Using the api

For an example of a client application that uses the api see the included `client.py` file. It deletes all entries and inserts example data. 

## Deployment

Deploy in production environment at your own risk. Consult official Eve, Flask and Docker documentation beforehand. 

## Built With

* [Eve](http://python-eve.org) - The web framework used for easy rest-api development
* [MongoDB](https://www.mongodb.com/) - Document-oriented Database
* [Docker](https://rometools.github.io/rome/) - Software container platform
* [Docker Compose](https://docs.docker.com/compose/) - Easy management of Docker containers
* [Python Docker Image](https://hub.docker.com/_/python/) - Official Python Docker Image
* [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) - Deployment Server

## Authors

* **Eve Developers** - *Initial work* - [Eve-Demo](https://github.com/pyeve/eve-demo/)
* **Anton Friberg** - *Dockerization* - [Profile](https://github.com/AntonFriberg/)

## License

This project is based on previous work see [LICENSE](LICENSE) file for more information.
Also note the docker image [licence](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/LICENSE.txt).

## Acknowledgments

* Hat tip to anyone who's code was used
