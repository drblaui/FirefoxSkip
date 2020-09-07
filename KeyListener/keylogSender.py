import keyboard, mouse, asyncio, websockets

class KeylogSender:
	def __init__(self):
		"""
		Handle Hotkey registering and tell the server we are the logger
		"""

		#Change Hotkeys here
		"""
		Note that how these are called is language sensitive,
		so make sure you type these in your keyboard language!
		"""
		self.HOTKEY_SKIP = "ctrl+alt+nach-rechts"
		self.HOTKEY_BACK = "ctrl+alt+nach-links"
		asyncio.get_event_loop().run_until_complete(self.sendMessage("logger", "ws://localhost:9999/"))
		keyboard.add_hotkey(self.HOTKEY_SKIP, lambda: self.eventLoop("skip"))
		keyboard.add_hotkey(self.HOTKEY_BACK, lambda: self.eventLoop("back"))

	def eventLoop(self, message):
		"""
		Go into the next loop to prevent multithread errors
		"""
		loop = asyncio.set_event_loop(asyncio.new_event_loop())
		asyncio.get_event_loop().run_until_complete(self.sendMessage(message, "ws://localhost:9999/"))

	async def sendMessage(self, message, uri):
		"""
		Send a message to the server
		"""
		async with websockets.connect(uri) as websocket:
			await websocket.send(message)
			

	def listen(self):
		"""
		Keep program alive and wait on any input
		"""
		keyboard.wait()


# Init and loop
keylogSend = KeylogSender()
keylogSend.listen()

