import pyshark
import json
import math
import random
import platform
interface=""
<<<<<<< HEAD
if platform.system()=="Linux":
=======

if platform.system()=="linux":
>>>>>>> 1e91b1c5155cc7e1924a381b113fc877272d39d4
    interface="wlo1"
elif platform.system()=="Darwin":
    interface="en1"
elif platform.system()=="Windows":
    interface="Wi-Fi"

cap = pyshark.LiveCapture(interface)
counter=0;


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
            print "You sat down on a table, " + str(http_user) + ", an arcane tool, in your hands. " 
            print "You couldn't help but notice that there was a marker on your table that had " + str(src_addr) + " written on it. This is who you are, for now." 
            print "Your eyes scanned across the room for "+ str(http_host) + " as you tried to find them."
            print "They said they would be waiting for you at Table " + str(dst_addr) + " but you couldn't see any from where you sat."
            print "Suddenly, a huge wave of frogs stormed into the room"
            print "They spoke the long forgotten language of "+ str(protocol) + ". So you tried to communicate with them in their language."
            print " 'Do you like to shake hands?', you asked"
            print " 'That won't be necessary', one of the frogs replied"


        for layer in pkt.layers:
            print "Frogs hop around."
            if 'ssl' in layer.layer_name:
                ssl_content_type=layer.record
                ok=str(ssl_content_type)
                fine=ok.split(" ")
                print "A rare SSL frog appears"
                print "The rare SSL frog passes secret " + fine[len(fine)-1] + " " + fine[len(fine)-2] + " messages to you"
                print "You nod, acknowledging it, in secret."

            if 'http' in layer.layer_name:
                print "A frog in the guise of a cookie" + str(layer.cookie) + " watches as you browse " + str(layer.request_full_uri) 
                print "An accommodating HTTP frog from " + str(layer.host) + " accepts " + str(layer.accept_encoding) + " variants of croak-coding reducing frog congestion in the room"
                print "'Are you an ETH Frog?', you ask"
                print "Deep down, all frogs are ETH frogs." 
                print "While being served by " + str(layer.server) + " the HTTP frog from " + str(layer.host) + " mutters the phrase: " + str(layer.response_phrase)
                
            if 'udp' in layer.layer_name:
                print "An unreliable UDP frog disables its own identification"
            if 'tcp' in layer.layer_name:
                if(random.random() < 0.3):
                    print "In the sky, " + str(layer.analysis_bytes_in_flight) + " frogs are still flying"
                if(random.random() < 0.6):
                    print "A frog waved a flag " + str(layer.flags) +  " that only other TCP-speaking frogs can understand"
                else:
                    print "Frog #" + str(layer.seq) + " said that it was waiting for Frog #" + str(layer.nxtseq)

                if str(layer.urgent_pointer)=='0':
                    print "I have an URGENT message to deliver to port " + str(layer.dstport) + ". Can you prioritize my message over other frogs?"

            if 'ip' in layer.layer_name:
                if str(layer.flags_df)=='1':
                    print "A IPv4 Frog #" + str(layer.id) + " arrives and requests, 'Please DO NOT FRAGMENT me. I have more coming behind me.'"
                    print "'Do you have any EXPLICIT CONGESTION NOTIFICATIONS?', you ask to the IPV4 Frog #" + str(layer.id) + "."
                    print " 'No, I don't and I like traffic', the IPV4 Frog #" + str(layer.id) + " replies"
                    print " 'That is fine', you reply. 'Please wait until more of you arrive from '" + str(layer.src) 
                else:
                    print "It is OK, says Frog #" + str(layer.id) + ". You can FRAGMENT me now"
                    print "OK, bye Frog #" + str(layer.id) + ". You shall be forgotten as you disappear in the crowd now."
                
                if(random.random() > 0.5):
                    print " 'Halt, Frog #" + str(layer.id) + "!', you shout. 'I need to know you aren't lost and just wandering like a croak. Show me your checksum!'"
                    print " The IPv4 frog shows its checksum " + str(layer.checksum) + " but unfortunately nobody cares about it."
                else:
                    print "Alas, the IPV4  Frog #" + str(layer.id) + " only has " + str(layer.ttl) + " hops to live" 


        
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


cap.apply_on_packets(print_conversation_header, timeout=10000)