#include <Arduino.h>
#include <IRremoteESP8266.h>
#include <IRsend.h>
#include <ir_Samsung.h>
// --------------------- Temp and Humidity ---------------------
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>
// ************************************************************
#define DHTPIN 15     // Digital pin connected to the DHT sensor

// Uncomment the type of sensor in use:
#define DHTTYPE    DHT11     // DHT 11

unsigned long startTime;
const unsigned long timerDuration = 10000;  // 10 seconds in milliseconds

// See guide for details on sensor wiring and usage:
//   https://learn.adafruit.com/dht/overview

DHT_Unified dht(DHTPIN, DHTTYPE);

uint32_t delayMS;



const uint16_t kIrLed = 5;  // Use the correct GPIO pin for your IR LED. COnnect the LED to D5
IRSamsungAc ac(kIrLed);
IRsend irTransmitter(kIrLed);

void printState() {
  // Display the settings.
  Serial.println("Samsung A/C remote is in the following state:");
  Serial.printf("  %s\n", ac.toString().c_str());
}

void setup() {
  ac.begin();
  Serial.begin(115200);
  delay(200);

  Serial.println("Default state of the remote.");
  printState();
  Serial.println("Setting initial state for A/C.");
  ac.off();
  ac.setFan(kSamsungAcFanLow);
  ac.setMode(kSamsungAcCool);
  ac.setTemp(25);
  ac.setSwing(false);
  printState();

  // -------------------------------
    irTransmitter.begin();

  // --------------- DHT - Temp and Humidity ----------------
    // Initialize device.
  dht.begin();
  Serial.println(F("DHTxx Unified Sensor Example"));
  // Print temperature sensor details.
  sensor_t sensor;
  pinMode(5, OUTPUT);

  // Store the current time as the start time
  startTime = millis();
  // ---------------- LEDs ---------------------
  pinMode(21,OUTPUT);
  pinMode(22,OUTPUT);
  pinMode(23,OUTPUT);
  digitalWrite(21,LOW);
  digitalWrite(22,LOW);
  digitalWrite(23,LOW);


}

void sendIRCode(unsigned long code) {
  irTransmitter.sendRC5(code, 14); // Adjust protocol and bits per code if needed
}

void blinkPin(int pin, int duration) {
  digitalWrite(pin, HIGH);
  delay(duration);
  digitalWrite(pin, LOW);
  delay(duration);
  digitalWrite(pin, HIGH);

}

