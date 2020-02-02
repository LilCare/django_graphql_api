import graphene

import userLanding.schema

class Query(userLanding.schema.Query, graphene.ObjectType):
    pass

class Mutation(userLanding.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)