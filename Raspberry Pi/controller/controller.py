import tkinter
import sys
import serial
import time
import os
from PIL import ImageTk, Image
from subprocess import call

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "images/"
img_files_path = os.path.join(script_dir, rel_path)

arduino = serial.Serial(port='/dev/ttyS0', baudrate=115200, timeout=0.1) 

b_font = "arial"
b_font_size = 24
b_font_type = "bold"
b_width=144 #126
b_height=148
b_c_text = "#000000"
b_c_bg = "#000000"
b_b =0
b_hl_t = 0
colour_background = "#000000"
colour4 = "#AAAAAA"
colour5 = "#FFFFFF"

i_width = 126
i_height = 126

def resize_image(file, width, height):
  i_original = Image.open(os.path.join(img_files_path, file))
  i_resize = i_original.resize((width, height))
  i_finished = ImageTk.PhotoImage(i_resize)
  return i_finished

def create_button(frame, b_text, image_obj, b_event_id, image_width, image_height):
  button=tkinter.Button(frame, text=b_text, image=image_obj, compound="center", font=(b_font, b_font_size, b_font_type), width=b_width, height=b_height, foreground=b_c_text, activeforeground=b_c_text, background=b_c_bg, activebackground=b_c_bg, border=b_b, highlightthickness=b_hl_t)
  button.bind("<ButtonPress-1>", lambda event, i=str(b_event_id):  button_on_press(event, i))
  button.bind("<ButtonRelease-1>", lambda event, i=str(b_event_id*-1): button_on_release(event, i))
  return button

def button_on_press(event, i):
  arduino.write(bytes(i, 'utf-8'))
  arduino.write(bytes("x", 'utf-8'))

def button_on_release(event, i):
  arduino.write(bytes(i, 'utf-8'))
  arduino.write(bytes("x", 'utf-8'))

def close_gui():
  sys.exit()

def shutdown():
  call("sudo shutdown -h now", shell=True)

def raise_frame(frame):
  frame.tkraise()

master=tkinter.Tk()
master.title("Controller")
#master.geometry("350x275")
master.attributes('-fullscreen',True)
master.config(cursor="none")
master.configure(background=b_c_bg)

#Main
frame001= tkinter.Frame(master)
frame001.configure(background=b_c_bg)

#Salvage
frame002= tkinter.Frame(master)
frame002.configure(background=b_c_bg)

#Mine
frame003= tkinter.Frame(master)
frame003.configure(background=b_c_bg)

#Scan
frame005= tkinter.Frame(master)
frame005.configure(background=b_c_bg)

#Emotes
frame004= tkinter.Frame(master)
frame004.configure(background=b_c_bg)
frame014= tkinter.Frame(master)
frame014.configure(background=b_c_bg)

frame_Settings= tkinter.Frame(master)
frame_Settings.configure(background=b_c_bg)

for frame in (frame001, frame002, frame003, frame004, frame014, frame005, frame_Settings):
    frame.grid(row=4, column=7, sticky='news')


i_general_ui_previous = resize_image("empty.png", i_width, i_height)
i_general_ui_next = resize_image("empty.png", i_width, i_height)
i_general_ui_home = resize_image("empty.png", i_width, i_height)
i_general_ui_quit = resize_image("empty.png", i_width, i_height)
i_general_ui_shutdown = resize_image("empty.png", i_width, i_height)
i_empty = resize_image("empty.png", i_width, i_height)

i_flight_power_engine_icon = resize_image("empty.png", i_width, i_height)
i_flight_power_power_icon = resize_image("empty.png", i_width, i_height)
i_LandingGearButton = resize_image("empty.png", i_width, i_height)
i_vehicles_weapons_cycle_gimble_mode = resize_image("empty.png", i_width, i_height)

#button_dummy=create_button(frame001, "", i_empty, 255, i_width, i_height)
#button_dummy.grid(row=1,column=5)

trigger = 30
#Start Frame
#Flight System Ready
i_flight_power_flightsysready = resize_image("empty.png", i_width, i_height)
button_001_11=create_button(frame001, "", i_flight_power_flightsysready, trigger, i_width, i_height)
button_001_11.grid(row=1,column=1)
trigger = trigger+1

#Landing Request
i_flight_movement_request_landing_icon = resize_image("empty.png", i_width, i_height)
button_001_21=create_button(frame001, "", i_flight_movement_request_landing_icon, trigger, i_width, i_height)
button_001_21.grid(row=2,column=1)
trigger = trigger+1

#Gears Up
i_flight_movement_gear_up_icon = resize_image("empty.png", i_width, i_height)
button_001_12=create_button(frame001, "", i_flight_movement_gear_up_icon, trigger, i_width, i_height)
button_001_12.grid(row=1,column=2)
trigger = trigger+1

