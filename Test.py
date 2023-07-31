import serial.tools.list_ports

def get_connected_com_ports():
    com_ports = []
    available_ports = list(serial.tools.list_ports.comports())
    for port, desc, hwid in available_ports:
        com_ports.append(port)
    return com_ports

if __name__ == "__main__":
    connected_ports = get_connected_com_ports()
    if connected_ports:
        print("Connected COM ports:")
        for port in connected_ports:
            print(port)
    else:
        print("No COM ports are currently connected.")
