from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse('Here is the graphql index')

def userLookup(request, username):
  print(username)
  return HttpResponse("You're looking up user %s." % username)