#Gears Down
i_flight_movement_gear_down_icon = resize_image("empty.png", i_width, i_height)
button_001_22=create_button(frame001, "", i_flight_movement_gear_down_icon, trigger, i_width, i_height)
button_001_22.grid(row=2,column=2)
trigger = trigger+1

#Doors Open
i_vehicles_cockpit_open_doors_icon = resize_image("empty.png", i_width, i_height)
button_001_13=create_button(frame001, "", i_vehicles_cockpit_open_doors_icon, trigger, i_width, i_height)
button_001_13.grid(row=2,column=3)
trigger = trigger+1

#Doors Closed
i_vehicles_cockpit_close_doors_icon = resize_image("empty.png", i_width, i_height)
button_001_23=create_button(frame001, "", i_vehicles_cockpit_close_doors_icon, trigger, i_width, i_height)
button_001_23.grid(row=1,column=3)
trigger = trigger+1

#Lights
i_lights_light_icon = resize_image("empty.png", i_width, i_height)
button_001_15=create_button(frame001, "", i_lights_light_icon, trigger, i_width, i_height)
button_001_15.grid(row=1,column=5)
trigger = trigger+1

#Engine Power
flight_power_engine_icon = resize_image("empty.png", i_width, i_height)
button_001_15=create_button(frame001, "", flight_power_engine_icon, trigger, i_width, i_height)
button_001_15.grid(row=1,column=4)
trigger = trigger+1

#Scan
i_vehicle_scanning_scan_icon = resize_image("empty.png", i_width, i_height)
button_001_43=create_button(frame001, "", i_vehicle_scanning_scan_icon, trigger, i_width, i_height)
button_001_43.grid(row=4,column=3)
trigger = trigger+1

#Activate SCM Mode
i_flight_movement_scm_mode_icon = resize_image("empty.png", i_width, i_height)
button_001_44=create_button(frame001, "", i_flight_movement_scm_mode_icon, trigger, i_width, i_height)
button_001_44.grid(row=4,column=4)
trigger = trigger+1

#Activate NAV Mode
i_flight_movement_nav_mode_icon = resize_image("empty.png", i_width, i_height)
button_001_45=create_button(frame001, "", i_flight_movement_nav_mode_icon, trigger, i_width, i_height)
button_001_45.grid(row=4,column=5)
trigger = trigger+1

#MAP
i_mobiglass_sky_map = resize_image("empty.png", i_width, i_height)
button_001_46=create_button(frame001, "", i_mobiglass_sky_map, trigger, i_width, i_height)
button_001_46.grid(row=4,column=6)
trigger = trigger+1

#SalvageMode
i_vehicles_seat_operator_modes_salvage_mode_icon = resize_image("empty.png", i_width, i_height)
button_001_Salvage=tkinter.Button(frame001, text="", image=i_vehicles_seat_operator_modes_salvage_mode_icon, compound="center", command=lambda:raise_frame(frame002), font=(b_font, b_font_size, b_font_type),
width=b_width, height=b_height, foreground=b_c_text, activeforeground=b_c_text, background=b_c_bg, activebackground=b_c_bg, border=b_b, highlightthickness=b_hl_t)
button_001_Salvage.bind("<ButtonPress-1>", lambda event, i=str(trigger):  button_on_press(event, i))
button_001_Salvage.bind("<ButtonRelease-1>", lambda event, i=str(trigger*-1): button_on_release(event, i))
button_001_Salvage.grid(row=3,column=1)
trigger = trigger+1

#MiningMode
i_vehicles_seat_operator_modes_mining_mode_icon = resize_image("empty.png", i_width, i_height)
button_001_Mining=tkinter.Button(frame001, text="", image=i_vehicles_seat_operator_modes_mining_mode_icon, compound="center", command=lambda:raise_frame(frame003), font=(b_font, b_font_size, b_font_type),
width=b_width, height=b_height, foreground=b_c_text, activeforeground=b_c_text, background=b_c_bg, activebackground=b_c_bg, border=b_b, highlightthickness=b_hl_t)
button_001_Mining.bind("<ButtonPress-1>", lambda event, i=str(trigger):  button_on_press(event, i))
button_001_Mining.bind("<ButtonRelease-1>", lambda event, i=str(trigger*-1): button_on_release(event, i))
button_001_Mining.grid(row=3,column=2)
trigger = trigger+1

#ScanMode
i_vehicles_seat_operator_modes_scan_mode_icon = resize_image("empty.png", i_width, i_height)
button_001_Scan=tkinter.Button(frame001, text="", image=i_vehicles_seat_operator_modes_scan_mode_icon, compound="center", command=lambda:raise_frame(frame005), font=(b_font, b_font_size, b_font_type),
width=b_width, height=b_height, foreground=b_c_text, activeforeground=b_c_text, background=b_c_bg, activebackground=b_c_bg, border=b_b, highlightthickness=b_hl_t)
button_001_Scan.bind("<ButtonPress-1>", lambda event, i=str(trigger):  button_on_press(event, i))
button_001_Scan.bind("<ButtonRelease-1>", lambda event, i=str(trigger*-1): button_on_release(event, i))
button_001_Scan.grid(row=3,column=3)
trigger = trigger+1

