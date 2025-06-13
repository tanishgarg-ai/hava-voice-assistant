
# 🤖 HAVA – Home Automation Voice Assistant

A voice-controlled offline smart home automation system using **Python**, **Vosk**, **Arduino (ESP32)**, and a custom GUI.

> Created as part of the Semester 1 Project for BE-CSE (Artificial Intelligence), Chitkara University

---

## ✨ Features

- 🎙️ Offline voice recognition using **Vosk**
- 🗣️ Wake word detection with **Porcupine**
- 💡 Control devices like **TV** and **AC**
- 🧠 Conditional command handling via **local Python logic**
- 🌡️ Real-time humidity and temperature monitoring (DHT11)
- 📊 Custom GUI built with **CustomTkinter**
- 🔊 Audio feedback with **pyttsx3** and **playsound**
- 🛠️ Communication with **ESP32** over serial

---

## 🖥️ GUI Preview

The interface includes:
- A **main menu** for selecting device control (TV/AC)
- Full **TV remote emulation**
- AC control with **temperature dials** and **mode selection**

_Screenshots can be added here if available._

---

## 🧰 Hardware Requirements

- ✅ ESP32 development board
- ✅ DHT11 sensor (Temperature & Humidity)
- ✅ IR LED, Normal LED
- ✅ Jumper cables, Resistors
- ✅ Arduino IDE or PlatformIO for flashing the ESP32

---

## 🔌 ESP32 Serial Communication Setup

This project **communicates with the ESP32 via serial port**:

- In `main.py`, locate and update the following line with your actual port:
  ```python
  ser = serial.Serial('COM18', 115200)  # Replace COM18 with your correct COM port

* You can find your COM port:

  * Windows: Check **Device Manager > Ports (COM & LPT)**
  * Linux: Usually `/dev/ttyUSB0` or `/dev/ttyS#`
  * Mac: `/dev/cu.SLAB_USBtoUART` or similar

### 🧩 Mandatory Driver – CP210x

Most ESP32 boards use the **CP2102 USB-to-Serial chip**. You **must install the driver**:

👉 [Download CP210x Driver (Silicon Labs)](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)

---

## 💻 Software Dependencies
### 🔐 Picovoice AccessKey Required
To use wake word detection (Porcupine), you must create a **free account** at [Picovoice Console](https://console.picovoice.ai/) and generate your own **AccessKey**.

### Install all Python packages in one step using:
`pip install -r requirements.txt`


### 🧠 Vosk Model Setup (Required)

This project uses the offline voice recognition model: `vosk-model-en-in-0.5`.

Please download it from the official site:

👉 [Download Vosk Model (en-in)](https://alphacephei.com/vosk/models)

After downloading:
- Extract the folder (e.g., `vosk-model-en-in-0.5`)
- Place it in the project directory or anywhere you'd like
- Update the path in `main.py` accordingly:

or use the script `python other_files/download_model.py`

### 🔌 ESP32 Serial Communication Setup

This project **communicates with an ESP32 board via a serial connection** and requires uploading a specific program to the ESP32.

#### ✅ Step-by-Step ESP32 Setup

1. **Install the CP210x USB Driver**
   Most ESP32 boards use a CP2102 USB-to-Serial chip. You **must install the driver** for your board to show up as a COM port:
   * 👉 [CP210x USB-to-UART Bridge VCP Drivers – Silicon Labs](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)

2. **Open the Arduino IDE or PlatformIO**

   * Install **ESP32 board support** via the Board Manager (search: `esp32`)
   * Select the appropriate **board** and **COM port**

3. **Upload the Provided ESP32 Code**

   * Open the file `esp32_code.ino` (or the provided Arduino `.ino` file)
   * Click **Upload** to flash it to your ESP32
   * Ensure that the **baud rate** in the Arduino code matches this line in `main.py`:

     ```python
     ser = serial.Serial('COM18', 115200)  # Change COM18 to your actual COM port
     ```






---

