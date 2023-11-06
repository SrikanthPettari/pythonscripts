#!/usr/bin/env python3

import sys
import socket

def Name_to_IP(name):
    #name = input("Enter the Ipaddress: ")
    try:
        ipaddr = socket.gethostbyname(name)
        fqdn = socket.gethostbyaddr(ipaddr)[0]
        addr = socket.gethostbyaddr(ipaddr)[2]
    except socket.herror as e:
        print("UNKNOWN HOST:%s"%e)
        sys.exit(1)
    except socket.gaierror as e:
        print("SERVICE NOT KNOWN: %s" %e)
        sys.exit(1)

    return fqdn, addr

def main():
    result = Name_to_IP(name)
    print(result)
    return result

if __name__ == "__main__":
    name = input("Enter the IPAddress: ")
    main()