#Toggle Lock Doors
i_vehicles_cockpit_lock_doors_icon = resize_image("empty.png", i_width, i_height)
button_001_24=create_button(frame001, "", i_vehicles_cockpit_lock_doors_icon, trigger, i_width, i_height)
button_001_24.grid(row=2,column=4)
trigger = trigger+1

#Emote
i_general_ui_emote = resize_image("empty.png", i_width, i_height)
button_001_Mining=tkinter.Button(frame001, text="", image=i_general_ui_emote, compound="center", command=lambda:raise_frame(frame004), font=(b_font, b_font_size, b_font_type),
width=b_width, height=b_height, foreground=b_c_text, activeforeground=b_c_text, background=b_c_bg, activebackground=b_c_bg, border=b_b, highlightthickness=b_hl_t)
button_001_Mining.grid(row=4,column=7)

#Accept
i_social_general_accept = resize_image("empty.png", i_width, i_height)
button_001_41=create_button(frame001, "", i_social_general_accept, trigger, i_width, i_height)
button_001_41.grid(row=4,column=1)
trigger = trigger+1

#Decline
i_social_general_reject = resize_image("empty.png", i_width, i_height)
button_001_42=create_button(frame001, "", i_social_general_reject, trigger, i_width, i_height)
button_001_42.grid(row=4,column=2)
trigger = trigger+1

#Look Behind
i_vehicles_cockpit_lookbehind = resize_image("empty.png", i_width, i_height)
button_001_25=create_button(frame001, "", i_vehicles_cockpit_lookbehind, trigger, i_width, i_height)
button_001_25.grid(row=2,column=5)
trigger = trigger+1

#Settings Frame
i_general_ui_settings = resize_image("empty.png", i_width, i_height)
button_001_Settings=tkinter.Button(frame001, text="", image=i_general_ui_settings, compound="center", command=lambda:raise_frame(frame_Settings), font=(b_font, b_font_size, b_font_type),
width=b_width, height=b_height, foreground=b_c_text, activeforeground=b_c_text, background=b_c_bg, activebackground=b_c_bg, border=b_b, highlightthickness=b_hl_t)
button_001_Settings.grid(row=1,column=7)

#Close
button_shutdown=tkinter.Button(frame_Settings, text="", image=i_general_ui_quit, compound="center", command=shutdown, font=(b_font, b_font_size, b_font_type), 
width=b_width, height=b_height, foreground=b_c_text, activeforeground=b_c_text, background=b_c_bg, activebackground=b_c_bg, border=b_b, highlightthickness=b_hl_t)
button_shutdown.grid(row=1,column=1)

button_close=tkinter.Button(frame_Settings, text="", image=i_general_ui_shutdown, compound="center", command=close_gui, font=(b_font, b_font_size, b_font_type),
width=b_width, height=b_height, foreground=b_c_text, activeforeground=b_c_text, background=b_c_bg, activebackground=b_c_bg, border=b_b, highlightthickness=b_hl_t)
button_close.grid(row=1,column=2)

button_dummy=create_button(frame_Settings, "", i_empty, 255, i_width, i_height)
button_dummy.grid(row=2,column=1)

button_dummy=create_button(frame_Settings, "", i_empty, 255, i_width, i_height)
button_dummy.grid(row=3,column=1)

button_dummy=create_button(frame_Settings, "", i_empty, 255, i_width, i_height)
button_dummy.grid(row=4,column=1)

button_dummy=create_button(frame_Settings, "", i_empty, 255, i_width, i_height)
button_dummy.grid(row=4,column=2)

button_dummy=create_button(frame_Settings, "", i_empty, 255, i_width, i_height)
button_dummy.grid(row=4,column=3)

button_dummy=create_button(frame_Settings, "", i_empty, 255, i_width, i_height)
button_dummy.grid(row=4,column=4)

button_dummy=create_button(frame_Settings, "", i_empty, 255, i_width, i_height)
button_dummy.grid(row=4,column=5)

button_dummy=create_button(frame_Settings, "", i_empty, 255, i_width, i_height)
button_dummy.grid(row=4,column=6)

button_home=tkinter.Button(frame_Settings, text="", image=i_general_ui_home, compound="center", command=lambda:raise_frame(frame001), font=(b_font, b_font_size, b_font_type),
width=b_width, height=b_height, foreground=b_c_text, activeforeground=b_c_text, background=b_c_bg, activebackground=b_c_bg, border=b_b, highlightthickness=b_hl_t)
button_home.grid(row=4,column=7)


