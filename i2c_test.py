import smbus
import time
bus = smbus.SMBus(1)

address = 0x04

def writeNumber(value):
	bus.write_byte(address, value)
	return -1

def readNumber():
	number = bus.read_byte(address)
	return number
while True:	
	while True:
		var = input("Enter 0-9")
		if var > -1:
			break
		
	writeNumber(var)
	print("RPI: I sent to Arduino ",  var)
	time.sleep(1)

	number = readNumber()
	print("RPI: I got from Arduino: ", number)
	
