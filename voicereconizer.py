from glob import glob
from vosk import Model,KaldiRecognizer
import pyaudio
from djitellopy import Tello
import time
tello=Tello()
#tello.connect()
model= Model(r"vosk-model-small-en-in-0.4")
recognizer=KaldiRecognizer(model,16000)
mic=pyaudio.PyAudio()
listening=False
response =''
result = ''
c = ''
def get_command():
    global response, result, c
    listening=True
    stream = mic.open(rate=16000,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=8192)

    while listening:
        stream.start_stream()
        try:
             data=stream.read(4096)
             if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                response = result[14:-3]
                listening=False
                return response
             
        except OSError: pass

def analyze_command(command):
    try:
        if command=="on":
            tello.connect()
        if command=="take" or command=="take off":
            tello.takeoff()
            print("takeoff has been recognized")
        elif command== "land" or command == 'l' or command == 'stop':
            tello.land()
            print("landing has been recognized")
        elif command=="move up" or command =="up":
            tello.move_up(30)
            print("moving up")
        elif command =="move down" or command == "down":
            tello.move_down(30)
            print("move down")
        elif command=="flip" or command == 'f' or command == 'action':
            print("flip")
            tello.flip_back()
        else:
            print("repeat again the command")
        
    except Exception: pass
    


while True:
    print("\nWaiting for command, Please speak after one second")
    command = get_command()
    print("Re", command)
    analyze_command(command)   
#stream.close() 
             
# from vosk import Model,KaldiRecognizer
# import pyaudio
# model= Model(r"C:\Users\GIRISH CHANDRA\vosk\vosk-model-small-en-in-0.4")
# reconiger=KaldiRecognizer(model,16000)
# mic=pyaudio.PyAudio()
# stream = mic.open(rate=16000,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=8192)
# stream.start_stream()

# while True:
#     data=stream.read(4096)
#    # if len(data)==0:
#     #    break
#     if reconiger.AcceptWaveform(data):
#         print(reconiger.Result()[14:-3])