#Salvage Frame
trigger = 60
i_vehicles_salvage_salvage_mode_icon = resize_image("empty.png", i_width, i_height)
button_002_11=create_button(frame002, "", i_vehicles_salvage_salvage_mode_icon, trigger, i_width, i_height)
button_002_11.grid(row=1,column=1)
trigger = trigger+1

i_vehicles_salvage_tractor_beam_mode_icon = resize_image("empty.png", i_width, i_height)
button_002_12=create_button(frame002, "", i_vehicles_salvage_tractor_beam_mode_icon, trigger, i_width, i_height)
button_002_12.grid(row=1,column=2)
trigger = trigger+1

i_vehicles_salvage_cut_mode_icon = resize_image("empty.png", i_width, i_height)
button_002_15=create_button(frame002, "", i_vehicles_salvage_cut_mode_icon, trigger, i_width, i_height)
button_002_15.grid(row=1,column=5)
trigger = trigger+1

i_vehicles_salvage_fracture_mode_icon = resize_image("empty.png", i_width, i_height)
button_002_16=create_button(frame002, "", i_vehicles_salvage_fracture_mode_icon, trigger, i_width, i_height)
button_002_16.grid(row=1,column=6)
trigger = trigger+1

i_vehicles_salvage_disintegrate_mode_icon = resize_image("empty.png", i_width, i_height)
button_002_17=create_button(frame002, "", i_vehicles_salvage_disintegrate_mode_icon, trigger, i_width, i_height)
button_002_17.grid(row=1,column=7)
trigger = trigger+1

i_vehicles_salvage_increase_beam_spacing_icon = resize_image("empty.png", i_width, i_height)
button_002_21=create_button(frame002, "", i_vehicles_salvage_increase_beam_spacing_icon, trigger, i_width, i_height)
button_002_21.grid(row=2,column=1)
trigger = trigger+1

i_vehicles_salvage_toggle_fire_focused_icon = resize_image("empty.png", i_width, i_height)
button_002_22=create_button(frame002, "", i_vehicles_salvage_toggle_fire_focused_icon, trigger, i_width, i_height)
button_002_22.grid(row=2,column=2)
trigger = trigger+1

i_vehicles_salvage_toggle_fire_right_icon = resize_image("empty.png", i_width, i_height)
button_002_23=create_button(frame002, "", i_vehicles_salvage_toggle_fire_right_icon, trigger, i_width, i_height)
button_002_23.grid(row=2,column=3)
trigger = trigger+1

i_vehicles_salvage_toggle_fire_left_icon = resize_image("empty.png", i_width, i_height)
button_002_24=create_button(frame002, "", i_vehicles_salvage_toggle_fire_left_icon, trigger, i_width, i_height)
button_002_24.grid(row=2,column=4)
trigger = trigger+1

i_vehicles_salvage_toggle_fire_fracture_icon = resize_image("empty.png", i_width, i_height)
button_002_26=create_button(frame002, "", i_vehicles_salvage_toggle_fire_fracture_icon, trigger, i_width, i_height)
button_002_26.grid(row=2,column=6)
trigger = trigger+1

i_vehicles_salvage_toggle_fire_disintegrate_icon = resize_image("empty.png", i_width, i_height)
button_002_27=create_button(frame002, "", i_vehicles_salvage_toggle_fire_disintegrate_icon, trigger, i_width, i_height)
button_002_27.grid(row=2,column=7)
trigger = trigger+1

i_vehicles_salvage_decrease_beam_spacing_icon = resize_image("empty.png", i_width, i_height)
button_002_31=create_button(frame002, "", i_vehicles_salvage_decrease_beam_spacing_icon, trigger, i_width, i_height)
button_002_31.grid(row=3,column=1)
trigger = trigger+1

i_vehicles_salvage_cycle_focused_modifiers_icon = resize_image("empty.png", i_width, i_height)
button_002_32=create_button(frame002, "", i_vehicles_salvage_cycle_focused_modifiers_icon, trigger, i_width, i_height)
button_002_32.grid(row=3,column=2)
trigger = trigger+1

i_vehicles_salvage_cycle_right_modifiers_icon = resize_image("empty.png", i_width, i_height)
button_002_33=create_button(frame002, "", i_vehicles_salvage_cycle_right_modifiers_icon, trigger, i_width, i_height)
button_002_33.grid(row=3,column=3)
trigger = trigger+1

i_vehicles_salvage_cycle_left_modifiers_icon = resize_image("empty.png", i_width, i_height)
button_002_34=create_button(frame002, "", i_vehicles_salvage_cycle_left_modifiers_icon, trigger, i_width, i_height)
button_002_34.grid(row=3,column=4)
trigger = trigger+1

