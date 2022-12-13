import struct 
import math 
import re
print("HHHHHHHHHHHHHHHHHHHH  HHHHHHHHHHHHHHHHHH                                                   HHHHHHHHHHHHHHHHHHHH   HHHHHHHHHHHHHHHHHH")
print("    HHHHHHHHH         HHH            HHH                                                        HHHHHHHHH         HHH            HHH")
print("    HHHHHHHHH         HHH            HHH                                HH                      HHHHHHHHH         HHH            HHH")
print("    HHHHHHHHH         HHH            HHH                                HH                      HHHHHHHHH         HHH            HHH")
print("    HHHHHHHHH         HHH            HHH                             HHHHHHHH                   HHHHHHHHH         HHH            HHH")
print("    HHHHHHHHH         HHH            HHH                                HH                      HHHHHHHHH         HHH            HHH")
print("    HHHHHHHHH         HHHHHHHHHHHHHHHHHHv            v H       H        HH                      HHHHHHHHH         HHHHHHHHHHHHHHHHHHv            v HHHHHHHH")
print("    HHHHHHHHH         HHH                v          v  H       H        HH     HHHHHHHHHHHH     HHHHHHHHH         HHH                v          v  H")
print("    HHHHHHHHH         HHH                 v        v   H       H        HH     H          H     HHHHHHHHH         HHH                 v        v   H")
print("    HHHHHHHHH         HHH                  v      v    HHHHHHHHH        HH     H          H     HHHHHHHHH         HHH                  v      v    HHHHHHHH")
print("    HHHHHHHHH         HHH                   v    v             H        HH     H          H     HHHHHHHHH         HHH                   v    v     H      H")
print("    HHHHHHHHH         HHH                    v  v              H        HH     H          H     HHHHHHHHH         HHH                    v  v      H      H")
print("HHHHHHHHHHHHHHHHHHHH  HHH                     vv               H        HH     HHHHHHHHHHHH HHHHHHHHHHHHHHHHHHHH  HHH                     vv       HHHHHHHH")
def ipv6to4like(ipv6): 
    ipv6_arr = ipv6.split(":")
    ipv6to4 = []
    for i in range(0,len(ipv6_arr)):
        if (ipv6_arr[i] == ''):
            ipv6to4.insert(i, "0")
        else:
            dec = int(str(ipv6_arr[i]),16)
            ipv6to4.insert(i, dec)

    if len(ipv6to4)<8:
        zeros = ipv6to4.index('0')
        for i in range (0,8):
            ipv6to4.insert(zeros,"0")
            if len(ipv6to4)==8: break
    
    return str('.'.join(map(str, ipv6to4)))

def ipv4liketo6(ipv6_4):
    ipv6_arr = ipv6_4.split(".")
    ipv6to4 = []
    for i in range(0,len(ipv6_arr)):
        if (ipv6_arr[i] == '' or ipv6_arr[i] == 0):
            ipv6to4.insert(i, '0')
        else:
            dec = hex(int(ipv6_arr[i])).split('x')[-1]
            ipv6to4.insert(i, dec)

    return str(':'.join(map(str, ipv6to4)))

def ip_delta4(ip1,ip2):
    ipv4_arr1, ipv4_arr2 = ip1.split("."), ip2.split(".")
    for i in range(0,len(ipv4_arr1)):        
        ipv4_arr1[i] = "0"*(3-len(ipv4_arr1[i]))+ipv4_arr1[i]
            
    for i in range(0,len(ipv4_arr2)):
        ipv4_arr2[i] = "0"*(3-len(ipv4_arr2[i]))+ipv4_arr2[i]

    ipv41=int(''.join(map(str, ipv4_arr1)))
    ipv42=int(''.join(map(str, ipv4_arr2)))
    delta = abs(ipv41-ipv42)

    return delta

def ip_delta6(ip1,ip2):
    ip1, ip2 = ipv6to4like(ip1), ipv6to4like(ip2)
    ipv4_arr1, ipv4_arr2 = ip1.split("."), ip2.split(".")
    for i in range(0,len(ipv4_arr1)):
        ipv4_arr1[i] = "0"*(5-len(ipv4_arr1[i]))+ipv4_arr1[i]
            
    for i in range(0,len(ipv4_arr2)):
        ipv4_arr1[i] = "0"*(5-len(ipv4_arr1[i]))+ipv4_arr1[i]

    ipv41=int(''.join(map(str, ipv4_arr1)))
    ipv42=int(''.join(map(str, ipv4_arr2)))
    delta = abs(ipv41-ipv42)

    return delta
def ipv(ip):
    f = ip.find(".")
    s = ip.find(":")
    if not(f or s): return -1
    if f: return 4
    if s: return 6
ip = input()
print(ipv6to4like("2a00:11d8:1201:0:962b:18:e716:fbff"))
print(ipv4liketo6(ip))#Вставить ipv4 сюда 
print(ip_delta4("192.168.0.1","192.168.0.24"))
print(ip_delta6("2a00:11d8:1201:0000:962b:18:e716:fb00","2a00:11d8:1201::962b:18:e716:fbff"))

print(ipv("192.168.0.1"))