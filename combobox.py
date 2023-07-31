import serial

def read():
    try:
        ser = serial.Serial('COM5', 9600, timeout=5)
        try:
            rs = ser.readline().decode("utf-8")
            if(rs != None and rs[3] == '1'):
                seperatedData = rs.split(",")
                # for x in seperatedData:
                #     print(x)
                print(seperatedData[2])

        except IndexError:
                # s1 = "Not getting value"
                print("Not getting value")
    except:
        print("COM port not connected")
if __name__ == "__main__":
    # Replace 'COMx' with the actual serial port name (e.g., 'COM3' on Windows, '/dev/ttyUSB0' on Linux)
    # serial_port = 'COM3'
    # baud_rate = 9600
    read()
    # read_serial_data(serial_port, baud_rate)