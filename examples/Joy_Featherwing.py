from board import *
import busio
import Adafruit_seesaw
import time
from micropython import const

BUTTON_RIGHT = const(6)
BUTTON_DOWN  = const(7)
BUTTON_LEFT  = const(9)
BUTTON_UP    = const(10)
BUTTON_SEL   = const(14)
button_mask = const( (1 << BUTTON_RIGHT) | (1 << BUTTON_DOWN) | (1 << BUTTON_LEFT) | (1 << BUTTON_UP) | (1 << BUTTON_SEL) )

myI2C = busio.I2C(SCL, SDA)

ss = Adafruit_seesaw.Seesaw(myI2C)

ss.pinModeBulk(button_mask, ss.INPUT_PULLUP);

last_x = 0
lasy_y = 0

while True:
	x = ss.analogRead(2)
	y = ss.analogRead(3)
	  
	if  (abs(x - last_x) > 3) or (abs(y - last_y) > 3):
		print(x, y)
		last_x = x
		last_y = y

	buttons = ss.digitalReadBulk(button_mask)
	if not (buttons & (1 << BUTTON_RIGHT)):
		print("Button A pressed")

	if not (buttons & (1 << BUTTON_DOWN)):
		print("Button B pressed")

	if not (buttons & (1 << BUTTON_LEFT)):
		print("Button Y pressed")

	if not (buttons & (1 << BUTTON_UP)):
		print("Button x pressed")

	if not (buttons & (1 << BUTTON_SEL)):
		print("Button SEL pressed")

	time.sleep(.01)