void loop() {
  //  ------------- DHT - Temp and Humidity -------------
      // Get the current time
  unsigned long currentTime = millis();

  // Check if 5 seconds have elapsed
  if (currentTime - startTime >= timerDuration) {
    // Your code to execute after 5 seconds
    // Serial.println("Timer expired! Do something.");
    // Get temperature event and print its value.
    sensors_event_t event;
    dht.temperature().getEvent(&event);
    if (isnan(event.temperature)) {
      Serial.println(F("Error reading temperature!"));
    }
    else {
      Serial.print(F("Temperature: "));
      Serial.print(event.temperature);
      Serial.println(F("°C"));
    }
    // Get humidity event and print its value.
    dht.humidity().getEvent(&event);
    if (isnan(event.relative_humidity)) {
      Serial.println(F("Error reading humidity!"));
    }
    else {
      Serial.print(F("Humidity: "));
      Serial.print(event.relative_humidity);
      Serial.println(F("%"));
    }


    // Reset the timer for the next iteration
    startTime = currentTime;
  }
  // *********************************************************

  // ---------------------- IR Remote ------------------------
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n'); // Read the entire line.
    if (command == "ac_on") {
      Serial.println("Turn on the A/C ...");
      ac.on();
      ac.send();
      printState();

      digitalWrite(21,HIGH);

    } else if (command == "ac_off") {
      Serial.println("Turn off the A/C ...");
      ac.off();
      ac.send();
      printState();

      digitalWrite(21,LOW);
      } else if (command == "ac_cool_mode") {
      Serial.println("Set the A/C mode to cooling ...");
      ac.setMode(kSamsungAcCool);
      ac.send();
      printState();
      blinkPin(21, 100);


    } else if (command == "ac_fan_up") {
      Serial.println("Increase the fan speed ...");
      ac.setFan(kSamsungAcFanHigh);
      ac.setSwing(true);
      ac.send();
      printState();

      digitalWrite(21,HIGH);
      delay(100);
      digitalWrite(21,LOW);
      delay(100);
      digitalWrite(21,HIGH);

    } else if (command == "ac_fan_down") {
      Serial.println("Set the A/C to fan only with a low speed, & no swing ...");
      ac.setSwing(false);
      ac.setMode(kSamsungAcFan);
      ac.setFan(kSamsungAcFanLow);
      ac.send();
      printState();

      digitalWrite(21,HIGH);
      delay(100);
      digitalWrite(21,LOW);
      delay(100);
      digitalWrite(21,HIGH);

    } else if (command.startsWith("set_temp ")) {
      String tempValue = command.substring(9); // Remove "set_temp " from the command.
      int temp = tempValue.toInt(); // Convert the remaining part to an integer.
      if (temp >= 16 && temp <= 30) {
        Serial.print("Setting temperature to ");
        Serial.println(temp);
        ac.on();
        ac.setTemp(temp);
        ac.send();
        printState();

      digitalWrite(21,HIGH);
      delay(100);
      digitalWrite(21,LOW);
      delay(100);
      digitalWrite(21,HIGH);

    } else if (command.startsWith("set_timer ")) {
      String tempValue = command.substring(11); // Remove "set_timer " from the command.
      int temp = tempValue.toInt(); // Convert the remaining part to an integer.
      if (temp >= 60 && temp <= 720) {
        Serial.print("Setting Timer to ");
        Serial.println(temp);
        ac.setOffTimer(temp);
        ac.send();
        printState();

      digitalWrite(21,HIGH);
      delay(100);
      digitalWrite(21,LOW);
      delay(100);
      digitalWrite(21,HIGH);

      }

      // --------------- Dish TV ----------------------
    } else if(command == "dish_0") {
      sendIRCode(0x28A1); 
      Serial.println("DISH TV - 0");
      printState();
      digitalWrite(21,HIGH);


    } else if(command == "dish_1") {
      sendIRCode(0x38A2); 
      Serial.println("DISH TV - 1");
      printState();
      digitalWrite(21,LOW);


    } else if(command == "dish_2") {
      sendIRCode(0x28A4); 
      Serial.println("DISH TV - 2");
      printState();

    } else if(command == "dish_3") {
      sendIRCode(0x38A7); 
      Serial.println("DISH TV - 3");
      printState();

    } else if(command == "dish_4") {
      sendIRCode(0x28A8); 
      Serial.println("DISH TV - 4");
      printState();

    } else if(command == "dish_5") {
      sendIRCode(0x28AB); 
      Serial.println("DISH TV - 5");
      printState();

    } else if(command == "dish_6") {
      sendIRCode(0x28AD); 
      Serial.println("DISH TV - 6");
      printState();

    } else if(command == "dish_7") {
      sendIRCode(0x38AE); 
      Serial.println("DISH TV - 7");
      printState();

    } else if(command == "dish_8") {
      sendIRCode(0x2891);
      Serial.println("DISH TV - 8");
      printState();

    } else if(command == "dish_9") {
      sendIRCode(0x2892); 
      Serial.println("DISH TV - 9");
      printState();

    } else if(command == "dish_mute") {
      sendIRCode(0x38B9); 
      Serial.println("DISH TV - Mute");
      printState();

    } else if(command == "dish_vol_up") {
      sendIRCode(0x38C2); 
      Serial.println("DISH TV - Vol up");
      printState();

    } else if(command == "dish_vol_down") {
      sendIRCode(0x3894); 
      Serial.println("DISH TV - vol down");
      printState();

    } else if(command == "projector_on") {
      irTransmitter.sendNEC(0x4FA0, 8);
      Serial.println("Projector_on");
      printState();

    }
  }
}
}