i_vehicles_salvage_gimball_icon = resize_image("empty.png", i_width, i_height)
button_002_41=create_button(frame002, "", i_vehicles_salvage_gimball_icon, trigger, i_width, i_height)
button_002_41.grid(row=4,column=1)
trigger = trigger+1

i_vehicles_salvage_free_gimball_icon = resize_image("empty.png", i_width, i_height)
button_002_42=create_button(frame002, "", i_vehicles_salvage_free_gimball_icon, trigger, i_width, i_height)
button_002_42.grid(row=4,column=2)
trigger = trigger+1

i_vehicles_salvage_cycle_structure_modifiers_icon = resize_image("empty.png", i_width, i_height)
button_002_43=create_button(frame002, "", i_vehicles_salvage_cycle_structure_modifiers_icon, trigger, i_width, i_height)
button_002_43.grid(row=4,column=3)
trigger = trigger+1

i_vehicles_salvage_focus_icon = resize_image("empty.png", i_width, i_height)
button_002_44=create_button(frame002, "", i_vehicles_salvage_focus_icon, trigger, i_width, i_height)
button_002_44.grid(row=4,column=4)
trigger = trigger+1

i_vehicles_salvage_salvage_beam_axis_toggle_icon = resize_image("empty.png", i_width, i_height)
button_002_45=create_button(frame002, "", i_vehicles_salvage_salvage_beam_axis_toggle_icon, trigger, i_width, i_height)
button_002_45.grid(row=4,column=5)
trigger = trigger+1

button_002_home=tkinter.Button(frame002, text="", image=i_general_ui_home, compound="center", command=lambda:raise_frame(frame001), font=(b_font, b_font_size, b_font_type),
width=b_width, height=b_height, foreground=b_c_text, activeforeground=b_c_text, background=b_c_bg, activebackground=b_c_bg, border=b_b, highlightthickness=b_hl_t)
button_002_home.grid(row=4,column=7)

#Mining Frame
trigger = 90
i_vehicle_mining_laser_fire_icon = resize_image("empty.png", i_width, i_height)
button_003_11=create_button(frame003, "", i_vehicle_mining_laser_fire_icon, trigger, i_width, i_height)
button_003_11.grid(row=1,column=1)
trigger = trigger+1

i_vehicle_mining_switch_laser_type_icon = resize_image("empty.png", i_width, i_height)
button_003_12=create_button(frame003, "", i_vehicle_mining_switch_laser_type_icon, trigger, i_width, i_height)
button_003_12.grid(row=1,column=2)
trigger = trigger+1

i_vehicle_mining_jettison_cargo_icon = resize_image("empty.png", i_width, i_height)
button_003_17=create_button(frame003, "", i_vehicle_mining_jettison_cargo_icon, trigger, i_width, i_height)
button_003_17.grid(row=1,column=7)
trigger = trigger+1

i_vehicle_mining_increase_icon = resize_image("empty.png", i_width, i_height)
button_003_21=create_button(frame003, "", i_vehicle_mining_increase_icon, trigger, i_width, i_height)
button_003_21.grid(row=2,column=1)
trigger = trigger+1

i_vehicle_mining_decrease_icon = resize_image("empty.png", i_width, i_height)
button_003_31=create_button(frame003, "", i_vehicle_mining_decrease_icon, trigger, i_width, i_height)
button_003_31.grid(row=3,column=1)
trigger = trigger+1

i_vehicle_mining_module01_text = resize_image("vehicle-mining_module01empty.png", i_width, i_height)
button_003_31=create_button(frame003, "", i_vehicle_mining_module01_text, trigger, i_width, i_height)
button_003_31.grid(row=4,column=1)
trigger = trigger+1

i_vehicle_mining_module02_text = resize_image("vehicle-mining_module02empty.png", i_width, i_height)
button_003_32=create_button(frame003, "", i_vehicle_mining_module02_text, trigger, i_width, i_height)
button_003_32.grid(row=4,column=2)
trigger = trigger+1

i_vehicle_mining_module03_text = resize_image("vehicle-mining_module03empty.png", i_width, i_height)
button_003_33=create_button(frame003, "", i_vehicle_mining_module03_text, trigger, i_width, i_height)
button_003_33.grid(row=4,column=3)
trigger = trigger+1

button_dummy=create_button(frame003, "", i_empty, 255, i_width, i_height)
button_dummy.grid(row=4,column=4)

button_dummy=create_button(frame003, "", i_empty, 255, i_width, i_height)
button_dummy.grid(row=4,column=5)

button_dummy=create_button(frame003, "", i_empty, 255, i_width, i_height)
button_dummy.grid(row=4,column=6)

button_003_home=tkinter.Button(frame003, text="", image=i_general_ui_home, compound="center", command=lambda:raise_frame(frame001), font=(b_font, b_font_size, b_font_type),
width=b_width, height=b_height, foreground=b_c_text, activeforeground=b_c_text, background=b_c_bg, activebackground=b_c_bg, border=b_b, highlightthickness=b_hl_t)
button_003_home.grid(row=4,column=7)

