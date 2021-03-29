import matplotlib.pyplot as plt
import serial
from time import sleep

# Erstellt eine leere Liste
squares = []

# Erstellt die Verbindung zum "Serial Monitor" des Arduino
Ser = serial.Serial("COM4", 115200, timeout=1)

# Speichert die Ausgabewerte in die Liste
for i in range(1, 20):

    data = Ser.readline().decode()
    print(data)

    squares.insert(i, data)

    sleep(1)
    i += 1

Ser.close()

# Plottet die Ausgabe
plt.plot(squares)
plt.show()
