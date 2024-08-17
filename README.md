# Star Citizen Controller WIP
Disclaimer: This is my first published project ever, so expect the worst and maybe you will be surprised (but I wouldn't count on it)
This is the repository of a 4-Axis Star Citizen Controller using a Raspberry pi and a Touchscreen as a Macropad

<img src="https://github.com/Haskar/Star_Citizen_Controller/blob/main/pictures/Controller_front.jpg" width=750/>


<p float="left">
  <img src="https://github.com/Haskar/Star_Citizen_Controller/blob/main/pictures/Controller_side.jpg" width="250" />
  <img src="https://github.com/Haskar/Star_Citizen_Controller/blob/main/pictures/Controller_back.jpg" width="250" /> 
  <img src="https://github.com/Haskar/Star_Citizen_Controller/blob/main/pictures/Controller_back_2.jpg" width="250" />
</p>
The hot-glue work on those connectors look much better in real life ... I was actually pretty proud of it ... it looks like a trainwreck in these pictures :(

## Intro and credits
The work is based on a controller by [Tinker Player Solder Pi](https://www.youtube.com/@TinkerPlayerSolderPi) 
I used the footage of his controller as a loose guide:
[Custom space flight controller - first flight in Star Citizen] (https://www.youtube.com/watch?v=7e5ViENf0X4)
[How I built a custom joystick for Star Citizen] (https://www.youtube.com/watch?v=LTITm7ulwR4)
He also mentioned in one of the replies to the videos, that he was working on a [Version 2](https://imgur.com/a/custom-6dof-joystick-with-touchscreen-interface-NOEMydg)

As Arduino Library I used [Arduino Joystick Library 2.1.1](https://github.com/MHeironimus/ArduinoJoystickLibrary) by [MHeironimus](https://github.com/MHeironimus)
The icons have been designed by KorneliusVonTastik and can be downloaded here [https://ko-fi.com/kvtkorp](https://ko-fi.com/kvtkorp) - see [Original Reddit Post](https://www.reddit.com/r/starcitizen/comments/1dvfeq6/icon_pack_and_streamdeck_profiles_by_kvt_korp/). Buy him a coffee or two. The Icons will not be included in this repository.

## BOM
* 1x Raspberry Pi Zero W 2: If you have the cash, you could also get a Raspberry Pi 4 .. but why? Raspberry Pi Zero W should do the trick too. If you get the Raspberry Pi Zero W 2 (as did I, make sure that you get an adapter from HDMI mini to FFC (something like this?)[https://amzn.eu/d/06kzbJqP] or at least from HDMI mini (male) to "normal" HDMI (female)
* 1x Arduino pro Micro: I bought a knock-off. It has do be a Micro, Leonardo or any Arduino clone that is based on the ATmega32u4 though (see [https://github.com/MHeironimus/ArduinoJoystickLibrary](https://github.com/MHeironimus/ArduinoJoystickLibrary))
* 1x Logic Level Converter (5v/3.3V)
* 1x (LUCKFOX for Raspberry Pi Screen 7 inch HDMI Touchscreen for Raspberry Pi 5 Plug & Play 1024x600)[https://amzn.eu/d/09yGKScL]: I link this one specifically because the 3D printed files are specifically for this screen
* 2x FrSky Taranis QX7 M7 Gimbal
* 1x a simple button
some cables, some connectors, a prototype-boards or a breadboard, ... you will figure this out.

If you want to use my 3d printed files you will need
* 25x M3x10mm screws (I love screws) (24 for iteration 2)
* 1x M3x16mm screw (iteration 2 of the does not need this screw anymore)
* 26x M3 square nuts (they are 5,2mmx5,2mm and ~1.4mm thick) 
* 4x M2,5x7mm screws for the touch screen. (M2,5x8mm should also fit - try at your own risk)
* Some thin EVA foam because, as it turns out ... plastic is quite hard and does not feel so good on your wrist after a while ... 
and a little bit of 3mm filament as dowels for the button-panels. You could also probably print those or mount the button somewhere else.

## Instructions
### Step1: Hardware
<img src="https://github.com/Haskar/Star_Citizen_Controller/blob/7c51cf232cdad70b0568458f5b99c814c59720e9/pictures/Screenshot%202024-07-22%20123810.png" width=800/>
sidenote: this is my first schematic drawn with fritzing

#### Wiring the joysticks: 
* Arduino 5V - Taranis M7 red wire
* Arduino GND - Taranis M7 (1 and 2) black wire
* Arduino GND - Taranis M7 (1 and 2) black wire
* Arduino A0 - Taranis M7 (1) yellow wire (may be a different color for you)
* Arduino A1 - Taranis M7 (1) green wire (may be a different color for you)
* Arduino A2 - Taranis M7 (2) yellow wire (may be a different color for you)
* Arduino A3 - Taranis M7 (2) green wire (may be a different color for you)

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
Write the [Star_Citizen_Controller.ino](https://github.com/Haskar/Star_Citizen_Controller/blob/713848e760347bb48a67777979dcc065e503b604/Arduino/Star_Citizen_Controller.ino) to your Arduino. Once restarted it will create 4 Joysticks with 120 buttons each (up to 4 Joysticks work "stable" on windows). With one X- and Y-Axis  on joystick 1 and one X- and Y-Axis on joystick 2, the other joysticks are only there for the additional buttons. Buttons are automatically assigned to the joysticks. Currently Star Citizen allows up to 128 buttons per joystick ... 480 should be enough for our purpose.

I had troubles inverting the roll movement in game, therefore I changed the mapping of the joystick to be inverted: 
```
yAxisJ2_ = map(yAxisJ2_,0,1023,510,0);
```
this is what it looks like when it is not inverted:
```
xAxisJ2_ = map(xAxisJ2_,0,1023,0,510);
```

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

Download  the [UAV-OSD-Sans-Mono font](https://www.dafont.com/uav-osd-sans.font) and copy it to ~/.fonts/ (create that folder if it doesn't exist)

[Disable Screen Blanking](https://github.com/raspberrypi/documentation/blob/develop/documentation/asciidoc/computers/configuration/screensaver.adoc)

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
wget https://github.com/Haskar/Star_Citizen_Controller/blob/73856a0640aa27e27cd1c83eb386a9308fdb30a8/Raspberry%20Pi/controller/controller.py
sudo chmod +x controller.py
```
then change to the image folder and copy the desired color scheme of KorneliusVonTastik icons to it. There should be just files in that folder. No subfolders. I also made some images myself using KorneliusVonTastik's images.


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
* every frame can have 4x7 buttons (that's 28)
* this is how a frame is declared:
  ```
  frame_name= tkinter.Frame(master)
  frame_name.configure(background=b_c_bg)
  ```
  The second line is optional.
  You will see that I use "frame_XXX" for my pages
  
  You will have to put it in the array of frames:
  ```
  for frame in (frame_name1, frame_name3, frame_name3)
  ```  
  You don't have to do anything else actually to add pages.
* I mainly use 4 buttons:
  Buttons used as "Joystick"-Buttons
   ```
   i_flight_movement_gear_up_icon = resize_image("flight-movement_gear-up-icon.png", i_width, i_height)
   button_name=create_button(frame_name, "", i_flight_movement_gear_up_icon, trigger, i_width, i_height)
   button_name.grid(row=1,column=2)
   trigger = trigger+1
   ```
   first line is to declare the image. I even left that in for those who still don't want to buy that coffee.
   second line is the declaration of the button. The function takes the name of the frame where the button should be, the image, a trigger-number (this will be the button number on the joystick), width and height
   third line declares the place on the page where the button should be. There are 4 rows and 7 columns available.
   fourth line is to ingrement the trigger-number. At the beginning of every page I declare the trigger a specific number. In case I f*** up in the code I would not have to assign every button again... just max. 28. first frame starts with button 30 to have a little bit of spare buttons in case I want to .. I don't know why actually.

   A variation of the buttons that function more like a switch (one for "Rear Cam ON" and one for "Rear Cam OFF") so I dont have to keep it pressed
   ```
   button_name=create_button_toggle_on(frame_name, "", i_vehicles_cockpit_lookbehind_on, trigger, i_width, i_height)
   button_name=create_button_toggle_off(frame_name, "", i_vehicles_cockpit_lookbehind_off, trigger, i_width, i_height)
   ```
   it is basically the same as the button above, just remember not to increase the toggle-counter between these two

   Buttons used to change between pages:
   ```
   i_general_ui_settings = resize_image("general-ui-settings.png", i_width, i_height)
   button_Settings=tkinter.Button(frame_name, text="", image=i_general_ui_settings, compound="center", command=lambda:raise_frame(frame_Settings), font=(b_font, b_font_size,     b_font_type), width=b_width, height=b_height, foreground=b_c_text, activeforeground=b_c_text, background=b_c_bg, activebackground=b_c_bg, border=b_b, highlightthickness=b_hl_t)
   button_Settings.grid(row=1,column=7)
   ```
   This button will switch to the "frame_Settings" page.

   And a fourth button type which does both (change frame and push a button). The Button that activates the Salvage Mode will also switch to a page with all Salvage Mode Buttons. 

* The 4x7 buttons grid will only be a 4x7 buttons grid if you have a button ... or something like a button in every cell of one column AND one row. Thats why you will find Dummy Buttons... especially on the settings-page :
   ```
   button_dummy=create_button(frame_Settings, "", i_empty, 255, i_width, i_height)
   button_dummy.grid(row=2,column=1)
   ```
* The Settings page will also let you shut off the Raspi, exit the python script and update your raspbian using
   ```
   sudo apt-get update -y && sudo apt-get upgrade -y
   ```
   Results will be shown in the texbox below the first row of buttons.

* There is also a "DISPL INFO" Button in the Main Menu. My plan is to include some 3rd party information that I need while playing. I implemented a helpfull graph of [Aaron Halo Travel Routes by CaptSheppard](https://cstone.space/resources/knowledge-base/36-refinery-to-aaron-halo-mining-routes). I had to crop and distort the image so keep it readable. If you add pictures keep in mind that, if you want to have one row on buttons, the image should be around 1020x448px (or should at least have a similar ratio)
  
