import sched
from time import sleep, time
import win32gui, win32ui, win32con, win32api
import InputTest

ButtonMapping = {
	'w': 0x26,
	's': 0x28,
	'a': 0x25,
	'd': 0x27,
	'e': 0x5A,
	'q': 0x58,
	'start': 0x0D

}

def handle_response(message) -> str:
	currentMessage = message.lower()

	if currentMessage in ButtonMapping:
		InputTest.press_key(ButtonMapping[currentMessage], 0.2)
		return ''

	if currentMessage == 'sunshine is the best 3d mario game':
		return 'you need therapy'

	if currentMessage == 'galaxy 2 is the best 3d mario game':
		return 'correct'

	if 'odyssey' in currentMessage:
		return 'Odyssey is the best 3D Mario game'