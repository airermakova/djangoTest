from django.apps import AppConfig
from multiprocessing import Process
from multiprocessing import Queue, Event
from django.views.generic import TemplateView
from celery import Celery
from celery import Celery
from celery.decorators import task
from celery.utils.log import get_task_logger
import os
import signal
from signal import signal, SIGINT, SIGTERM, SIGABRT
import time
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.shortcuts import render_to_response
from django.urls import reverse
import sys
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
sys.path.append("webview")


def submit(event, queue):  
    event.wait()       
    finalText = queue.get()    
    text = "" 
    context = None
    for s in finalText:
       text = text + s + "\n"
    context= {
    'resString': text
    }
    pid = os.getpid()
    os.kill(pid, SIGABRT)  
    
