from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from multiprocessing import Process
from multiprocessing import Queue, Event
#from celery import Celery
#from celery.decorators import task
#from celery.utils.log import get_task_logger
import os
import signal
from signal import signal, SIGINT, SIGTERM, SIGABRT
import time
import threading
import sys
sys.path.append("djTest1")
from apps import getfactorial



# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"
    resg = -1
    finalText = []
    manager = None
    fact1 = 0
    htmlObj = None
    instance = None
    event = None
    resString = ""
  
    
    def __init__(self, default=0):
        template_name="index.html"
        HomePageView.resg = -1
        HomePageView.manager = Queue() 
        HomePageView.event = Event()        
 
    #function to display result of factorial calculations
    def getAA(event, request, queue):
        event.wait() 
        finalText = queue.get()    
        text = "" 
        context = None
        for s in finalText:
           text = text + s + "\n"
        context= {
        'resString': text
        }
        print(text)
        return render(request, 'index.html', context)
    #function to perform following actions
    #check if current web page already counting more than 5 factorials
    #start new process for factorial counts
    #show on web view message that factorial is counting
    def count_fact(request):
        if len(request.POST['factorial'])<=0:
            return render(request, 'index.html', context = None)
        try:
            resg = int(request.POST['factorial'])
        except:
            return 
        HomePageView.htmlObj = request
        if HomePageView.manager is None:
            HomePageView.manager = Queue()  
        if HomePageView.event is None:
            HomePageView.event = Event()
            
        if len(HomePageView.finalText)<5:
            HomePageView.finalText.append("Counting factorial of " + request.POST['factorial'])
            p = Process(target=getfactorial, args=(HomePageView.event, HomePageView.manager, resg,HomePageView.finalText,(len(HomePageView.finalText)-1)))
            p.start() 
            th = threading.Thread(target=HomePageView.getAA, args=(HomePageView.event,request,HomePageView.manager))
            th.start()
            #getfactorial.delay(resg, HomePageView.finalText, len(HomePageView.finalText)-1)
        else:
            HomePageView.finalText.append("Error. Number of requests have reached its maximum. Factorial of " + str(resg) + " will not be calculated.")
        text = "" 
        for s in HomePageView.finalText:
           text = text + s + "\n"
        context= {
        'resString': text
        }
        return render(request, 'index.html', context)
        
# Create your views here.
