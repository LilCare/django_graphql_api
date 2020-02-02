import graphene
import jwt
import json

from graphene_django.types import DjangoObjectType
from .models import User
from .controllers import searchUser, saveUser, authenticate, verifyToken, deleteUser
from config import jwt_key

class UserType(DjangoObjectType):
  class Meta:
    model = User
    fields = ('id', 'username')


class Query(object):
  user = graphene.Field(UserType,
                        id=graphene.Int(),
                        username=graphene.String())

  def resolve_user(self, info, **kwargs):
    return searchUser(**kwargs)


class CreateUser(graphene.Mutation):
  class Arguments:
    username = graphene.String(required=True)
    password = graphene.String(required=True)

  user = graphene.Field(UserType)

  def mutate(self, info, username, password):
    user = saveUser(username, password)
    return CreateUser(user=user)


class LoginUser(graphene.Mutation):
  class Arguments:
    username = graphene.String(required=True)
    password = graphene.String(required=True)

  jwt_token = graphene.String()

  def mutate(self, info, username, password):
    jwt_token = authenticate(username, password)
    return LoginUser(jwt_token=jwt_token)


class DeleteUser(graphene.Mutation):

  ok = graphene.Boolean()

  def mutate(self, info):
    authorization = info.context.headers.get('Authorization')
    token = verifyToken(authorization)
    ok = deleteUser(token)
    return DeleteUser(ok=ok)


class Mutation(graphene.ObjectType):
  create_user = CreateUser.Field()
  login_user = LoginUser.Field()
  delete_user = DeleteUser.Field()
