#!/usr/bin/python
"""
It is Auxscan 2.0 module ( WhoIs Lookup )
"""
from urllib2 import *

print
target = raw_input("Domain/IP Target\n Input :")
hackertarget = "http://api.hackertarget.com/whois/?q=" + target
hackertarget = urlopen(hackertarget).read()
print (hackertarget)
