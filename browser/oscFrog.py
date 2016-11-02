"""OSC Test Script
Written by Aaron Chamberlain Dec. 2013
The purpose of this script is to make a very simple communication structure to the popular 
application touchOSC. This is achieved through the pyOSC library. However, since the pyOSC 
documentation is scarce and only one large example is included, I am going to strip down 
the basic structures of that file to implement a very simple bi-directional communication.
"""

#!/usr/bin/env python

import socket, OSC, re, time, threading, math
import pyshark
import json
import math
import random
import platform

receive_address = '127.0.0.1', 7000 #Mac Adress, Outgoing Port
send_address = '127.0.0.1',7110 #iPhone Adress, Incoming Port

interface=""
if platform.system()=="linux":
    interface="wlo1"
elif platform.system()=="Darwin":
    interface="en2"
elif platform.system()=="Windows":
    interface="Wi-Fi"

#cap = pyshark.LiveCapture(interface)
counter=0;

frog_string=""
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

def sendMessage(address,message):
	msg = OSC.OSCMessage()
	msg.setAddress(address)
	msg.append(message)
	c.send(msg)
	print address

# adding my functions
s.addMsgHandler("/user/1", moveStop_handler)
s.addMsgHandler("/user/2", moveJoystick_handler)

s.addMsgHandler("/user/3", user3_handler)


# just checking which handlers we have added
print "Registered Callback-functions are :"
for addr in s.getOSCAddressSpace():
	print addr

def capture_frogs():
    global interface
    cap = pyshark.LiveCapture(interface)
    cap.sniff(timeout=2)
    dir(cap)
    for pkt in cap:
        all_layers=pkt.layers
        for layer in all_layers:
            layer_name=layer._layer_name
            if "radiotap" in layer_name:
                #print "radiotap"
                if layer.channel_flags_5ghz == '1':
                    #print "on 5ghz"
                    chan='5'
                else:
                    #print "on 2ghz"
                    chan='2'
                sendMessage("Frog/radiotap", chan)
            elif "wlan_radio" in layer_name:
                if 'signal_dbm' in dir(layer):
                    sig_strength=layer.signal_dbm
                    sendMessage("Frog/wlan_radio",sig_strength)
                    #print sig_strength
                
            elif "wlan" in layer_name:
                #print "wlan"
                if 'ta' in dir(layer):
                    trans_addr=layer.ta
                    #sendMessage("Frog/wlan_addr/trans",trans_addr)
                if 'ra' in dir(layer):
                    rec_addr=layer.ra
                    #sendMessage("Frog/wlan_addr/rec",rec_addr)
                sendMessage("Frog/wlan_addr",trans_addr + "," + rec_addr)
            elif "http" in layer.layer_name:
                print layer
                print dir(layer)
                if 'content_encoding' in dir(layer):
                    content_encoding=layer.content_encoding
                    sendMessage("Frog/ssl/encoding",content_encoding)
                if 'set_cookie' in dir(layer):
                    set_cookie=layer.set_cookie
                    sendMessage("Frog/ssl/cookie",set_cookie)
                if 'server' in dir(layer):
                    server=layer.server
                    sendMessage("Frog/http",server)
                if 'user_agent' in dir(layer):
                    user_agent=layer.user_agent
                    sendMessage("Frog/http/user_agent",user_agent)
                #print "USER: " + user_agent
            elif "ip" in layer._layer_name:
                #print "ip"
                if 'src' in dir(layer):
                    source_addr= layer.src
                    sendMessage("Frog/ip/src",source_addr)
                if 'dst' in dir(layer):
                    dest_addr=layer.dst
                    sendMessage("Frog/ip/dst",dest_addr)
                if 'ttl' in dir(layer):
                    ttl=layer.ttl
                    sendMessage("Frog/ip/ttl",ttl)
                if 'id' in dir(layer):
                    ip_id=layer.id
            elif "ssl" in layer.layer_name:
                if 'handshake' in dir(layer):
                    handshake_protocol=layer.handshake
                #print "a rare SSL frog appears"

    capture_frogs()

# Start OSCServer
#print "\nStarting OSCServer. Use ctrl-C to quit."
#st = threading.Thread( target = s.serve_forever )
#st.start()

# Loop while threads are running.
#try :
#	while 1 :
#		sendMessage()
#		time.sleep(10)
 
#except KeyboardInterrupt :
#	print "\nClosing OSCServer."
#	s.close()
#	print "Waiting for Server-thread to finish"
#	st.join()
#print "Done"
#s.addMsgHandler("/user/4", print_conversation_header)
################

