
from pymcbot.bot import Client
from pymcbot.event import Event

def attack_handler(client):
	client.message("Ow!")

def death_handler(client):
	client.message(":(")

if __name__=='__main__':
	import sys
	if len(sys.argv) > 2:
		if sys.argv[1] == "-d":
			debug = True
			i = 2
		else:
			debug = False
			i = 1
		username = sys.argv[i]
		host = sys.argv[i+1]

		client = Client(debug)
		if len(sys.argv) > i+2:
			client.connect(host, sys.argv[i+2])
		else:
			client.connect(host)

		client.set_event_handler(Event.BOTHURT, attack_handler)
		client.set_event_handler(Event.BOTDEAD, death_handler)
		client.login(username, run=False)
		while client.is_running:
			client.update()

	else:
		print("Usage: walkingBot [-d] username host [port]")
