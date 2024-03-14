
from django.http import HttpResponse
from django.template import loader
def ods(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def tennis_ods(request):
    template = loader.get_template('tennis.html')
    return HttpResponse(template.render())