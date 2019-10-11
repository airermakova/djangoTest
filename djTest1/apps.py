from django.apps import AppConfig
from multiprocessing import Process
from multiprocessing import Queue, Event
from celery import Celery
from celery.decorators import task
from celery.utils.log import get_task_logger
import os
import signal
from signal import signal, SIGINT, SIGTERM, SIGABRT
import time


@task(name="getfactorial")    
def getfactorial(event, queue, data, strArray, strNum):  
    event.clear()  
    if data==0:
        return 0
    fact = 1
    for i in range(1,data+1):
        fact = fact*i
    strArray[strNum] = "Factorial of " + str(data) + " is " + str(fact)
    queue.put(strArray)     
    pid = os.getpid()  
    event.set()
    os.kill(pid, SIGABRT)   
