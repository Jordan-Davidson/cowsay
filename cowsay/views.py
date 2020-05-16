from django.shortcuts import render
from cowsay.forms import Newcowsay
from cowsay.models import Cowsay
from subprocess import check_output

# Create your views here.

def create_cowsay(request):
    html = 'index.html'
    if request.method == 'POST':
        form = Newcowsay(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            output = check_output(['cowsay', str(data['text'])])
            output = output.decode('utf-8')
            newCow = Cowsay.objects.create(text=data['text'])
            return render(request, html, {'form': form, 'newCow': newCow})
    form = Newcowsay()
    return render(request, html, {'form': form}) 

def history(request):
    html = 'history.html'
    data = Cowsay.objects.order_by('-id')[:10]
    return render(request,html,{'data' : data})