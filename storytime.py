import pyshark
import json
import math
import random
cap = pyshark.LiveCapture('Wi-Fi')
counter=0;

def print_conversation_header(pkt):
    try:
        for layer in pkt.layers:
            # if 'ssl' in layer.layer_name:
            #     ssl_content_type=layer.record
            #     ok=str(ssl_content_type)
            #     fine=ok.split(" ")
            #     print "A secret " + fine[len(fine)-1] + " " + fine[len(fine)-2] + " was exchanged between them"

            # if 'http' in layer.layer_name:
            #     print "My precious cookie: " + str(layer.cookie) + " watches as you browse " + str(layer.request_full_uri) 
            #     if(random.random() > 0.5):
            #         print "An accommodating HTTP from " + str(layer.host) + " accepts " + str(layer.accept_encoding) + " variants of encoding reducing burden"
            #     else:
            #         print "While being served by " + str(layer.server) + " the HTTP packet from " + str(layer.host) + " mutters the phrase: " + str(layer.response_phrase)
                
            if 'udp' in layer.layer_name:
                print "An unreliable UDP packet seeks denies identification"
            # if 'tcp' in layer.layer_name:
            #     if(random.random() < 0.3):
            #         print "In the sky, " + str(layer.analysis_bytes_in_flight) + " bytes are still flying"
            #     if(random.random() < 0.6):
            #         print "Someone waved a flag marked with " + str(layer.flags) +  " that only TCP-speakers can understand"
            #     else:
            #         print "Packet #" + str(layer.seq) + " said that it was waiting for Packet #" + str(layer.nxtseq)

            #     if str(layer.urgent_pointer)=='1':
            #         print "I have an URGENT message to me"

            # if 'ip' in layer.layer_name:
            #     if(random.random() > 0.5):
            #         print "Alas " + str(layer.id) + " only has " + str(layer.ttl) + " moments to live" 
            #     if str(layer.flags_df)=='1':
            #         print "The packet " + str(layer.id) + " requests, please DO NOT FRAGMENT me. I have more coming behind me." 
            #     else:
            #         print "It is OK, says Packet " + str(layer.id) + ". You can FRAGMENT me now"


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
        # if pkt.ssl is not None:
        #     print "SSL is here"
        # handshake_length=pkt.ssl.handshake_length
        global counter
        counter+=1
        if counter==1:
            print "You sat down on a table, " + str(http_user) + " an arcane tool, in your hands. " 
            print "You couldn't help but notice that there was a marker on your table that had " + str(src_addr) + " written on it. This is who you are now." 
            print "Your eyes scanned across the room for "+ str(http_host) + " as you tried to find them."
            print "They said they would be waiting for you at Table " + str(dst_addr) + " but you couldn't see any from where you sat."
            print "They spoke the long forgotten language of "+ str(protocol) 
        
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