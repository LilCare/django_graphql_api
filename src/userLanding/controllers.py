import jwt
import json

from .models import User
from config import jwt_key

def searchUser(**kwargs):
  username = kwargs.get('username')
  password = kwargs.get('password')
  id = kwargs.get('id')

  if username is not None and password is not None:
    return User.objects.get(username = username, password=password)

  if id is not None and username is not None:
    return User.objects.get(pk=id, username=username)

  if id is not None:
    return User.objects.get(pk=id)

  if username is not None:
    return User.objects.get(username=username)

  return None

def saveUser(username, password):
  user = User(username = username, password=password)
  user.save()
  return user

def authenticate(username, password):
  user = searchUser(username=username, password=password)
  user.is_authenticated = True
  user.save()
  jwt_token = createToken(user)
  return jwt_token

def createToken(user):
  payload = {
    'id': user.id,
    'username': user.username
  }
  jwt_token = jwt.encode(payload, jwt_key, algorithm='HS256')
  return jwt_token

def verifyToken(authorization):
  if not authorization:
    raise Exception('Authentication credentials were not provided')

  authorization = authorization.split('\'')
  if len(authorization) == 1 or authorization[0] != 'b':
    raise Exception('Authentication credentials were not provided')

  return authorization[1]

def deleteUser(token):
  userInfo = jwt.decode(token, jwt_key)
  username = userInfo.get('username')
  id = userInfo.get('id')
  user = searchUser(username=username, id=id)

  if not user.is_authenticated:
    raise Exception('Authentication not validated')

  user.delete()
  return True
