import graphene

from graphene_django.types import DjangoObjectType
# from graphene_django.filter import DjangoFilterConnectionField

from .models import User

class UserType(DjangoObjectType):
  class Meta:
    model = User
    fields = ('id', 'username')

class Query(object):
  all_users = graphene.List(UserType)
  user = graphene.Field(UserType,
                        id=graphene.Int(),
                        username=graphene.String())

  def resolve_all_users(self, info, **kwargs):
    return User.objects.all()
  
  def resolve_user(self, info, **kwargs):
    id = kwargs.get('id')
    username = kwargs.get('username')

    if id is not None:
      return User.objects.get(pk=id)

    if username is not None:
      return User.objects.get(username=username)

    return None

class UserMutation(graphene.Mutation):
  class Arguments:
    # The input arguments for this mutation
    username = graphene.String(required=True)
    password = graphene.String(required=True)

  # The class attributes define the response of the mutation
  user = graphene.Field(UserType)

  def mutate(self, info, username, password):
    user = User(username = username, password=password)
    user.save()
    # Notice we return an instance of this mutation
    return UserMutation(user=user)


class Mutation(graphene.ObjectType):
  create_user = UserMutation.Field()
    
