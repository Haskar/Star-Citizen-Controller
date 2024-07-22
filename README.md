# Star Citizen Controller WIP
Disclaimer: This is my first published project ever, so expect the worst and maybe you will be surprised (but I wouldn't count on it)
This is the repository of a 4-Axis Star Citizen Controller using a Raspberry pi and a Touchscreen as a Macropad

<img src="https://github.com/Haskar/Star_Citizen_Controller/blob/7c51cf232cdad70b0568458f5b99c814c59720e9/pictures/bd804097-d34a-4821-94e8-2e508bc554db.jpg" width=800/>

## Intro and credits
The work is based on a controller by [Tinker Player Solder Pi](https://www.youtube.com/@TinkerPlayerSolderPi) 
I used the footage of his controller as a loose guide:
[Custom space flight controller - first flight in Star Citizen] (https://www.youtube.com/watch?v=7e5ViENf0X4)
[How I built a custom joystick for Star Citizen] (https://www.youtube.com/watch?v=LTITm7ulwR4)
He also mentioned in one of the replies to the videos, that he was working on a [Version 2](https://imgur.com/a/custom-6dof-joystick-with-touchscreen-interface-NOEMydg)

As Arduino Library I used [Arduino Joystick Library 2.1.1](https://github.com/MHeironimus/ArduinoJoystickLibrary) by [MHeironimus](https://github.com/MHeironimus)
The icons have been designed by [KorneliusVonTastik] and can be downloaded here [https://ko-fi.com/kvtkorp](https://ko-fi.com/kvtkorp) - see [Original Reddit Post](https://www.reddit.com/r/starcitizen/comments/1dvfeq6/icon_pack_and_streamdeck_profiles_by_kvt_korp/). Buy him a coffee or two. The Icons will not be included in this repository.

## BOM
1x Raspberry Pi Zero W 2: If you have the cash, you could also get a Raspberry Pi 4 .. but why? Raspberry Pi Zero W should do the trick too. If you get the Raspberry Pi Zero W 2 (as did I, make sure that you get an adapter from HDMI mini to FFC (something like this?)[https://amzn.eu/d/06kzbJqP] or at least from HDMI mini (male) to "normal" HDMI (female)
1x Arduino pro Micro: I bought a knock-off. It has do be a Micro, Leonardo or any Arduino clone that is based on the ATmega32u4 though (see [https://github.com/MHeironimus/ArduinoJoystickLibrary](https://github.com/MHeironimus/ArduinoJoystickLibrary))
1x Logic Level Converter (5v/3.3V)
1x (LUCKFOX for Raspberry Pi Screen 7 inch HDMI Touchscreen for Raspberry Pi 5 Plug & Play 1024x600)[https://amzn.eu/d/09yGKScL]: I link this one specifically because the 3D printed files are specifically for this screen
2x FrSky Taranis QX7 M7 Gimbal
1x a simple button
some cables, some connectors, a prototype-boards or a breadboard, ... you will figure this out.

## Instructions
### Step1: Hardware
<img src="https://github.com/Haskar/Star_Citizen_Controller/blob/7c51cf232cdad70b0568458f5b99c814c59720e9/pictures/Screenshot%202024-07-22%20123810.png" width=800/>
sidenote: this is my first schematic drawn with fritzing

#### Wiring the joysticks: 
* Arduino 5V - Taranis M7 red wire
* Arduino GND - Taranis M7 (1 and 2) black wire
* Arduino GND - Taranis M7 (1 and 2) black wire
* Arduino A0 - Taranis M7 (1) yellow wire (my be a different color for you)
* Arduino A1 - Taranis M7 (1) green wire (my be a different color for you)
* Arduino A2 - Taranis M7 (2) yellow wire (my be a different color for you)
* Arduino A3 - Taranis M7 (2) green wire (my be a different color for you)

#### Wiring the serial connection Arduino/Raspberry Pi: 
* Arduino 5V - Logic Converter HV
* Arduino GND - Logic Converter GND
* Arduino TX - Logic Converter TX (HV side)
* Arduino RX - Logic Converter RX (HV side)

* Raspberry Pi 3V (Pin 1) - Logic Converter LV
* Raspberry Pi GND (Pin 9) - Logic Converter GND (LV side, not sure if this is necessary or best practice as I have seen diagrams with only one GND being used)
* Raspberry Pi TX (Pin 8) - Logic Converter RX (LV side) - this is intentionally connected TX to RX
* Raspberry Pi RX (Pin 10) - Logic Converter TX (LV side) - this is intentionally connected RX to TX

#### Wiring the Boot-Button: 
* Raspberry Pi GND (Pin 14) - Button (Pin 1)
* Raspberry Pi GPIO 3 (Pin 5) - Button (Pin 2)

#### Misc: 
* Raspberry Pi 5V (Pin 2), Raspberry Pi 5V (Pin 4) and Raspberry Pi GND (Pin 6) will be connected to the Touchscreen
* Raspberry Pi USB-Port will be connected to the Touchscreen (for the Touch functionality)
* Raspberry Pi HDMI Port will be connected to the Touchscreen

### Step2: Software
#### Arduino
Write the [Star_Citizen_Controller.ino](https://github.com/Haskar/Star_Citizen_Controller/blob/main/Star_Citizen_Controller.ino) to your Arduino. It will create 4 Joysticks with 120 buttons each (up to 4 Joysticks work "stable" on windows). With one Gimbal on joystick 1 and the other Gimbal on joystick 2, the other joysticks are only there for the additional buttons. Buttons are automatically assigned to the joysticks. Currently Star Citizen allows up to 128 buttons per joystick.

#### Raspberry Pi
Now this is where it gets messy
Start with a standard Raspbian Image. Activate SSH, VNC and Serial Port using
```bash
sudo raspi-config
```

Create a folder for the python script in your home directory
```bash
mkdir controller
```

and a subfolder for the images
```bash
cd controller
mkdir images
```
copy 