#Scan Frame
trigger = 120
vehicle_scanning_scan_icon = resize_image("empty.png", i_width, i_height)
button_005_11=create_button(frame005, "", vehicle_scanning_scan_icon, trigger, i_width, i_height)
button_005_11.grid(row=1,column=1)
trigger = trigger+1

vehicle_scanning_decrease_scan_angle_icon = resize_image("empty.png", i_width, i_height)
button_005_22=create_button(frame005, "", vehicle_scanning_decrease_scan_angle_icon, trigger, i_width, i_height)
button_005_22.grid(row=2,column=1)
trigger = trigger+1

vehicle_scanning_increase_scan_angle_icon = resize_image("empty.png", i_width, i_height)
button_005_21=create_button(frame005, "", vehicle_scanning_increase_scan_angle_icon, trigger, i_width, i_height)
button_005_21.grid(row=2,column=2)
trigger = trigger+1

button_dummy=create_button(frame005, "", i_empty, 255, i_width, i_height)
button_dummy.grid(row=3,column=1)

button_dummy=create_button(frame005, "", i_empty, 255, i_width, i_height)
button_dummy.grid(row=4,column=1)

button_dummy=create_button(frame005, "", i_empty, 255, i_width, i_height)
button_dummy.grid(row=4,column=2)

button_dummy=create_button(frame005, "", i_empty, 255, i_width, i_height)
button_dummy.grid(row=4,column=3)

button_dummy=create_button(frame005, "", i_empty, 255, i_width, i_height)
button_dummy.grid(row=4,column=4)

button_dummy=create_button(frame005, "", i_empty, 255, i_width, i_height)
button_dummy.grid(row=4,column=5)

button_dummy=create_button(frame005, "", i_empty, 255, i_width, i_height)
button_dummy.grid(row=4,column=6)

button_005_home=tkinter.Button(frame005, text="", image=i_general_ui_home, compound="center", command=lambda:raise_frame(frame001), font=(b_font, b_font_size, b_font_type),
width=b_width, height=b_height, foreground=b_c_text, activeforeground=b_c_text, background=b_c_bg, activebackground=b_c_bg, border=b_b, highlightthickness=b_hl_t)
button_005_home.grid(row=4,column=7)


#Emote Frame1
trigger = 400
i_social_emote_agree_icon = resize_image("empty.png", i_width, i_height)
button_004_11=create_button(frame004, "", i_social_emote_agree_icon, trigger, i_width, i_height)
button_004_11.grid(row=1,column=1)
trigger = trigger+1

i_social_emote_angry_icon = resize_image("empty.png", i_width, i_height)
button_004_12=create_button(frame004, "", i_social_emote_angry_icon, trigger, i_width, i_height)
button_004_12.grid(row=1,column=2)
trigger = trigger+1

i_social_emote_at_ease_icon = resize_image("empty.png", i_width, i_height)
button_004_13=create_button(frame004, "", i_social_emote_at_ease_icon, trigger, i_width, i_height)
button_004_13.grid(row=1,column=3)
trigger = trigger+1

i_social_emote_attention_icon = resize_image("empty.png", i_width, i_height)
button_004_14=create_button(frame004, "", i_social_emote_attention_icon, trigger, i_width, i_height)
button_004_14.grid(row=1,column=4)
trigger = trigger+1

i_social_emote_blah_icon = resize_image("empty.png", i_width, i_height)
button_004_15=create_button(frame004, "", i_social_emote_blah_icon, trigger, i_width, i_height)
button_004_15.grid(row=1,column=5)
trigger = trigger+1

i_social_emote_bored_icon = resize_image("empty.png", i_width, i_height)
button_004_16=create_button(frame004, "", i_social_emote_bored_icon, trigger, i_width, i_height)
button_004_16.grid(row=1,column=6)
trigger = trigger+1

i_social_emote_bow_icon = resize_image("empty.png", i_width, i_height)
button_004_17=create_button(frame004, "", i_social_emote_bow_icon, trigger, i_width, i_height)
button_004_17.grid(row=1,column=7)
trigger = trigger+1

i_social_emote_burp_icon = resize_image("empty.png", i_width, i_height)
button_004_21=create_button(frame004, "", i_social_emote_burp_icon, trigger, i_width, i_height)
button_004_21.grid(row=2,column=1)
trigger = trigger+1

i_social_emote_cheer_icon = resize_image("empty.png", i_width, i_height)
button_004_22=create_button(frame004, "", i_social_emote_cheer_icon, trigger, i_width, i_height)
button_004_22.grid(row=2,column=2)
trigger = trigger+1

