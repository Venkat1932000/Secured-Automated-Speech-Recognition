
#getting package for speech recognition,cryptography
import speech_recognition as sr
from Crypto.Cipher import AES
import socket
import time
import pickle


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5)


obj = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
obj2 = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')

#while true allows the program to run infinitely



    
clientsocket, address = s.accept()

#assign variable to access Recognizer functionalities
r=sr.Recognizer()

#setting high threshold limit for good audio capture 
r.energy_threshold = 50000
with sr.Microphone(0) as source:
    print("Say Something")
    audio=r.listen(source)
try:    
    #print(r.recognize_google(audio),"\n")
    voice = r.recognize_google(audio)
    print("Actual voice : {}" .format(voice))
    ciphertext = obj.encrypt(voice)
    print("Encrpted : {}" .format(ciphertext))
    
    
    #print(f"Connection from {address} has been established.")

    msg = pickle.dumps(ciphertext)

    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

    clientsocket.send(msg)

    
    #deciphered = obj2.decrypt(ciphertext)
    #print("Decrypted : {}" .format(deciphered))
    
except:
    pass
