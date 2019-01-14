import time
import mido
from mido import Message
from concurrent.futures import ThreadPoolExecutor
from random import uniform
from random import randint
import threading

# print ("Midi out:")
# print (mido.get_output_names ())  # To list the output ports
# print ("Midi in:")
# print (mido.get_input_names ())  # To list the input ports

output_midi_name = "M-Track 2X2M 1"
outport = mido.open_output (output_midi_name)

scala_midi = pentatonica_minore_C = [ 60, 63, 65, 67, 70, 72 ]
print ("Pentatonica Minore C4:", pentatonica_minore_C)

def nota(scala, offset):
    while True:
        i = randint (0, 5)
        rand_time=uniform(1.55, 2.55)
        tempo = 1
        delay= tempo + uniform(0.1, 0.99999999) - 0.5
        #delay = uniform (1.5, 2.5)
        # msg = Message('polytouch', note = scala[i], value=80)
        msg = Message('note_on', note=scala[i], velocity=64, time=15, channel=0)
        outport.send(msg)
        print ("Nota: ", scala[ i ])
        time.sleep (delay+offset)
        #time.sleep (5)
        msg = Message ('note_off', note=scala[i], velocity=64, time=15, channel=0)
        outport.send (msg)
        time.sleep (delay+offset)
        #time.sleep (5)
        #print ("Task Executed {}".format (threading.current_thread ()))

def accordo(scala, offset_ottava):
    while True:
        i = randint (0, 5)
        rand_time=uniform(1.55, 2.55)
        tempo = 2
        #delay= tempo + uniform(0.1, 0.99999999) - 0.5
        #delay = uniform (1.5, 2.5)
        # msg = Message('polytouch', note = scala[i], value=80)
        msg = Message('note_on', note=scala[i]-offset_ottava, velocity=64, time=15, channel=0)
        outport.send(msg)
        print ("Accordo: ", scala[ i ] - offset_ottava)
        #time.sleep (delay+offset)
        time.sleep (5)
        msg = Message ('note_off', note=scala[i]-offset_ottava, velocity=64, time=15, channel=0)
        outport.send (msg)
        #time.sleep (delay+offset)
        time.sleep (1)
        #print ("Task Executed {}".format (threading.current_thread ()))

def main():
    executor = ThreadPoolExecutor(max_workers=5)
    task1 = executor.submit(accordo, scala_midi,10)
    task2 = executor.submit(accordo, scala_midi,10)
    task3 = executor.submit(accordo, scala_midi,10)
    task4 = executor.submit (nota, scala_midi, 0.09)
    #task5 = executor.submit (nota, pentatonica_minore_C, 10)


if __name__ == '__main__':
    main()
    #nota(pentatonica_minore_C)
