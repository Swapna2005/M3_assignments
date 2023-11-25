# from django.shortcuts import render
# from django.http import HttpResponse

# def members(request):
#     return HttpResponse("Hello world!")

from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
# def members(request):
#   template = loader.get_template('dictionary.html')
#   return HttpResponse(template.render())

def print_hello(request):
    sat_scores = {
    'Name':'swapna',
    'Age':18,
    'Place':'palakkad',}
    return render(request, 'dictionary.html', sat_scores)
