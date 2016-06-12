import pyshark
capture = pyshark.LiveCapture(interface='Wi-Fi',display_filter='http')
capture.sniff(timeout=50)
capture
for packet in capture.sniff_continuously(packet_count=5):
    print "Person: ", packet.ip.src, "to : ", packet.ip.dst