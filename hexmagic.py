import pyshark
import json
import math
import random
import base64
cap = pyshark.LiveCapture('Wi-Fi')
a= []
def print_conversation_header(pkt):
    try:
        protocol =  pkt.layers
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
        # ok=""
        # while random.random() > 0.1:
        #     ok+="    "
        ascii_string = str(base64.b16decode(pkt.ip_id))[2:-1]
        print (ascii_string)
        # ok=str(pkt.ip.id)
        # print ok
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
 
cap.apply_on_packets(print_conversation_header, timeout=50)