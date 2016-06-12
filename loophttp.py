import pyshark
 
cap = pyshark.LiveCapture('Wi-Fi')
 
def print_conversation_header(pkt):
    try:
        protocol =  pkt.transport_layer
        http_user= pkt.http.user_agent
        http_host= pkt.http.host
        src_addr = pkt.ip.src
        src_port = pkt[pkt.transport_layer].srcport
        dst_addr = pkt.ip.dst
        dst_port = pkt[pkt.transport_layer].dstport
        print 'A human who went by the title of %s , residing at %s , looked out the window %s, to talk to %s, who lived at %s via the ancient mystic language of %s'  % (http_user, src_addr, src_port, http_host, dst_addr, protocol)
    except AttributeError as e:
        #ignore packets that aren't TCP/UDP or IPv4
        pass
 
cap.apply_on_packets(print_conversation_header, timeout=100)