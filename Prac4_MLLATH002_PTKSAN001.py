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



