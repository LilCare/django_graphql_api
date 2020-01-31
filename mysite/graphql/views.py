from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import User

# Create your views here.
def index(request):
  return HttpResponse('Here is the graphql index')

def userLookup(request, username):
  print(username)
  user = get_object_or_404(User, username=username)
  return HttpResponse("The following user exists in the database: %s" % username)

def createUser(request, username, password):
  user = User(username=username, password=password)
  user.save()
  return HttpResponse("You're adding a user %s." % user.id)
