#!/usr/bin/python3

import socket
import re
import time

host = "64.227.41.83"
port = 30359
result=b""

# try and connect to a bind shell
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    try :  
        print("[+] Connected to bind shell!\n")
        
        while 1: 
            s.send(bytes(b"1"+b"\n")) 
            result = s.recv(1024).strip()  
            for i in range(0,501):
                num=""  
                
                
                #print(result)
                x=re.findall("(\d*\s[\+-/\*]\s\d*)",str(result))
                if len(x) > 0:
                    
                    for i in x:
                        num=num+i

                    try:
                        round(float(eval(num)),2)
                    except ZeroDivisionError:
                        s.send(bytes("DIV0_ERR","utf-8")+b"\n") 
                        result = s.recv(1024).strip()
                        print(result)
                        continue
                    answer = round(float(eval(num)),2)                   
                    print(answer)
                    if answer>1337.00 or answer<-1337.00:
                        s.send(bytes("MEM_ERR","utf-8")+b"\n") 
                        result = s.recv(1024).strip()
                        print(result)
                        continue

                    #print(answer)    
                    s.send(bytes(str(answer),"utf-8")+b"\n") 
                    result = s.recv(1024).strip()
                    print(result)
                    if len(re.findall(".Incorrect response.",str(result)))>0:
                        exit(0)
                        

    except KeyboardInterrupt:
        print ("\n[+] ^C Received, closing connection")
        s.close();
    except EOFError:
        print ("\n[+] ^D Received, closing connection")
        s.close();

except socket.error:
    print ("[+] Unable to connect to bind shell.")