i_social_emote_chicken_icon = resize_image("empty.png", i_width, i_height)
button_004_23=create_button(frame004, "", i_social_emote_chicken_icon, trigger, i_width, i_height)
button_004_23.grid(row=2,column=3)
trigger = trigger+1

i_social_emote_clap_icon = resize_image("empty.png", i_width, i_height)
button_004_24=create_button(frame004, "", i_social_emote_clap_icon, trigger, i_width, i_height)
button_004_24.grid(row=2,column=4)
trigger = trigger+1

i_social_emote_come_icon = resize_image("empty.png", i_width, i_height)
button_004_25=create_button(frame004, "", i_social_emote_come_icon, trigger, i_width, i_height)
button_004_25.grid(row=2,column=5)
trigger = trigger+1

i_social_emote_cry_icon = resize_image("empty.png", i_width, i_height)
button_004_26=create_button(frame004, "", i_social_emote_cry_icon, trigger, i_width, i_height)
button_004_26.grid(row=2,column=6)
trigger = trigger+1

i_social_emote_dance_icon = resize_image("empty.png", i_width, i_height)
button_004_27=create_button(frame004, "", i_social_emote_dance_icon, trigger, i_width, i_height)
button_004_27.grid(row=2,column=7)
trigger = trigger+1

i_social_emote_disagree_icon = resize_image("empty.png", i_width, i_height)
button_004_31=create_button(frame004, "", i_social_emote_disagree_icon, trigger, i_width, i_height)
button_004_31.grid(row=3,column=1)
trigger = trigger+1

i_social_emote_failure_icon = resize_image("empty.png", i_width, i_height)
button_004_32=create_button(frame004, "", i_social_emote_failure_icon, trigger, i_width, i_height)
button_004_32.grid(row=3,column=2)
trigger = trigger+1

i_social_emote_flex_icon = resize_image("empty.png", i_width, i_height)
button_004_33=create_button(frame004, "", i_social_emote_flex_icon, trigger, i_width, i_height)
button_004_33.grid(row=3,column=3)
trigger = trigger+1

i_social_emote_flirt_icon = resize_image("empty.png", i_width, i_height)
button_004_34=create_button(frame004, "", i_social_emote_flirt_icon, trigger, i_width, i_height)
button_004_34.grid(row=3,column=4)
trigger = trigger+1

i_social_emote_gasp_icon = resize_image("empty.png", i_width, i_height)
button_004_35=create_button(frame004, "", i_social_emote_gasp_icon, trigger, i_width, i_height)
button_004_35.grid(row=3,column=5)
trigger = trigger+1

i_social_emote_gloat_icon = resize_image("empty.png", i_width, i_height)
button_004_36=create_button(frame004, "", i_social_emote_gloat_icon, trigger, i_width, i_height)
button_004_36.grid(row=3,column=6)
trigger = trigger+1

i_social_emote_greet_icon = resize_image("empty.png", i_width, i_height)
button_004_37=create_button(frame004, "", i_social_emote_greet_icon, trigger, i_width, i_height)
button_004_37.grid(row=3,column=7)
trigger = trigger+1

i_social_emote_laugh_icon = resize_image("empty.png", i_width, i_height)
button_004_41=create_button(frame004, "", i_social_emote_laugh_icon, trigger, i_width, i_height)
button_004_41.grid(row=4,column=1)
trigger = trigger+1

i_social_emote_launch_icon = resize_image("empty.png", i_width, i_height)
button_004_42=create_button(frame004, "", i_social_emote_launch_icon, trigger, i_width, i_height)
button_004_42.grid(row=4,column=2)
trigger = trigger+1

i_social_emote_no_icon = resize_image("empty.png", i_width, i_height)
button_004_43=create_button(frame004, "", i_social_emote_no_icon, trigger, i_width, i_height)
button_004_43.grid(row=4,column=3)
trigger = trigger+1

i_social_emote_point_icon = resize_image("empty.png", i_width, i_height)
button_004_44=create_button(frame004, "", i_social_emote_point_icon, trigger, i_width, i_height)
button_004_44.grid(row=4,column=4)
trigger = trigger+1

i_social_emote_rude_icon = resize_image("empty.png", i_width, i_height)
button_004_45=create_button(frame004, "", i_social_emote_rude_icon, trigger, i_width, i_height)
button_004_45.grid(row=4,column=5)
trigger = trigger+1

button_004_frame014=tkinter.Button(frame004, text="", image=i_general_ui_next, compound="center", command=lambda:raise_frame(frame014), font=(b_font, b_font_size, b_font_type),
width=b_width, height=b_height, foreground=b_c_text, activeforeground=b_c_text, background=b_c_bg, activebackground=b_c_bg, border=b_b, highlightthickness=b_hl_t)
button_004_frame014.grid(row=4,column=6)

