# OLED Example (SSD1306 on Raspberry Pi)

This repository contains **example Python code** showing how to use an
**SSD1306 OLED display** with a **Raspberry Pi** via the I2C bus.

It includes:
- `display_class.py` – a simple `LcdDisplayClass` wrapper around `adafruit_ssd1306`
- `main.py` – a basic example that writes `Hello World` to the display

## What you need

- Raspberry Pi
- SSD1306 OLED display (commonly `128x64`, I2C address `0x3C`)
- Python 3 installed
- Git installed

## Connection Guide
On The Raspberry Pi, Pins 1–9 are located on the header pins on the left hand side closest to the SD Card.

| Connection | Raspberry Pi | SSD1306 |  
|------------|--------------|---------|  
| 3v3        | 1            | 2       | 
| I2C Data   | 3            | 4       | 
| I2C Clock  | 5            | 3       |
| Ground     | 9            | 1       | 


## Step by step setup guide

### 1) Run an update on the Raspberry Pi
```bash
sudo apt update
sudo apt upgrade
```

### 2) Use the Raspberry Pi config manager to enable I2C
```bash
sudo raspi-config
```
- choose `3 Interface Options`  
- choose `I5 I2C`   
- choose `yes`  

### 3) Install the `python3-smbus` and `i2c-tools` packages

```bash
sudo apt install python3-smbus i2c-tools
```

### 4) Check the SSD1306 is connected to the I2C bus
Run the following command:
```bash
sudo i2cdetect -y 1 
```
you will get a response line this if the SSD1306 is connected, it will be detected at 0x3C:
```bash
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- 3c -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

### 5) Clone this repository
```bash
git clone https://github.com/westerlymerlin/oled-example.git
cd oled-example
```

### 6) Create a Python virtual environment (`venv`)

From the project root:
```bash
python3 -m venv .venv
```

If `python3` is not available, try:
```bash
python -m venv .venv
```

### 7) Activate the virtual environment
Linux / Raspberry Pi OS:
```bash
source .venv/bin/activate
```

### 8) Install the python dependencies
```bash
pip install -r requirements.txt
```

### 9) Run the example
```bash
python main.py
```
Expected behaviour: the OLED display shows `Hello World`.

## Notes
- This example uses the `board` and `adafruit-circuitpython-ssd1306` libraries for I2C communication and display control.
- If the display is not found, double-check wiring, I2C enablement, and the device address (`0x3C`).
