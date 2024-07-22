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
The icons have been designed by KorneliusVonTastik and can be downloaded here [https://ko-fi.com/kvtkorp](https://ko-fi.com/kvtkorp) - see [Original Reddit Post](https://www.reddit.com/r/starcitizen/comments/1dvfeq6/icon_pack_and_streamdeck_profiles_by_kvt_korp/). Buy him a coffee or two. The Icons will not be included in this repository.

## BOM
*1x Raspberry Pi Zero W 2: If you have the cash, you could also get a Raspberry Pi 4 .. but why? Raspberry Pi Zero W should do the trick too. If you get the Raspberry Pi Zero W 2 (as did I, make sure that you get an adapter from HDMI mini to FFC (something like this?)[https://amzn.eu/d/06kzbJqP] or at least from HDMI mini (male) to "normal" HDMI (female)
*1x Arduino pro Micro: I bought a knock-off. It has do be a Micro, Leonardo or any Arduino clone that is based on the ATmega32u4 though (see [https://github.com/MHeironimus/ArduinoJoystickLibrary](https://github.com/MHeironimus/ArduinoJoystickLibrary))
*1x Logic Level Converter (5v/3.3V)
*1x (LUCKFOX for Raspberry Pi Screen 7 inch HDMI Touchscreen for Raspberry Pi 5 Plug & Play 1024x600)[https://amzn.eu/d/09yGKScL]: I link this one specifically because the 3D printed files are specifically for this screen
*2x FrSky Taranis QX7 M7 Gimbal
*1x a simple button
some cables, some connectors, a prototype-boards or a breadboard, ... you will figure this out.

If you want to use my 3d printed files you will need
*25x M3x10mm screws (I love screws)
*1x M3x16mm screw
*26x M3 square nuts (they are 5,2mmx5,2mm and ~1.4mm thick) 
*4x M2,5x7mm screws for the touch screen. (M2,5x8mm should also fit - try at your own risk)
and a little bit of 3mm filament as dowels for the button-panels. You could also probably print those or mount the button somewhere else.

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
Write the [Star_Citizen_Controller.ino](https://github.com/Haskar/Star_Citizen_Controller/blob/713848e760347bb48a67777979dcc065e503b604/Arduino/Star_Citizen_Controller.ino)) to your Arduino. Once restarted it will create 4 Joysticks with 120 buttons each (up to 4 Joysticks work "stable" on windows). With one X- and Y-Axis  on joystick 1 and one X- and Y-Axis on joystick 2, the other joysticks are only there for the additional buttons. Buttons are automatically assigned to the joysticks. Currently Star Citizen allows up to 128 buttons per joystick ... 480 should be enough for our purpose.

#### Raspberry Pi
##### Initial Installation and Serial Port
Now this is where it gets messy
Start with a standard Raspbian Image. Activate SSH, VNC and Serial Port using
```bash
sudo raspi-config
```
install minicom 
```bash
sudo apt-get install minicom -y
```
and test the connection to the Arduino
```bash
minicom -b 115200 -o -D /dev/ttyS0
```

Optional: Install Samba for an easier transfer of files (Images for example)

##### Python Script
Create a folder for the python script in your home directory
```bash
mkdir controller
```
and a subfolder for the images
```bash
cd controller
mkdir images
```
while currently in the controller folder download the python script
```bash
wget https://github.com/Haskar/Star_Citizen_Controller/blob/713848e760347bb48a67777979dcc065e503b604/Raspberry%20Pi/controller/controller.py
```
then go to your images folder and download the "sample image"
```bash
cd images
https://github.com/Haskar/Star_Citizen_Controller/blob/b7ad4dfabad1206d7526e9e06b6d0be5ae7533fa/Raspberry%20Pi/controller/images/empty.png
```

or, if you bought KorneliusVonTastik a coffee (or five ... ) you can download the python script with some sample images and use samba to copy the colorscheme of your choice to the image folder.
```bash
wget https://github.com/Haskar/Star_Citizen_Controller/blob/713848e760347bb48a67777979dcc065e503b604/Raspberry%20Pi/controller/controller%20-%20KVT.py
```
##### Autostart Python Script 
Quick and dirty: 
```bash
cd ~
sudo nano start_controller.sh
sudo chmod +x start_controller.sh
```

this is the complete content of the start_controller.sh-file
```
#!/bin/sh
sleep 5
cd /home/pi/controller
export DISPLAY=:0
/usr/bin/python3 controller.py
sleep 3

if pidof python3; then
   echo
else
   /usr/bin/python3 controller.py
```

Then: 
```bash
cd ~/.config/
mkdir autostart
cd autostart
sudo nano controller_autostart.desktop
```

this is the complete content of the controller_autostart.desktop-file
```
[Desktop Entry]
Name=controller autostart
Comment=startet controller automatisch
Type=Application
Exec=/home/pi/start_controller.sh
Terminal=false
```

While you are at it, add a Link to your Raspi-Desktop:
```bash
cd ~/Desktop/
sudo nano controller.desktop
sudo chmod +x controller.desktop
```
this is the complete content of the controller.desktop-file. That's a lie ... I also have an awesome icon thanks to KorneliusVonTastik. You should really buy him a coffee or 12. 
```
[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=Controller
Exec=/usr/bin/python3 /home/pi/controller/controller.py
StartupNotify=false
Terminal=true
```

Reboot and hope for the best


##### Python Script tuning
This is my first "working" python script using tkinter. It is ugly and I don't like it, but I dont have to see it that much because it works.
You will have to change the code if you want to make the GUI the way you want it.
What you need to know: 
* every "page" is a frame.
* every frame can have 4*7 buttons (that's 28)
* this is how a frame is declared:
  ```
  frame_name= tkinter.Frame(master)
  frame014.configure(background=b_c_bg)
  ```
  The second line is optional.
  
  You will have to put it in the array of frames:
  ```
  for frame in (frame_name1, frame_name3, frame_name3)
  ```  
  You don't have to do anything else actually to add pages.
* I use 2 buttons: 
   ```
   i_flight_movement_gear_up_icon = resize_image("flight-movement_gear-up-icon.png", i_width, i_height)
   button_001_12=create_button(frame001, "", i_flight_movement_gear_up_icon, trigger, i_width, i_height)
   button_001_12.grid(row=1,column=2)
   trigger = trigger+1
   ```
   first line

  
