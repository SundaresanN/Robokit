

from machine import Pin

class Stepper:
 "Class defining Motor functions"
 #class initializer
 def __init__(self):
    #LEFT Motor
   self.motorA_front =Pin(2,Pin.OUT)
   self.motorA_back = Pin(0,Pin.OUT)
    #RIGHT Motor
   self.motorB_front =Pin(4,Pin.OUT)
   self.motorB_back = Pin(5,Pin.OUT)

 def Move_Forward(self):
   self.motorA_front.value(1)
   self.motorA_back.value(0)
   self.motorB_front.value(1)
   self.motorB_back.value(0)
   print("Forward")
 
 def Move_Backward(self):
   self.motorA_front.value(0)
   self.motorA_back.value(1)
   self.motorB_front.value(0)
   self.motorB_back.value(1)
   print("Backward")

 def Turn_Left(self):
   self.motorA_front.value(0)
   self.motorA_back.value(0)
   self.motorB_front.value(1)
   self.motorB_back.value(0)
   print("Left")
 
 def Turn_Right(self):
   self.motorA_front.value(1)
   self.motorA_back.value(0)
   self.motorB_front.value(0)
   self.motorB_back.value(0)
   print("Right")
  
 def STOP(self):
   self.motorA_front.value(0)
   self.motorA_back.value(0)
   self.motorB_front.value(0)
   self.motorB_back.value(0)
   print("Stop")


