#!/usr/bin/env python
import requests
import turtle
import time

__author__ = 'Greg Spurgeon with help from Kevin Clark and Joseph'


def get_astronaunts_info():
    """This function get all the astronaunts in space, their name and what
        craft they are on"""
    r = requests.get('http://api.open-notify.org/astros.json')
    raw_data = r.json()
    print(f"There are currently {raw_data['number']} astronaunts in space")
    people = raw_data['people']
    for person in people:
        for _ in person:
            print(person['name'] + " is on board " + person['craft'])
            break


def get_geographic_coordinates():
    """Retrives the current location of the international space station"""
    r = requests.get('http://api.open-notify.org/iss-now.json')
    raw_data = r.json()
    print("timestamp =", raw_data['timestamp'])
    iss_position = raw_data['iss_position']
    for k, v in iss_position.items():
        print(f"current ISS {k} is {v}")
    return iss_position


def over_indy():
    """Displays the next time the ISS will be over Indianapolis"""
    host = 'http://api.open-notify.org'
    path = '/iss/v1/?lat=39.768380&lon=-86.1580400&alt=1650&n=1'
    r = requests.get(host + path)
    raw_data = r.json()
    date = raw_data["response"][0]["risetime"]  # dict drilling down "risetime"
    realtime = time.ctime(date)  # convert timestamp to human readable time
    return realtime


def turtle_screen():
    """Creates a display of the world with the ISS current location.
        Places a yellow dot over Indianapolis along with the next date and
        time the space sation will be over Indianapolis """
    # displaying world map
    sc = turtle.Screen()
    sc.setup(720, 360)
    sc.bgpic("map.gif")
    turtle.setworldcoordinates(-180, -90, 180, 90)
    sc.register_shape("iss.gif")

    # dispaly position of ISS as graphic
    iss = turtle.Turtle(shape="iss.gif")
    iss.setheading(90)
    iss.penup()
    cords = get_geographic_coordinates()  # this function call returns a dict
    iss.goto(float(cords["longitude"]), float(cords["latitude"]))

    # Places a yellow dot representing Indianapolis
    indy_dot = turtle.Turtle(shape="circle")
    indy_dot.color("yellow")
    indy_dot.turtlesize(0.3)
    indy_dot.penup()
    indy_dot.setpos(-86.1580400, 39.7683800)

    # Renders readable timestamp for next time ISS is over Indianapolis
    readable_time = turtle.Turtle()
    readable_time.color("white")
    readable_time.penup()
    readable_time.setpos(-80, 39.7683800)
    readable_time.write(over_indy())

    turtle.done()


def main():
    get_astronaunts_info()
    turtle_screen()


if __name__ == '__main__':
    main()
