
from threading import Thread,Semaphore,current_thread,Lock
from random import randint
import sys
import time

buff = []
semafor1 = Semaphore(value = 3)
semafor2 = Semaphore(value = 1)

def producator(semf):
	global buff
	while(1):
		semf.acquire()
		while(1):
			if(len(buff)<10):
				break
		produs  = randint(1,80)
		print "%s produce the element: %d \n" % (current_thread().name,produs)
		buff.append(produs)
		print buff
 		semf.release()
 		time.sleep(1.2)

def consumator(semaf):
	global buff
	while(1):
		semaf.acquire()
		if not buff:
			print "List is empty\n"
			semaf.release()
		else:	
			consuma = buff.pop()
			print "%s consum the element: %d \n" % (current_thread().name,consuma)
			semaf.release()
		time.sleep(1.2)

for i in range(4):
	thread = Thread(target = producator, args = (semafor1,))
	thread.start()


for i in range(4):
	thread = Thread(target = consumator, args = (semafor2,))
	thread.start()