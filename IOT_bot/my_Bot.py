

import Motor

import AdafruitSubscribe as cloud

def Start_Bot(): 
  
  M = Motor.Stepper()

  while True:
    #Getting the command from Adafruit IO
    command = cloud.getCommand()
    command = command.lower()
    
    if command == "forward":
      M.Move_Forward()
    
    elif command == "backward":
      M.Move_Backward()
    
    elif command == "left":
      M.Turn_Left()
    
    elif command == "right":
      M.Turn_Right()
    
    elif command == "stop":
      M.STOP()
    else:
      print('No Match') 







