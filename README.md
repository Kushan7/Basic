# Basic
![This is an image](https://i.ibb.co/68shMZK/basic.png)
**In this repository "Basic" I will be uploading all the basic tools for hacking with basic functionalities.I will be improving the functionalities to make it better.**
# MAC Changer
![This is an image](https://i.ibb.co/f0Hzsnh/MAC-CHANGER.png)
It is a mac changer in which you can easy change MAC  address of any interface with help of some options and arguments.

# Why to change your MAC address ?

- Your ISP uses MAC address to identify or authenticate your Internet connection. So in case your network card goes boom, the new card you replace it with will have different MAC address and so the Internet wont work. So changing the MAC address to old network adapter is the quickest fix instead of telling your ISP to register your new MAC address which may take lot of time.

- If you want to access a network, which limits access based on MAC address, from another machine then you can change MAC address to the one for which you have access. Note that only one computer would be able to access the same network (no two computers can have same MAC address on same network to access it without any problem)

- A very important reason is privacy. Your MAC address can be seen by everyone on the local Ethernet network using many simple tools. A hacker on local network thus can track machines (and thus you) on the network. This is especially a threat when you are on a wireless network and are using a public WiFi network like in coffee shops, hotels or airports.

- If your original MAC address is revealed, an hacker can use it to impersonate you! On many networks (wired or wireless) access is restricted based on MAC address to avoid access to unauthorized devices on the network. So, when you go offline, someone can use your machine's MAC address and access the network as 'you'.

- You can get a new IP address lease from DHCP server by changing MAC address. On many networks, DHCP lease is set to last many days or is associated directly with a MAC address such that you get the same IP address all the time.

# How to Use MAC changer?

``git clone https://github.com/Kushan7/Hack_Legacy ``

``sudo python3 mac_changer.py -i {interface} -m {mac address} ``


# Help!

Usage: mac_changer.py [options]

Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        Interface to change its MAC address.
  -m NEW_MAC, --mac=NEW_MAC
                        New MAC address.
                        
                        

**I will be updating the tools in this repository regularly.**
