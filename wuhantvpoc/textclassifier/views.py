from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
from .forms import TextClassifierForm
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TextClassifierForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            content = form.cleaned_data['text'].encode('utf-8')
            print type(content).__name__
            # process the data in form.cleaned_data as required
            result = models.classify(content)
            # redirect to a new URL:
            return HttpResponse(content + '  ' + result)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TextClassifierForm()

    return render(request, 'textclassifier/index.html', {'form': form})
