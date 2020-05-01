from django.http import HttpResponse
from django.shortcuts import render





def index(request):


    return render(request, 'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')


    #check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #which checkbox ix on
    if removepunc == "on":

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed + char
        params={'purpose':'removed punc', 'analyzed_text': analyzed}
        djtext = analyzed


    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char.upper()


        params = {'purpose': 'Capitalized', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose': 'to upper case', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'extra space removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcount == "on"):
        analyzed = len(djtext)
        djtext = analyzed
        params = {'purpose': 'No. of char', 'analyzed_text': analyzed}
    if(charcount != "on" and extraspaceremover != "on" and newlineremover !="on" and fullcaps !="on" and removepunc != "on"):
        return HttpResponse("error")


    return render(request, 'analyze.html', params)