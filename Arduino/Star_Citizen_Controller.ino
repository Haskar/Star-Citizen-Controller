#include <Joystick.h>

#define JOY1X A2
#define JOY1Y A3
#define JOY2X A1
#define JOY2Y A0
#define JOYSTICK_COUNT 4
#define MAX_BUTTONS 120
#define PRIM_JOYSTICK 0
#define SEC_JOYSTICK 1
//Defining the Joystick
//The Joystick is defined in the following setup:
//Joystick(Joystick HID ID, Joystick Type, Button Count, Hat Switch Count, Include X, Include Y, Include Z, Include Rx, Include Ry, Include Rz, Include Rudder, Include Throttle, Include Accelerator, Include Brake, Include Steering
//Joystick HID ID: A Hex value identifier for HID Device Recognition (default: 0x03). DO NOT USE 0x01 or 0x02
//Joystick type: Define the type of joystick from the types supported. Types: DEFAULT Joystick (0x04 or JOYSTICK_TYPE_JOYSTICK), Gamepad (0x05 or JOYSTICK_TYPE_GAMEPAD), Multi-Axis Controller (0x08 or JOYSTICK_TYPE_MULTI_AXIS)
//Button Count: Number of Buttons shown to HID system (default: 32)
//Hat Switch Count: Number of Hat Switches, max 2. (default:2)
//Include X Axis: Determines whether the X axis is avalible for used by the HID system, defined as a bool value (default:true)
//Include Y Axis: Determines whether the Y axis is avalible for used by the HID system, defined as a bool value (default:true)
//Include Z Axis: Determines whether the Z axis is avalible for used by the HID system, defined as a bool value (default:true)
//Include Rx Axis: Determines whether the X Rotational axis is avalible for used by the HID system, defined as a bool value (default:true)
//Include Ry Axis: Determines whether the Y Rotational axis is avalible for used by the HID system, defined as a bool value (default:true)
//Include Rz Axis: Determines whether the Z Rotational axis is avalible for used by the HID system, defined as a bool value (default:true)
//Include Rudder: Determines whether a Rudder axis is avalible for used by the HID system, defined as a bool value (default:true)
//Include Throttle: Determines whether a Throttle axis is avalible for used by the HID system, defined as a bool value (default:true)
//Include Accelerator: Determines whether an Accelerator axis is avalible for used by the HID system, defined as a bool value (default:true)
//Include Brake: Determines whether a Brake axis is avalible for used by the HID system, defined as a bool value (default:true)
//Include Steering: Determines whether a Steering axis is avalible for used by the HID system, defined as a bool value (default:true)

Joystick_ Joystick[JOYSTICK_COUNT] = {
  Joystick_(0x11, JOYSTICK_TYPE_JOYSTICK, MAX_BUTTONS, 0, true, true, false, false, false, false, false, false, false, false, false),
  Joystick_(0x12, JOYSTICK_TYPE_JOYSTICK, MAX_BUTTONS, 0, true, true, false, false, false, false, false, false, false, false, false),
  Joystick_(0x13, JOYSTICK_TYPE_JOYSTICK, MAX_BUTTONS, 0, false, false, false, false, false, false, false, false, false, false, false),
  Joystick_(0x14, JOYSTICK_TYPE_JOYSTICK, MAX_BUTTONS, 0, false, false, false, false, false, false, false, false, false, false, false)
};

const bool initAutoSendState = true;

int xAxisJ1_ = 0;
int yAxisJ1_ = 0;
int xAxisJ2_ = 0;
int yAxisJ2_ = 0;
int index = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial1.begin(115200);
  
  for (int index = 0; index < JOYSTICK_COUNT; index++)
  {
    delay(100);
    if (initAutoSendState)
    {
      Joystick[index].begin();
      for (int button_index = 0; button_index < MAX_BUTTONS; button_index++)
      { 
        Joystick[index].setButton(button_index, 0);
      }
    }
    else
    {
      Joystick[index].begin(false);
    }
  }

  //Joystick.begin();
}

void loop() {

  // put your main code here, to run repeatedly:
  xAxisJ1_ = analogRead(JOY1X);
  xAxisJ1_ = map(xAxisJ1_,0,1023,510,0);
  Joystick[PRIM_JOYSTICK].setXAxis(xAxisJ1_);

  yAxisJ1_ = analogRead(JOY1Y);
  yAxisJ1_ = map(yAxisJ1_,0,1023,510,0);
  Joystick[PRIM_JOYSTICK].setYAxis(yAxisJ1_);

  xAxisJ2_ = analogRead(JOY2X);
  xAxisJ2_ = map(xAxisJ2_,0,1023,0,510);
  Joystick[SEC_JOYSTICK].setYAxis(xAxisJ2_);

  yAxisJ2_ = analogRead(JOY2Y);
  yAxisJ2_ = map(yAxisJ2_,0,1023,510,0);
  Joystick[SEC_JOYSTICK].setXAxis(yAxisJ2_);
  
  
 
  if (Serial1.available()) // Check to see if at least one character is available
  {
    int integerValue = Serial1.parseInt();
    int joystick_number = 0;
    while (abs(integerValue)>MAX_BUTTONS)
    {
      joystick_number = joystick_number+1;
      if (integerValue > 0)
      {
        integerValue = integerValue-MAX_BUTTONS;
      }
      if (integerValue < 0)
      {
        integerValue = integerValue+MAX_BUTTONS;
      }
    }

    if (integerValue > 0)
    {
      Joystick[joystick_number].setButton(integerValue-1, 1);
    }
    if (integerValue < 0)
    {
      Joystick[joystick_number].setButton((integerValue*-1)-1, 0);
    }
    Serial.print(integerValue);
    Serial.print(" - ");
    Serial.println(joystick_number);
  }
}

