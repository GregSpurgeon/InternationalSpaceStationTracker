#!/usr/bin/env python
import requests

__author__ = '???'


def get_astronaunts_info():
    r = requests.get('http://api.open-notify.org/astros.json')
    raw_data = r.json()
    print(f"There are currently {raw_data['number']} astronaunts in space")
    people = raw_data['people']
    for person in people:
        for _ in person:
            print(person['name'] + " is on board " + person['craft'])
            break


def get_geographic_coordinates():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    raw_data = r.json()
    print("timestamp =", raw_data['timestamp'])
    iss_position = raw_data['iss_position']
    for k, v in iss_position.items():
        print(f"{k} is {v}")


def main():
    get_astronaunts_info()
    get_geographic_coordinates()


if __name__ == '__main__':
    main()
