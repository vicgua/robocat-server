from graphene import ObjectType, String, Schema, Field
from graphene_django.debug import DjangoDebug

from .api_auth import Query as AuthQuery, Mutation as AuthMutation

from teams.schema import Query as TeamsQuery
from matches.schema import Query as MatchesQuery

class Query(ObjectType, AuthQuery, TeamsQuery, MatchesQuery):
    debug = Field(DjangoDebug, name='_debug')

class Mutation(ObjectType, AuthMutation):
    pass

schema = Schema(query=Query, mutation=Mutation)

