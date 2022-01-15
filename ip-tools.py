import struct
import math







def ipv6to4like(ipv6): #Converts hex ipv6 to address, that look like ipv4 Example: 
    ipv6_arr = ipv6.split(":")
    ipv6to4 = []
    for i in range(0,len(ipv6_arr)):
        if (ipv6_arr[i] == ''):
            ipv6to4.insert(i, "0000")
        else:
            dec = int(str(ipv6_arr[i]),16)
            ipv6to4.insert(i, dec)

    return str('.'.join(map(str, ipv6to4)))

def ipv4liketo6(ipv6_4):
    ipv6_arr = ipv6_4.split(".")
    ipv6to4 = []
    for i in range(0,len(ipv6_arr)):
        if (ipv6_arr[i] == '' or ipv6_arr[i] == 0):
            ipv6to4.insert(i, '0000')
        else:
            dec = hex(int(ipv6_arr[i])).split('x')[-1]
            ipv6to4.insert(i, dec)

    return str(':'.join(map(str, ipv6to4)))

def ip_delta4(ip1,ip2):
    ipv4_arr1 = ip1.split(".")
    ipv4_arr2 = ip2.split(".")
    for i in range(0,len(ipv4_arr1)):
        ai = len(ipv4_arr1[i])
        match ai:
            case 1:
                ipv4_arr1[i] = "00"+ipv4_arr1[i]
            case 2:
                ipv4_arr1[i] = "0"+ipv4_arr1[i]
    for i in range(0,len(ipv4_arr2)):
        ai = len(ipv4_arr2[i])
        match ai:
            case 1:
                ipv4_arr2[i] = "00"+ipv4_arr2[i]
            case 2:
                ipv4_arr2[i] = "0"+ipv4_arr2[i]           

    ipv41=int(''.join(map(str, ipv4_arr1)))    
    ipv42=int(''.join(map(str, ipv4_arr2)))
    delta = abs(ipv41-ipv42)

    return delta


def ip_delta6(ip1,ip2):
    ip1, ip2 = ipv6to4like(ip1), ipv6to4like(ip2)
    ipv4_arr1 = ip1.split(".")
    ipv4_arr2 = ip2.split(".")
    for i in range(0,len(ipv4_arr1)):
        ai = len(ipv4_arr1[i])
        match ai:
            case 1:
                ipv4_arr1[i] = "0000"+ipv4_arr1[i]
            case 2:
                ipv4_arr1[i] = "000"+ipv4_arr1[i]
            case 3:
                ipv4_arr1[i] = "00"+ipv4_arr1[i]
            case 4:
                ipv4_arr1[i] = "0"+ipv4_arr1[i]
            
    for i in range(0,len(ipv4_arr2)):
        ai = len(ipv4_arr2[i])
        match ai:
            case 1:
                ipv4_arr2[i] = "0000"+ipv4_arr2[i]
            case 2:
                ipv4_arr2[i] = "000"+ipv4_arr2[i]
            case 3:
                ipv4_arr2[i] = "00"+ipv4_arr2[i]
            case 4:
                ipv4_arr2[i] = "0"+ipv4_arr2[i]           

    ipv41=int(''.join(map(str, ipv4_arr1)))    
    ipv42=int(''.join(map(str, ipv4_arr2)))
    delta = abs(ipv41-ipv42)

    return delta



print(ipv6to4like("2a00:11d8:1201:0:962b:18:e716:fbff"))
print(ipv4liketo6("10752.4568.4609.0.38443.24.59158.64511"))
print(ip_delta4("192.168.0.1","192.168.0.24"))
print(ip_delta6("2a00:11d8:1201:0:962b:18:e716:fb00","2a00:11d8:1201::962b:18:e716:fbff"))
