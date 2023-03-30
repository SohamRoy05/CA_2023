#! /usr/bin/python3


xored_pass = ["47","7B","7A","61","77","52","7D","77","55","7A","7D","72","7F","32","32","32","13"]

password_hex = []

for i in range(0,17):
	xored=int(xored_pass[i],16)^int("13",16)
	password_hex.append('{:x}'.format(xored))
	#input_value=input_value+t[i]


print(password_hex)	