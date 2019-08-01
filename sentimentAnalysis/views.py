from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

from django.shortcuts import render
from django.http import HttpResponseRedirect
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

# Create your views here.
session ={}
def sentimentAnalysis(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            tools=[]
            if type(request.POST.get('vader')) !=type(None):
                tools.append("Vader Sentiment")
            if type(request.POST.get('textblob')) != type(None):
                tools.append("TextBlob")
            if tools:
                #preprocess the file
                form.save()
                form.name = request.FILES['file'].name
                ids, contents, annotations, hashtags = preprocessFile(request.FILES['file'])

                form.ids=ids
                form.annotations=annotations
                form.content = contents #text type(list)
                form.hashtag = hashtags #text type(list)
                form.tool = tools

                #all content type(str)
                contentString = convertToString(contents)

                #surface metrics
                cleansingText = cleansing(contents)
                form.word_frequent = word_frequent(cleansingText)
                form.topFrequentWords=top_freqeunt(cleansingText)
                form.wordcounter = wordcounter(cleansingText)
                save_wordcloud(form.word_frequent,"basic")

                form.hashtag_frequent = top_freqeunt(hashtags)

                #sentimentAnalysis
                for i in tools:
                    if i == "Vader Sentiment":
                        form.vaderScores=vaderSentimentFucntion(form.content)
                        form.vaderPolarity=convertSentimentResult("Vader",form.vaderScores)
                        form.vaderCategory=compareFileWithVader(form.annotations,form.vaderPolarity)
                        form.vaderConfusionMatrix = confusionMatrix(form.annotations, form.vaderPolarity)
                        form.vaderPrecise = precise(form.annotations, form.vaderPolarity)
                        form.vaderRecall = recall(form.annotations, form.vaderPolarity)
                    elif i == "TextBlob":
                        form.textblobScores=textblobSentimentFunction(form.content)
                        form.textblobPolarity=convertSentimentResult("TextBlob",form.textblobScores)
                        form.textblobCategory=compareFileWithVader(form.annotations,form.textblobPolarity)
                        form.textblobConfusionMatrix = confusionMatrix(form.annotations, form.textblobPolarity)
                        form.textblobPrecise = precise(form.annotations, form.textblobPolarity)
                        form.textblobRecall = recall(form.annotations, form.textblobPolarity)

                context = {
                    'form':form,
                    }
                if type(request.POST.get('basic')) !=type(None):
                    global session
                    session = context
                    return render(request, "basic_page.html",session)
                elif type(request.POST.get('expert'))!=type(None):

                    positiveSet,negativeSet=separatePN(form.annotations,form.content)
                    positiveList = list(positiveSet)
                    negativeList = list(negativeSet)
                    positiveHashtag= extractHashtag(positiveList)
                    negativeHashtag= extractHashtag(negativeList)
                    form.positiveTopFrequentHashtag=top_freqeunt(positiveHashtag)
                    form.negativeTopFrequentHashtag=top_freqeunt(negativeHashtag)

                    #surface metrics
                    positiveCleansingText = cleansing(positiveList)
                    form.positiveWord_frequent = word_frequent(positiveCleansingText)
                    form.positiveTopFrequentWords=top_freqeunt(positiveCleansingText)
                    form.positiveWordcounter = wordcounter(positiveCleansingText)
                    save_wordcloud(form.positiveWord_frequent,"positive")

                    negativeCleansingText = cleansing(negativeList)
                    form.negativeWord_frequent = word_frequent(negativeCleansingText)
                    form.negativeTopFrequentWords=top_freqeunt(negativeCleansingText)
                    form.negativeWordcounter = wordcounter(negativeCleansingText)
                    save_wordcloud(form.negativeWord_frequent,"negative")

                    #sentimentAnalysis
                    for i in tools:
                        if i == "Vader Sentiment":
                            form.vaderScores=vaderSentimentFucntion(form.content)
                            form.vaderPolarity=convertSentimentResult("Vader",form.vaderScores)
                            form.vaderCategory=compareFileWithVader(form.annotations,form.vaderPolarity)
                            form.vaderConfusionMatrix = confusionMatrix(form.annotations, form.vaderPolarity)
                            form.vaderPrecise = precise(form.annotations, form.vaderPolarity)
                            form.vaderRecall = recall(form.annotations, form.vaderPolarity)

                        elif i == "TextBlob":
                            form.textblobScores=textblobSentimentFunction(form.content)
                            form.textblobPolarity=convertSentimentResult("TextBlob",form.textblobScores)
                            form.textblobCategory=compareFileWithVader(form.annotations,form.textblobPolarity)
                            form.textblobConfusionMatrix = confusionMatrix(form.annotations, form.textblobPolarity)
                            form.textblobPrecise = precise(form.annotations, form.textblobPolarity)
                            form.textblobRecall = recall(form.annotations, form.textblobPolarity)

                    context = {
                        'form':form,
                        }
                    session=context
                    return render(request, "expert_page.html",session)
            if not tools:
                messages.warning(request, 'You should check the tool at least 1!', extra_tags='alert')
    else:
        form = UploadFileForm()
    context = {
        'form':form,
    }
    return render(request, 'main_page.html', context)


def expert_page(request):
    if request.method == 'POST':
        global session
        if 'metric' in request.POST:
            return render(request,'expert_metrics.html',session)
        return render(request,'expert_page.html',session)

def basic_page(request):
    if request.method == 'POST':
        global session
        if 'metric' in request.POST:
            return render(request,'basic_metrics.html',session)
        return render(request,'basic_page.html',session)

def preprocessFile(f):
    fileName="text/"+f.name
    file = open(fileName, "r", encoding='UTF-8')
    text=file.readlines()

    id = []
    content = []
    hashtag = []
    annotation = []

    pattern = '#([0-9a-zA-Z]*)'
    hashtag_word = re.compile(pattern)

    for line in text:
        sentence = re.split(r'\t+', line)
        text = ""
        id.append(sentence[0])
        content.append(sentence[1])
        annotation.append(sentence[2].strip('\n'))

        for tag in hashtag_word.findall(line):
            hashtag.append(tag)

    return id,content,annotation, hashtag

def extractHashtag(list):
    hashtag=[]
    pattern = '#([0-9a-zA-Z]*)'
    hashtag_word = re.compile(pattern)
    for i in list:
        for j in hashtag_word.findall(i):
            hashtag.append(j)
    return hashtag

def convertToString(list):
    contentString=""
    for i in list:
        contentString+=i
        contentString+=" "
    return contentString

def separatePN(annotations,text):
    positiveSet = set()
    negativeSet = set()
    for i in range(len(annotations)):
        if annotations[i]=="Positive":
            positiveSet.add(text[i])
        elif annotations[i]=="Negative":
            negativeSet.add(text[i])
    return positiveSet,negativeSet

def cleansing(content):
    result = []
    url_pattern ='https?://\S+|#([0-9a-zA-Z]*)'

    for text in content:
        #대문자 소문자 변환
        lower_content = (text.lower())

        #불용어 제거
        shortword = re.compile(r'\W*\b\w{1,2}\b')
        shortword_content = shortword.sub('', lower_content)
        text = re.sub('[-=.#/?:$}!,@]', '', shortword_content)

        stop_words = set(stopwords.words('english'))
        content_tokens = word_tokenize(text)
        real_content = re.sub(pattern=url_pattern, repl='', string = text)

        for w in content_tokens:
            if w not in stop_words:
                    result.append(w)
    return result

def wordcounter(text):
    return(len(text))

def word_frequent(text):
    fd_content = FreqDist(text)
    return fd_content

def top_freqeunt(list):
    fd_content = FreqDist(list)
    return fd_content.most_common(5)

def save_wordcloud(text,fileName):
    wc = WordCloud(width=1000, height=600, background_color="white", random_state=0)
    plt.imshow(wc.generate_from_frequencies(text))
    plt.axis("off")
    plt.savefig("sentimentAnalysis/static/img/"+fileName+".png", format = "png")

def vaderSentimentFucntion(sentences):
    analyzer = SentimentIntensityAnalyzer()
    result = []
    for sentence in sentences:
        vs = analyzer.polarity_scores(sentence)
        result.append(vs['compound']) #only Compound value
    return result

#convert the result sentiment analysis for compare each of things
def convertSentimentResult(toolName,sentimentResult):
    converted=[]
    if toolName=="Vader" or toolName=="TextBlob":
        for i in sentimentResult:
            if i >= 0.05:
                converted.append("Positive")
            elif i<0.05 and i>-0.05:
                converted.append("Neutral")
            elif i<=-0.05:
                converted.append("Negative")
        return converted
    elif toolName=="userFile":
        for i in sentimentResult:
            if i == "4":
                converted.append("Positive")
            elif i == "2":
                converted.append("Neutral")
            elif i == "0":
                converted.append("Negative")
        return converted
    return converted

#compare the polarity of two lists
def compareFileWithVader(annotations, toolResults):
    category=[]
    for i in range(0,len(annotations)):
        if annotations[i]==toolResults[i]:
            category.append(True)
        else:
            category.append(False)
    return category

def textblobSentimentFunction(sentences):
    result = []
    for sentence in sentences:
        testimonial = TextBlob(sentence)
        result.append(testimonial.sentiment.polarity)
    return result

def confusionMatrix (annotation_result, tool_result):
 return confusion_matrix(annotation_result, tool_result, labels=["Positive", "Negative"])

def precise(annotation_result, tool_result):
    return precision_score(annotation_result, tool_result, average='macro')

def recall(annotation_result, tool_result):
    return recall_score(annotation_result, tool_result, average='macro')
