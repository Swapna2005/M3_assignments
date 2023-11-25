from django.http import HttpResponse
from django.template import loader

# def members(request):
#   template = loader.get_template('register.html')
#   return HttpResponse(template.render())
def register(request):
   template=loader.get_template('register.html')
   return HttpResponse(template.render())