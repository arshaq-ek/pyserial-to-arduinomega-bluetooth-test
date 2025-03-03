import serial
import time

# Replace 'COM6' with your Bluetooth port (Check Device Manager on Windows)
bluetooth_serial = serial.Serial('COM7', 9600, timeout=1)
time.sleep(2)  # Wait for connection

print("Connected to Bluetooth. Type messages below:")

try:
    while True:
        message = input("You: ")
        bluetooth_serial.write(message.encode())  # Send message to Arduino
        
        if message.lower() == "exit":
            print("Closing connection.")
            break
        
        # Receive response from Arduino
        response = bluetooth_serial.readline().decode().strip()
        if response:
            print("Arduino:", response)

except KeyboardInterrupt:
    print("\nConnection closed.")

bluetooth_serial.close()
