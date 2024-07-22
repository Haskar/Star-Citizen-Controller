# Star_Citizen_Controller
Disclaimer: This is my first published project ever, so expect the worst and maybe you will be surprised (but I wouldn't count on it)
This is the repository of a 4-Axis Star Citizen Controller using a Raspberry pi and a Touchscreen as a Macropad

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
<img src="https://github.com/Haskar/Star_Citizen_Controller/blob/main/Screenshot%202024-07-22%20123810.png" width=150 align="left" />




