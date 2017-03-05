#
# Scrieti un program in care mai multe threaduri (numarul lor este dat ca
# argument in linia de comanda) aleg random un element dintr-o lista comuna si
# le adauga intr-o lista rezultat (tot comuna).
# a) in fiecare thread, afisati numele threadului si varianta din acel moment 
#    a listei rezultat
# b) in fiecare thread adunati elementul la o variabila globala. Protejati 
#    accesul la aceasta printr-un lock
# 
# !!! Verificati ca suma calculata in vareiabila globala este egala cu suma 
#    elementelor din lista rezultat. Rulati cu 1000 de threaduri.   
#
import sys, time, random
from threading import *
from random import randint
import time

threads = 0
suma = 0
lista = []
lista_dest = []
lock = Lock()
lista_t = []

def funct():
    time.sleep(random.uniform(0.5,0.8))
    number = random.choice(lista)
    global suma 
    lock.acquire()
    suma += int(number)
    lock.release()
    lista_dest.append(int(number))
    #to do print list_Dest
    print currentThread().getName()
    print "Suma cu functia de suma: " + str(sum(lista_dest))
    print "Suma calculata de thred-uri" +  str(suma)
    return number


if __name__ == "__main__":
    threads= int(sys.argv[1])
    for i in xrange(0, threads - 1):
        lista.append(random.randint(0, threads))
    for i in xrange(0, threads - 1):	
        t = Thread(target=funct)
        lista_t.append(t)
    for i in xrange(0, threads - 1):
        lista_t[i].start()   
    for i in xrange(0, threads - 1):
        lista_t[i].join()