void setup() {
    Serial.begin(9600);   // Serial Monitor (for debugging)
    Serial1.begin(9600);  // Bluetooth module connected to Serial1 (TX1, RX1)
    
    Serial.println("Bluetooth Module Ready. Waiting for messages...");
}

void loop() {
    // Receiving data from laptop (via Bluetooth)
    if (Serial1.available()) {  
        String receivedMessage = "";
        while (Serial1.available()) {
            char receivedChar = Serial1.read();
            receivedMessage += receivedChar;
            delay(5);  // Small delay for better reading
        }
        
        Serial.print("Received: ");
        Serial.println(receivedMessage);  // Print message to Serial Monitor

        // Send acknowledgment back to the laptop
        Serial1.println("Arduino Received: " + receivedMessage);
    }

    // Sending data from Arduino to Laptop (optional)
    if (Serial.available()) {  // If input is entered in Serial Monitor
        String userMessage = Serial.readString();
        Serial1.println(userMessage);  // Send it via Bluetooth
        Serial.print("Sent to Laptop: ");
        Serial.println(userMessage);
    }
}