button_004_home=tkinter.Button(frame004, text="", image=i_general_ui_home, compound="center", command=lambda:raise_frame(frame001), font=(b_font, b_font_size, b_font_type),
width=b_width, height=b_height, foreground=b_c_text, activeforeground=b_c_text, background=b_c_bg, activebackground=b_c_bg, border=b_b, highlightthickness=b_hl_t)
button_004_home.grid(row=4,column=7)

#Emote Frame2
i_social_emote_salut_icon = resize_image("empty.png", i_width, i_height)
button_014_11=create_button(frame014, "", i_social_emote_salut_icon, trigger, i_width, i_height)
button_014_11.grid(row=1,column=1)
trigger = trigger+1

i_social_emote_sit_icon = resize_image("empty.png", i_width, i_height)
button_014_12=create_button(frame014, "", i_social_emote_sit_icon, trigger, i_width, i_height)
button_014_12.grid(row=1,column=2)
trigger = trigger+1

i_social_emote_sleep_icon = resize_image("empty.png", i_width, i_height)
button_014_13=create_button(frame014, "", i_social_emote_sleep_icon, trigger, i_width, i_height)
button_014_13.grid(row=1,column=3)
trigger = trigger+1

i_social_emote_smell_icon = resize_image("empty.png", i_width, i_height)
button_014_14=create_button(frame014, "", i_social_emote_smell_icon, trigger, i_width, i_height)
button_014_14.grid(row=1,column=4)
trigger = trigger+1

i_social_emote_taunt_icon = resize_image("empty.png", i_width, i_height)
button_014_15=create_button(frame014, "", i_social_emote_taunt_icon, trigger, i_width, i_height)
button_014_15.grid(row=1,column=5)
trigger = trigger+1

i_social_emote_threaten_icon = resize_image("empty.png", i_width, i_height)
button_014_16=create_button(frame014, "", i_social_emote_threaten_icon, trigger, i_width, i_height)
button_014_16.grid(row=1,column=6)
trigger = trigger+1

i_social_emote_wait_icon = resize_image("empty.png", i_width, i_height)
button_014_17=create_button(frame014, "", i_social_emote_wait_icon, trigger, i_width, i_height)
button_014_17.grid(row=1,column=7)
trigger = trigger+1

i_social_emote_wave_icon = resize_image("empty.png", i_width, i_height)
button_014_21=create_button(frame014, "", i_social_emote_wave_icon, trigger, i_width, i_height)
button_014_21.grid(row=2,column=1)
trigger = trigger+1

i_social_emote_whistle_icon = resize_image("empty.png", i_width, i_height)
button_014_22=create_button(frame014, "", i_social_emote_whistle_icon, trigger, i_width, i_height)
button_014_22.grid(row=2,column=2)
trigger = trigger+1

i_social_emote_yes_icon = resize_image("empty.png", i_width, i_height)
button_014_23=create_button(frame014, "", i_social_emote_yes_icon, trigger, i_width, i_height)
button_014_23.grid(row=2,column=3)
trigger = trigger+1

button_dummy=create_button(frame014, "", i_empty, 255, i_width, i_height)
button_dummy.grid(row=3,column=1)

button_014_frame004=tkinter.Button(frame014, text="", image=i_general_ui_previous, compound="center", command=lambda:raise_frame(frame004), font=(b_font, b_font_size, b_font_type),
width=b_width, height=b_height, foreground=b_c_text, activeforeground=b_c_text, background=b_c_bg, activebackground=b_c_bg, border=b_b, highlightthickness=b_hl_t)
button_014_frame004.grid(row=4,column=6)

button_014_home=tkinter.Button(frame014, text="", image=i_general_ui_home, compound="center", command=lambda:raise_frame(frame001), font=(b_font, b_font_size, b_font_type),
width=b_width, height=b_height, foreground=b_c_text, activeforeground=b_c_text, background=b_c_bg, activebackground=b_c_bg, border=b_b, highlightthickness=b_hl_t)
button_014_home.grid(row=4,column=7)

##################################################################

#i_EnginesButton_original = Image.open("empty.png")
#i_EnginesButton_resize = i_EnginesButton_original.resize((i_width, i_height))
#i_EnginesButton = ImageTk.PhotoImage(i_EnginesButton_resize)


#button_008=tkinter.Button(master, text="", image=i_QT, compound="center", font=(b_font, b_font_size, b_font_type), width=b_width, height=b_height, foreground=b_c_text, activeforeground=b_c_text, background=b_c_bg, activebackground=b_c_bg, border=b_b, highlightthickness=b_hl_t)
#button_008.grid(row=1,column=8)
#button_008.bind("<ButtonPress-1>", lambda event, i="7":  button_on_press(event, i))
#button_008.bind("<ButtonRelease-1>", lambda event, i="-7": button_on_release(event, i))

raise_frame(frame001)

master.mainloop()