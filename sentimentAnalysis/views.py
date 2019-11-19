from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")
import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect,HttpResponse,Http404
from .forms import UploadFileForm
from django.contrib import messages

import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import re
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk import FreqDist
from wordcloud import WordCloud

import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

import pandas as pd
from sklearn.metrics import confusion_matrix, precision_score, recall_score

from django.core.files import File
from pycorenlp import StanfordCoreNLP


from .models import Requestlist, RequestlistManager
from .models import tweet, tweetResultManager
import time
from .tasks import run
import random
import yaml

#about firebase
import pyrebase
from django.contrib import auth

import celery
import json
import requests


session ={}
stream = open("sentimentAnalysis/config.yml", 'r')
data_loaded = yaml.safe_load(stream)

#for firebase
config =  data_loaded

#Initialize Firebase
firebase = pyrebase.initialize_app(config)
auther = firebase.auth()
database = firebase.database()


#for jwt (11/18)
import json
from aiohttp import web
from datetime import timedelta, datetime
import jwt

from .models import TokenInfo, TokenInfoManager

#default setting for jwt
JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 20

##To respond directly to information (QuerySet) in JSON directly from the database
def json_response(body='', **kwargs):
    kwargs['body'] = json.dumps(body or kwargs['body']).encode('utf-8')
    kwargs['content_type'] = 'text/json'
    return web.Response(**kwargs)

def main(request):
    if request.method == 'POST': 
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid() and 'request_id' in request.POST:
            form.save() #Save the Input File
            filePath="text/"+request.FILES['file'].name
            Requestlist(request_id = request.POST.get('request_id', ''), request_owner = request.POST.get('request_owner',0), request_status = "unassigned", request_pid = 0,
            vader_status="unassigned", vader_pid = 0, textblob_status = "unassigned",textblob_pid = 0, stanfordNLP_status= "unassigned",stanfordNLP_pid = 0, sentiWordNet_status="unassigned", sentiWordNet_pid = 0,
            request_issued_time = time.strftime(r"%Y-%m-%d %H:%M:%S", time.localtime()),request_completed_time = time.strftime(r"%Y-%m-%d %H:%M:%S", time.localtime()), file_path = filePath).save()
            unassignedRequest = None
            unassignedRequest = Requestlist.objects.get(request_id = request.POST.get('request_id', ''))
            if unassignedRequest != None :
                try:
                    run.apply_async(kwargs={'id': unassignedRequest.request_id},time_limit=60*30, soft_time_limit=60*30)
                except SoftTimeLimitExceeded:
                    print("SoftTimeLimitExceeded : ", SoftTimeLimitExceeded)
                    clean_up_in_a_hurry()
                except TimeoutError as err:
                    print("Timeout Error : ", err)
                #run.delay(unassignedRequest.request_id
            lists = Requestlist.objects.all()
            context = {'lists':lists}
            #tweet
            tweets_list = tweet.objects.all()
            tweets = {"tweets_list":tweets_list}
            return render(request, "result_page.html", context) 
    
    #when cookie is exist
    if(request.COOKIES.get('email') is not None):
        #get from token
        email = request.COOKIES.get('email')
        token = request.COOKIES.get('token_info')
        print("cookie_email: ", email)
        print("cookie_token: ", token)
        return render(request, "main_page.html", {"e":email}) 
        # check the token authenticate 
        # if(token authenticate succeess):
        #     return render(request, "main_page.html", {"e":email})
        # else(token authenticate fail):
        #     return render(request, "main_page.html") 

    #login request
    elif(request.POST.get('email') != None):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            #login using firebase
            user = auther.sign_in_with_email_and_password(email, password)
            print('user: ', user)
        except Exception as exception:
            print("ERROR : ", exception)
            messages = "nvalided account"
            return render(request, "loginpage.html", {"message":messages}) 
        #-----------------------------------
        payload = {
        'user_id': user['localId'], #local == uid(provided by firebase)
        'email': email,
        'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
        }
        jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)

        #save in database
        TokenInfo(uid = user['localId'], email = email, token = jwt_token, state = "1").save()
        print("token: ", jwt_token)
        #save cookie
        if jwt_token is not None:
            response = render(request, "main_page.html", {"e":email})
            response.set_cookie("token_info", jwt_token)
            response.set_cookie("email", email)
            return response
        return render(request, "main_page.html")
    # optional: store into our database
    # send the jwt token to our client
    # wrap the token in cookie
    # send the html page to the user
    else:
        return render(request, "main_page.html") 
           
#이지 코드 넣은 부분
def signIn(request):
    return render(request, "loginpage.html")

def logout_view(request):
    response = render(request, "main_page.html")
    response.delete_cookie('token_info')
    auth.logout(request)
    return render(request, "main_page.html")

#회원가입 창 & 로그인 창
def signUp(request):
    if(request.POST.get('email') != None):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = auther.create_user_with_email_and_password(email, password)
            print('user: ', user)
            return render(request, "main_page.html", {"e":email})
            
        except Exception as exception:
            print("ERROR : ", exception)
            messages = "unable to create account try again"
            return render(request, "signUp.html", {"message":messages})

        uid = user['localId']
        data = {"name":name, "status":"l"}
        database.child("users").child(uid).child("details").set(data)

        return render(request, "loginpage.html")       
    return render(request, 'signUp.html')