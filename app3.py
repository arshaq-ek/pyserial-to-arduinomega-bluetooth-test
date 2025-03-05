import serial
import time
import tkinter as tk

# Replace 'COM8' with your Bluetooth port
bluetooth_serial = serial.Serial('COM8', 9600, timeout=1)
time.sleep(2)  # Wait for connection

def send_command(command):
    """Send command to Arduino."""
    bluetooth_serial.write(command.encode())
    print(f"Sent: {command}")

def stop_motors(event):
    """Send stop command when button is released."""
    send_command("S")

# Create GUI
root = tk.Tk()
root.title("Bluetooth Robot Controller")

# Define button actions
btn_up = tk.Button(root, text="↑ Forward", width=10, height=2)
btn_down = tk.Button(root, text="↓ Backward", width=10, height=2)
btn_left = tk.Button(root, text="← Left", width=10, height=2)
btn_right = tk.Button(root, text="→ Right", width=10, height=2)
btn_stop = tk.Button(root, text="■ Stop", width=10, height=2, command=lambda: send_command("S"))

# Bind button press and release events
btn_up.bind("<ButtonPress>", lambda event: send_command("F"))
btn_up.bind("<ButtonRelease>", stop_motors)

btn_down.bind("<ButtonPress>", lambda event: send_command("B"))
btn_down.bind("<ButtonRelease>", stop_motors)

btn_left.bind("<ButtonPress>", lambda event: send_command("L"))
btn_left.bind("<ButtonRelease>", stop_motors)

btn_right.bind("<ButtonPress>", lambda event: send_command("R"))
btn_right.bind("<ButtonRelease>", stop_motors)

# Grid layout
btn_up.grid(row=0, column=1, padx=5, pady=5)
btn_left.grid(row=1, column=0, padx=5, pady=5)
btn_stop.grid(row=1, column=1, padx=5, pady=5)
btn_right.grid(row=1, column=2, padx=5, pady=5)
btn_down.grid(row=2, column=1, padx=5, pady=5)

# Close connection on exit
def on_closing():
    print("Closing connection.")
    bluetooth_serial.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

print("Connected to Bluetooth. Hold buttons to move.")
root.mainloop()
