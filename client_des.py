import socket
import pickle
import speech_recognition as sr
from Crypto.Cipher import DES

cipher = DES.new("8bytekey")

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

#obj = DES.new('This is a key123', DES.MODE_CFB, 'This is an IV456')
#obj2 = DES.new('This is a key123', DES.MODE_CFB, 'This is an IV456')
while True:

    
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {msglen}")

        full_msg += msg

        print(len(full_msg))


        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])


            d=pickle.loads(full_msg[HEADERSIZE:])
            #print(d)
            new_msg = True
            #full_msg = b""
            deciphered = cipher.decrypt(ciphertext)
            print("message : {}" .format(deciphered))
        
            exit()
        
