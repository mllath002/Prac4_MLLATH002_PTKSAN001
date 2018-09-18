#!/usr/bin/python

import RPi.GPIO as GPIO
import Adafruit_MCP3008
import os
import time

#use BCM pin number and define pins
GPIO.setmode(GPIO.BCM)
freq_btn = 20
reset_btn = 21
stop_btn = 16
display_btn = 6

#set all pins to input mode and set to pull up mode
GPIO.setup(freq_btn,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(reset_btn,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(stop_btn,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(display_btn,GPIO.IN,pull_up_down = GPIO.PUD_UP)

#define SPI pins
SPICS = 8
SPIMISO = 9
SPIMOSI =10
SPICLK =11

#set modes for SPI pins
GPIO.setup(SPICS, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPICLK, GPIO.OUT)

mcp = Adafruit_MCP3008.MCP3008(clk = SPICLK, cs =SPICS, mosi = SPIMOSI, miso = SPIMISO)

#interrupts
GPIO.add_event_detect(freq_btn,GPIO.FALLING, callback=freq_callback,bouncetime=200)
GPIO.add_event_detect(reset_btn,GPIO.FALLING, callback=clear_callback,bouncetime=200)
GPIO.add_event_detect(stop_btn,GPIO.FALLING, callback=stop_callback,bouncetime=200)
GPIO.add_event_detect(display_btn,GPIO.FALLING, callback=disp_callback,bouncetime=200)

# variables 
delay = 0.5 #frequency delay 
stop = False #stop button 
display = [0]*5
reset = 0 #reset button 
number = 0

# FUNCTION DEFINITION: CLEAR  
def clear_callback(channel)
    # clear console and reset time
    empty = os.system('clear')
    global reset
    reset = 0 
    print("Time|t|tTimer|tPot|tTemp|tLight")
    
    
# FUNCTION DEFINITION: CHANGE FREQUENCY 
def freq_callback(channel)
    global delay
    if (delay == 0.5): 
        delay = 1
    elif (delay == 1):
        delay = 2 
    else: 
        delay = 0.5

# FUNCTION DEEFINITION: Stop 
def stop_callback(channel):
    global stop
    global count
    if(stop==False):
        count =0
        stop = True
    else:
        stop = False
        
 # FUNCTION DEFINITION: Display
def disp_callback(channel):
    global display
    print("------------------------------------------------")
    print("Time|t|tTimer|tPot|tTemp|tLight")
    for i in range(5):
        print(display[i])
    print("------------------------------------------------")
    
=======
#FUNCTION DEFINITION: convert data to voltage
def Volt_Convert(voltage): 
    voltage_read = (voltage*3.3)/1023
    voltage_read = round (voltage_read, 1) # round to 1 decimal place
    return voltage_read 


#FUNCTION DEFINITION: convert data to temperature in celsius 
def Temp_Convert(temp): 
    voltage = (temp*3.3)/1023 
    temperature_read = (voltage-0.5)*100
    temperature_read = int (round (temp, 0)) 
    return temperature_read

#FUNCTION DEFINITION: converting light data to percentage
def Light_Convert(light_val):
    light = (light_val/1023)*100
    light = 100 - light
    light = int(round(light)) #round off number and convert type to int
    return light

vals = [0] * 8
print("Time|t|tTimer|tPot|tTemp|tLight")
timer = time.time()

while True:
    for i in range(8):
        values[i]=mcp.read_adc(i) #read in data from adc
    time.sleep(delay)
    voltage = vals[2] # read data from channel 2
    temperature = vals[1] #read data from channel 1
    light_val = vals[6] #read data from channel 6
    
    #convert values to display values
    light_up = Light_Convert(light_val)
    temp_t = Temp_Convert(temperature)
    pot_volt = Volt_Convert(voltage)
    
    tim = time.strftime("%X") #formatting directive for time
    currentTime = time.time()
    timeDifference = round((currentTime - timer),1) #record time passed
    timer = currentTime #reset reference time
    reset = round((reset + timeDifference),2)
   
GPIO.cleanup()



