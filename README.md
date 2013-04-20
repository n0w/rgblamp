Written by n0w
20 April 2013

v1

Python class to smoothly fade between colours using RGB Strip via arduino.
Using arduino lib from https://github.com/vascop/Python-Arduino-Proto-API-v2

(schematics: not yet available)

Usage:

import rgblamp.py

lamp1 = rgblamp.RGBLamp("/dev/ttyACM0")
lamp1.crossFade((255,0,0))

- RGBLamp object intializes with the path to arduino virtual dev.
- crossFade method receives one value for each colour: (red, green, blue). Then it fades smoothly from the (initially set to black by default) previous colour.

In further versions it will be possible to set certains values to manipulate fade in and colour hold times.
