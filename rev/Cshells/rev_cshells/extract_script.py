#! /usr/bin/python3

import binascii
	
m1 = ["6Eh","3Fh","0C3h","0B9h","0D7h","8Dh","15h","58h","0E5h","0Fh","0FBh","0ACh","22h","4Dh","57h","0h","0DFh","0CFh","0EDh","0FCh","1Ch","84h","6Ah","0D8h","1Ch","0A6h","17h","0C4h","0C1h","0BFh","0A0h","85h","87h","0A1h","43h","0D4h","58h","4Fh","8Dh","0A8h","0B2h","0F2h","7Ch","0A3h","0B9h","86h","37h","0DAh","0BFh","7","0Ah","7Eh","73h","0DFh","5Ch","60h","0AEh","0CAh","0CFh","0B9h","0E0h","0DEh","0FFh","0","70h","0B9h","0E4h","5Fh","0C8h","9Ah","0B3h","51h","0F5h","0AEh","0A8h","7Eh","8Dh","13h"]

m1_cleaned=[]
for i in m1:
	if i[-1]=='h':
		i=i[-2::-1]
		i=i[::-1]
		#i="0x"+i
	m1_cleaned.append(i)

#print(len(m1_cleaned))

m2 =["2Ch","4Ah","0B7h","99h","0A3h","0E5h","70h","78h","93h","6Eh","97h","0D9h","47h","6Dh","38h","0BDh","0FFh","0BBh","85h","99h","6Fh","0E1h","4Ah","0ABh","74h","0C3h","7Bh","0A8h","0B2h","9Fh","0D7h","0ECh","0EBh","0CDh","63h","0B2h","39h","23h","0E1h","84h","92h","96h","9","0C6h","99h","0F2h","58h","0FAh","0CBh","6Fh","6Fh","5Eh","1Fh","0BEh","2Bh","13h","8Eh","0A5h","0A9h","99h","93h","0ABh","8Fh","70h","1Ch","0C0h","0C4h","3Eh","0A6h","0FEh","93h","35h","90h","0C3h","0C9h","10h","0E9h"]

m2_cleaned=[]

for i in m2:
	if i[-1]=='h':
		i=i[-2::-1]
		i=i[::-1]
		#i="0x"+i
	m2_cleaned.append(i)


key=[]
input_value=""
for i in range(0,77):
	xored=int(m1_cleaned[i],16)^int(m2_cleaned[i],16)
	key.append('{:x}'.format(xored))
	input_value=input_value+key[i]

t=[]
input_value=""
for i in range(0,77):
	xored=int(m1_cleaned[i],16)^int(key[i],16)
	t.append('{:x}'.format(xored))
	input_value=input_value+t[i]

m3=["64h","1Eh","0F5h","0E2h","0C0h","97h","44h","1Bh","0F8h","5Fh","0F9h","0BEh","18h","5Dh","48h","8Eh","91h","0E4h","0F6h","0F1h","5Ch","8Dh","26h","9Eh","2Bh","0A1h","2","0F7h","0C6h","0F7h","0E4h","0B3h","98h","0FEh","57h","0EDh","4Ah","4Bh","0D1h","0F6h","0A1h","0EBh","9","0C6h","99h","0F2h","58h","0FAh","0CBh","6Fh","6Fh","5Eh","1Fh","0BEh","2Bh","13h","8Eh","0A5h","0A9h","99h","93h","0ABh","8Fh","70h","1Ch","0C0h","0C4h","3Eh","0A6h","0FEh","93h","35h","90h","0C3h","0C9h","10h","0E9h"]

m3_cleaned=[]

for i in m3:
	if i[-1]=='h':
		i=i[-2::-1]
		i=i[::-1]
		#i="0x"+i
	m3_cleaned.append(i)

#print(len(flag_cleaned))

flag=[]
final_flag=""
for i in range(0,77):
	xored=int(t[i],16)^int(m3_cleaned[i],16)
	flag.append('{:x}'.format(xored))
	#final_flag=input_value+key[i].decode("hex")


print(flag)

#flag = HTB{cr4ck1ng_0p3n_sh3ll5_by_th3_s34_sh0r3}HTB{cr4ck1ng_0p3n_sh3ll5_by_th3_s34_sh0r3}