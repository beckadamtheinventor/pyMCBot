
from pymcbot.bot import Client
from pymcbot.event import Event

def attack_handler(client):
	client.message("Ow!")

def death_handler(client):
	client.message(":(")

if __name__=='__main__':
	import sys
	if len(sys.argv) > 2:
		username = sys.argv[1]
		host = sys.argv[2]

		client = Client()
		if len(sys.argv) > 3:
			client.connect(host, port)
		else:
			client.connect(host)

		client.set_event_handler(Event.BOTHURT, attack_handler)
		client.set_event_handler(Event.BOTDEAD, death_handler)
		client.login(username, run=False)
		while client.is_running:
			client.update()

	else:
		print("Usage: walkingBot username host [port]")
