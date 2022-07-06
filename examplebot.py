import math, threading, time

from pymcbot.client import Client
from pymcbot.event import Event

import PySimpleGUI as sg

walk_angle = 0


def attack_handler(client):
    print("Ow")
    client.message("Ow!")


def death_handler(client):
    print(":(")
    client.message(":(")


def update_handler(client):
    global walk_angle
    client.walk(walk_angle, 1)
    walk_angle += math.pi / 8


if __name__ == '__main__':
    import sys

    layout = [
        [sg.Text("Username"), sg.Input(key="user")],
        [sg.Text("Hostname"), sg.Input(key="host")],
        [sg.Text("Port"), sg.Input(key="port", default_text="25565")],
        [sg.Checkbox("Debug Mode", key="debug")],
        [sg.Button("Log in", key="login", bind_return_key=True)],
        [sg.Button("Exit", key="exit")],
    ]
    win = sg.Window("examplebot using pymcbot", layout)
    while True:
        event, values = win.read()
        if event in (sg.WIN_CLOSED, "exit"):
            win.close()
            exit()
        elif event == "login":
            win.close()
            debug = values["debug"]
            host = values["host"]
            port = int(values["port"])
            username = values["user"]
            break

    layout = [
        [sg.Text()],
#        [sg.Multiline(reroute_stdout=True, autoscroll=(not debug), size=(100, 35), write_only=True)],
        [sg.Input(key="console", size=(90, 1)), sg.Button("Send", k="send", bind_return_key=True)],
    ]
    win = sg.Window("example bot using pymcbot", layout, finalize=True)

    main_client = Client(debug)
    main_client.set_event_handler(Event.BOT_HURT, attack_handler)
    main_client.set_event_handler(Event.BOT_DEAD, death_handler)
    main_client.set_update(update_handler)
    main_client.login(host, port, username)

    while not main_client.is_logged_in:
        time.sleep(0.25)

    while main_client.is_logged_in:
        event, values = win.read(timeout=1)
        if event in (sg.WIN_CLOSED, "quit"):
            main_client.disconnect()
            break
        elif event == "send":
            main_client.send_message(values["console"])

    win.close()
