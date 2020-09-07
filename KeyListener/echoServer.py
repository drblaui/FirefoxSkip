import asyncio, websockets
#Simple Echo server


# For message sending
sockets = {"browser": None, "logger": None}

async def echo(websocket, path):
	"""
	Make sure we have the newest socket to message to
	and message it if we read skip or back
	"""
	async for message in websocket:
		print("Got message:", message)

		if(message == "browser" or message == "logger"):
			sockets[message] = websocket

		if(message == "skip"):
			await sockets["browser"].send("skip")

		if(message == "back"):
			await sockets["browser"].send("back")
		

asyncio.get_event_loop().run_until_complete(
	#Use Port 9999 so it doesn't intefere with users localhost
	websockets.serve(echo, 'localhost', 9999))
asyncio.get_event_loop().run_forever()