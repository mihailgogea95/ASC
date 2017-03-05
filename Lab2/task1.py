#a) Folosind clasa Thread, creati 10 threaduri care afiseaza un mesaj de forma:
#    Hello, I'm thread id_thread

#b) Modificati codul anterior astfel incat thread-urile sa primeasca un 
#   index si un mesaj date ca parametru sub forma de dictionar
#   *hint: exemplu in lab1 http://cs.curs.pub.ro/wiki/asc/asc:lab1:index#functii

#c) Modificati codul anterior astfel incat thread-urile sa afiseze si numele
#   thread-ului (campul 'name' din clasa Thread)

#d) Modificati codul anterior astfel incat thread-urile sa primeasca index-ul
#   drept nume al thread-ului, afisati-l ca la punctul b)
#   * hint: folositi campul 'name' al constructorului clasei Thread

from threading import *
from time import sleep

def func(**dict):

   
    key = dict.keys()
    print "Thread name :" + currentThread().getName()
    print "Index:", key[0], " mesaj:", dict[key[0]]
    

list_threads = []

for x in range(0,10):
	t = Thread(target = func, kwargs = {str(x) : "mesajul" + str(x) }, name=str(x))
	list_threads.append(t)

for x in range(0,10):
	list_threads[x].start()
	sleep(0.5)

for x in range(0,10):
	list_threads[x].join()
