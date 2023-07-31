import serial
from time import sleep
# Create a serial connection
print("welcome to seral")
ser = serial.Serial('COM5', 9600,timeout=1)  # Replace 'COM4' with your actual port and set the appropriate baud rate
while 1:
    rs = ser.readline()
    decoded_data = rs.decode("utf-8")
    # try:
    #     decoded_data = rs.decode('utf-8')
    # except UnicodeDecodeError:
    #    decoded_data = rs.decode('latin-1')
    if(rs != None):
        print("rs:"+decoded_data)
    else:
        print("check com-port")
        

        

