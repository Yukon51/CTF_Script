import pyshark

cap = pyshark.FileCapture("./ping.pcap", tshark_path="D:/Program Files/Wireshark/tshark.exe")

cipher = "".join(c.icmp.data[:2] for c in cap)
plantext = "".join(chr(int(cipher[i:i+2], 16)) for i in range(0, len(cipher), 2))
print(plantext)