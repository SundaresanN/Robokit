
try:
  import usocket as socket
except:
  import socket

import network

import uRover as Motor

def Start_Bot():
  #initializes Socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind(('', 80))
  s.listen(2)
  
  #object for stepper class
  M = Motor.Stepper()

  while True:
    #connection established
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    
    #receives requests
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    
    #parse request to identify command
    forward = request.find('/forward')
    backward = request.find('/backward')
    left = request.find('/left')
    right = request.find('/right')
    stop = request.find('/stop')
  
    #controls bot based on request
    if forward != -1:
      M.Move_Forward()
    
    elif backward != -1:
      M.Move_Backward()
    
    elif left != -1:
      M.Turn_Left()
    
    elif right != -1:
      M.Turn_Right()
    
    elif stop != -1:
      M.STOP()
    
    #connection closed
    conn.close()


