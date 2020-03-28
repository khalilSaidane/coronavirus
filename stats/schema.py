from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import CountryStats



class CountryStatsNode(DjangoObjectType):
    class Meta:
        model = CountryStats
        filter_fields = ['name']

        interfaces = (relay.Node,)



class Query(ObjectType):
    country_stats = relay.Node.Field(CountryStatsNode)
    all_country_stats = DjangoFilterConnectionField(CountryStatsNode)
