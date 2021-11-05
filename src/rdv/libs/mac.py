import netifaces
for nic in netifaces.interfaces():
    print(nic)
    iface = netifaces.ifaddresses(nic)[netifaces.AF_LINK]
    if len(iface[0]['addr']) > 0:
        print("mac address: ", iface[0]['addr'])