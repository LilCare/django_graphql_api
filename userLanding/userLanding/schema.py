import graphene
import jwt
import json

from graphene_django.types import DjangoObjectType
from .models import User

class UserType(DjangoObjectType):
  class Meta:
    model = User
    fields = ('id', 'username')


class Query(object):
  user = graphene.Field(UserType,
                        id=graphene.Int(),
                        username=graphene.String())

  def resolve_user(self, info, **kwargs):
    id = kwargs.get('id')
    username = kwargs.get('username')

    if id is not None:
      return User.objects.get(pk=id)

    if username is not None:
      return User.objects.get(username=username)

    return None


class CreateUser(graphene.Mutation):
  class Arguments:
    username = graphene.String(required=True)
    password = graphene.String(required=True)

  user = graphene.Field(UserType)

  def mutate(self, info, username, password):
    user = User(username = username, password=password)
    user.save()
    return CreateUser(user=user)


class LoginUser(graphene.Mutation):
  class Arguments:
    username = graphene.String(required=True)
    password = graphene.String(required=True)

  jwt_token = graphene.String()

  def mutate(self, info, username, password):
    user = User.objects.get(username = username, password=password)
    
    if not user:
      raise Exception('Valid credentials were not provided')

    user.is_authenticated = True
    user.save()

    payload = {
      'id': user.id,
      'username': user.username
    }
    jwt_token = jwt.encode(payload, 'SECRET_KEY', algorithm='HS256')
    return LoginUser(jwt_token=jwt_token)


class DeleteUser(graphene.Mutation):

  ok = graphene.Boolean()

  def mutate(self, info, **kwargs):
    id = kwargs.get('id')
    username = kwargs.get('username')

    authorization = info.context.headers.get('Authorization')
    if not authorization:
      raise Exception('Authentication credentials were not provided')
    
    authorization = authorization.split('\'')
    if len(authorization) == 1 or authorization[0] != 'b':
      raise Exception('Authentication credentials were not provided')

    token = jwt.decode(authorization[1], 'SECRET_KEY')
    username = token.get('username')
    id = token.get('id')

    user = User.objects.get(pk=id, username=username)

    if not user.is_authenticated:
      raise Exception('Authentication not validated')

    user.delete()
    ok = True
    return DeleteUser(ok=ok)


class Mutation(graphene.ObjectType):
  create_user = CreateUser.Field()
  login_user = LoginUser.Field()
  delete_user = DeleteUser.Field()
