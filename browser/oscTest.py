"""OSC Test Script
Written by Aaron Chamberlain Dec. 2013
The purpose of this script is to make a very simple communication structure to the popular 
application touchOSC. This is achieved through the pyOSC library. However, since the pyOSC 
documentation is scarce and only one large example is included, I am going to strip down 
the basic structures of that file to implement a very simple bi-directional communication.
"""

#!/usr/bin/env python

import socket, OSC, re, time, threading, math

receive_address = '127.0.0.1', 7000 #Mac Adress, Outgoing Port
send_address = '127.0.0.1',7110 #iPhone Adress, Incoming Port

class PiException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

##########################
#	OSC
##########################

# Initialize the OSC server and the client.
s = OSC.OSCServer(receive_address)
c = OSC.OSCClient()
c.connect(send_address)

s.addDefaultHandlers()

# define a message-handler function for the server to call.
def test_handler(addr, tags, stuff, source):
	print "---"
	print "received new osc msg from %s" % OSC.getUrlStr(source)
	print "with addr : %s" % addr
	print "typetags %s" % tags
	print "data %s" % stuff
	msg = OSC.OSCMessage()
	msg.setAddress(addr)
	msg.append(stuff)
	c.send(msg)
	print "return message %s" % msg
	print "---"

def moveStop_handler(add, tags, stuff, source):
	addMove(0,0)

def moveJoystick_handler(add, tags, stuff, source):
	print "message received:"
	msg = OSC.OSCMessage()
	msg.setAddress(addr)
	msg.append(stuff)
	c.send(msg)
	print "X Value is: " 
	print stuff[0] 
	print "Y Value is: " 
	print stuff[1]  #stuff is a 'list' variable

def user3_handler(add, tags, stuff, source):
	print "user 3 was sent"
def user4_handler(add, tags, stuff, source):
	print "user 4 was sent"
# adding my functions
s.addMsgHandler("/user/1", moveStop_handler)
s.addMsgHandler("/user/2", moveJoystick_handler)

s.addMsgHandler("/user/3", user3_handler)

s.addMsgHandler("/user/4", user4_handler)

# just checking which handlers we have added
print "Registered Callback-functions are :"
for addr in s.getOSCAddressSpace():
	print addr

# Start OSCServer
print "\nStarting OSCServer. Use ctrl-C to quit."
st = threading.Thread( target = s.serve_forever )
st.start()

def sendMessage():
	msg = OSC.OSCMessage()
	msg.setAddress(addr)
	msg.append('ok')
	c.send(msg)
	print "sending message"
# Loop while threads are running.
try :
	while 1 :
		sendMessage()
		time.sleep(10)
 
except KeyboardInterrupt :
	print "\nClosing OSCServer."
	s.close()
	print "Waiting for Server-thread to finish"
	st.join()
print "Done"