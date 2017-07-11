import requests
from faker import Factory


def main():
    url = 'http://localhost:5000/people'
    fake = Factory.create('de_DE')

    for i in range(0, 20000):
        name = fake.name().split()
        firstname = name.pop()
        lastname = " ".join(name)
        data = {"firstname": firstname, "lastname": lastname}
        response = requests.post(url, data=data)
        if not response.ok:
            print(response.text)


if __name__ == '__main__':
    main()