def print_conversation_header(pkt):
    try:
        protocol =  pkt.transport_layer
        http_user= pkt.http.user_agent
        if "Firefox" in http_user:
            http_user="Firefox"
        else:
            http_user="Chrome"

        http_host= pkt.http.host
        src_addr = pkt.ip.src
        src_port = pkt[pkt.transport_layer].srcport
        dst_addr = pkt.ip.dst
        dst_port = pkt[pkt.transport_layer].dstport
        ip_id=pkt.ip.id
        global counter
        counter+=1
        if counter==1:
            sendMessage("Frog/init",str(src_addr))
            frog_string= "You sat down on a table, " + str(http_user) + ", an arcane tool, in your hands. " 
            frog_string= "You couldn't help but notice that there was a marker on your table that had " + str(src_addr) + " written on it. This is who you are, for now." 
            frog_string= "Your eyes scanned across the room for "+ str(http_host) + " as you tried to find them."
            frog_string= "They said they would be waiting for you at Table " + str(dst_addr) + " but you couldn't see any from where you sat."
            frog_string= "Suddenly, a huge wave of frogs stormed into the room"
            frog_string= "They spoke the long forgotten language of "+ str(protocol) + ". So you tried to communicate with them in their language."
            frog_string= " 'Do you like to shake hands?', you asked"
            frog_string= " 'That won't be necessary', one of the frogs replied"
            #sendMessage()


        for layer in pkt.layers:
            frog_string= "Frogs hop around."
            if 'ssl' in layer.layer_name:
                ssl_content_type=layer.record
                ok=str(ssl_content_type)
                fine=ok.split(" ")
                frog_string= "A rare SSL frog appears"
                frog_string= "The rare SSL frog passes secret " + fine[len(fine)-1] + " " + fine[len(fine)-2] + " messages to you"
                frog_string= "You nod, acknowledging it, in secret."
                sendMessage("Frog/ssl", 'ack')

            if 'http' in layer.layer_name:
                frog_string= "A frog in the guise of a cookie" + str(layer.cookie) + " watches as you browse " + str(layer.request_full_uri) 
                frog_string= "An accommodating HTTP frog from " + str(layer.host) + " accepts " + str(layer.accept_encoding) + " variants of croak-coding reducing frog congestion in the room"
                frog_string= "'Are you an ETH Frog?', you ask"
                frog_string= "Deep down, all frogs are ETH frogs." 
                frog_string= "While being served by " + str(layer.server) + " the HTTP frog from " + str(layer.host) + " mutters the phrase: " + str(layer.response_phrase)
                sendMessage("Frog/http", 'served by HTTP frog')
                
            if 'udp' in layer.layer_name:
                sendMessage("Frog/udp",'udp')
                frog_string= "An unreliable UDP frog disables its own identification"
            if 'tcp' in layer.layer_name:
                if(random.random() < 0.3):
                    frog_string= "In the sky, " + str(layer.analysis_bytes_in_flight) + " frogs are still flying"
                if(random.random() < 0.6):
                    frog_string= "A frog waved a flag " + str(layer.flags) +  " that only other TCP-speaking frogs can understand"
                else:
                    frog_string= "Frog #" + str(layer.seq) + " said that it was waiting for Frog #" + str(layer.nxtseq)

                if str(layer.urgent_pointer)=='0':
                    frog_string= "I have an URGENT message to deliver to port " + str(layer.dstport) + ". Can you prioritize my message over other frogs?"
                    sendMessage("Frog/tcp",'urgent')

            if 'ip' in layer.layer_name:
                if str(layer.flags_df)=='1':
                    frog_string= "A IPv4 Frog #" + str(layer.id) + " arrives and requests, 'Please DO NOT FRAGMENT me. I have more coming behind me.'"
                    frog_string= "'Do you have any EXPLICIT CONGESTION NOTIFICATIONS?', you ask to the IPV4 Frog #" + str(layer.id) + "."
                    frog_string= " 'No, I don't and I like traffic', the IPV4 Frog #" + str(layer.id) + " replies"
                    frog_string= " 'That is fine', you reply. 'Please wait until more of you arrive from '" + str(layer.src) 
                else:
                    frog_string= "It is OK, says Frog #" + str(layer.id) + ". You can FRAGMENT me now"
                    frog_string= "OK, bye Frog #" + str(layer.id) + ". You shall be forgotten as you disappear in the crowd now."
                
                if(random.random() > 0.5):
                    frog_string= " 'Halt, Frog #" + str(layer.id) + "!', you shout. 'I need to know you aren't lost and just wandering like a croak. Show me your checksum!'"
                    frog_string= " The IPv4 frog shows its checksum " + str(layer.checksum) + " but unfortunately nobody cares about it."
                else:
                    frog_string= "Alas, the IPV4  Frog #" + str(layer.id) + " only has " + str(layer.ttl) + " hops to live"
                    sendMessage("Frog/ip",'few hops')                     


        
        # if pkt.ssl is not None:
        #     print "SSL is here"
        # handshake_length=pkt.ssl.handshake_length
        
        #print ip_id
        # json_obj = {
        #         'handshake_length':handshake_length,
        #         'protocol' : protocol,
        #         'user': http_user,
        #         'host':http_host,
        #         'srcaddr':src_addr,
        #         'ip_id':ip_id
        # }

        #a.append(json_obj)
        #print len(a)
        # with open('results.json', 'w') as fp:
        #     json.dump(json_obj, fp)
        #     json_obj.close();
        #temporarily disabled
        # if protocol == 'UDP':
        #     print 'A human who went by the title of %s , residing at %s , looked out the window marked with number %s, to talk to %s, who lived at %s via the ancient mystic language of %s'  % (http_user, src_addr, src_port, http_host, dst_addr, protocol)
        # else:
        #     print 'When %s heard a voice at %s , they could not help but look out of the window marked with number %s and thought of %s, who they had met a long time back at %s where they had together learnt the art of speaking in %s'  % (http_user, src_addr, src_port, http_host, dst_addr, protocol)     
    except AttributeError as e:
        #ignore packets that aren't TCP/UDP or IPv4
        pass

capture_frogs()
#cap.apply_on_packets(print_conversation_header, timeout=2)
