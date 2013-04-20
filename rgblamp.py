#!/usr/bin/env python

from arduino import Arduino
import time

class RGBLamp:
  def __init__(self,vDev):
    # Inicializamos modo OUTPUT en los pines que correspondan
    self.redPin = 5
    self.greenPin = 6
    self.bluePin = 9

    self.redVal = 0
    self.greenVal = 0
    self.blueVal = 0
   
    self.prevR = 0
    self.prevB = 0
    self.prevG = 0

    self.wait = 0.05
    self.hold = 0

    self.repeat = 0
    self.j = 0

    self.myArduino = Arduino(vDev)
    self.myArduino.output([self.redPin,self.greenPin,self.bluePin])
    
    print self.myArduino
  
	
  def calculateStep(self,prevValue, endValue):
    step = endValue - prevValue
    
    if (step != 0):
      step = 1020 / step			
    return step
	
  def calculateVal(self,step,val,i):
    # calcula el valor a establecer en la tira RGB
    if ((step != 0) and (i % step == 0)):
      if (step >= 0):
	val += 1
    elif (step < 0):
	val -= 1
		
    # el rango del pwm: (0,255)
    if (val > 255):
      val = 255
		
    if (val < 0):
      val = 0

    return val
       
  def crossFade(self,(r,g,b)):		
    stepR = self.calculateStep(self.prevR, r)
    stepG = self.calculateStep(self.prevG, g)
    stepB = self.calculateStep(self.prevB, b)
		
    for i in range(1020):
      self.redVal = self.calculateVal(stepR, self.redVal, i)
      self.greenVal = self.calculateVal(stepG, self.greenVal, i)
      self.blueVal = self.calculateVal(stepB, self.blueVal, i)
	
      self.myArduino.analogWrite(self.redPin, self.redVal)
      self.myArduino.analogWrite(self.greenPin, self.greenVal)
      self.myArduino.analogWrite(self.bluePin, self.blueVal)
      
    
      time.sleep(self.wait)
    
    # actualizar valores para la siguiente iteracion
    self.prevR = self.redVal
    self.prevG = self.greenVal
    self.prevB = self.blueVal

    time.sleep(self.hold)

  def setWait(input):
    # establece el tiempo de espera entre steps
    wait = input
    return 0
		
  def setHold(input):
    # establece el tiempo de espera antes de cambiar de color
    hold = input
    return 0
