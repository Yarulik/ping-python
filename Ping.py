#!/usr/bin/python -u

import struct
import serial

#Open the serial port
ser = serial.Serial('/dev/ttyUSB0', 115200)
#ser = serial.Serial('/dev/tty.usbserial-A5059KLC', 115200)

#Sonar report packet
#452 Bytes
packetFormat = "<ccHHhiiiiihhhhiIIhHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHcc"


while True:
    buf = []
    data = ""

    try:
        #Burn through data until start signal
        while(ser.read() != "s"):
            pass
        #Check second start signal
        if (ser.read() != "s"):
            break

        #Add start signal to buffer, since we have a valid message
        buf.append("s")
        buf.append("s")
        data += struct.pack("<B", 83)
        data += struct.pack("<B", 83)

        #Get the content of the message
        for i in range(0,450):
            byte = ser.read()
            data += struct.pack("<c", byte)
            buf.append(byte)

        unpacked = struct.unpack(packetFormat, data)

        print(unpacked)
        print()

    except(Exception, e):
        print("Error: "+str(e))
        pass
