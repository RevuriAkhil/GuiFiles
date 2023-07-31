#import library called serial to use serial ports
import serial

ser = serial.Serial("COM5", 9600,timeout=1) #added
#discrad what ever in the serial port before sending commands
#com.flush()
#print(ser.readline()) 
#functions to send command give a string as parameter
def sendCommand(command):
    ser.write(command.encode('utf-8'))

#this code will run forever untill we stop it in terminal similler to void loop() 
while True:
    inpdata = ser.readline().decode("ascii")#added
    # print(inpdata)
    # print(len(inpdata))
    

    if(inpdata != None and inpdata[0] == '$' and inpdata[33] == '#'):
        if(inpdata[2] == '1'):
            sepdata = inpdata.split(",")
            # sendCommand("E P C")
            # sendCommand(sepdata[1])
            # sendCommand(sepdata[2])
            # sendCommand(sepdata[3])
            # sendCommand(sepdata[4])
            # sendCommand(sepdata[5])
            print("E P C")
            print("------")
            print(sepdata[1])
            print(sepdata[2])
            print(sepdata[3])
            print(sepdata[4])
            print(sepdata[5])
        if(inpdata[2] == '2' or inpdata[2] == '3'):
            sepdata = inpdata.split(",")
            # sendCommand("E M C")
            # sendCommand(sepdata[1])
            # sendCommand(sepdata[2])
            # sendCommand(sepdata[3])
            # sendCommand(sepdata[4])
            # sendCommand(sepdata[5])
            # sendCommand(sepdata[6])
            print("E M C")
            print('-----')
            print(sepdata[1])
            print(sepdata[2])
            print(sepdata[3])
            print(sepdata[4])
            print(sepdata[5])
            last = sepdata[6]
            print(last[:4])

        
    #sendCommand(inpdata)#added
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()