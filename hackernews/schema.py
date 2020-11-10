import graphene

import links.schema
import users.schema
import links.schema_relay


class Query(users.schema.Query, links.schema.Query, links.schema_relay.RelayQuery, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, links.schema.Mutation, links.schema_relay.RelayMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
