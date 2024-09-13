from graphene import Schema, ObjectType
from library_app.schema.mutations import library_mutations
from library_app.schema.queries import library_queries


class RootMutation(library_mutations.Mutation, ObjectType):
    pass


class RootQuery(library_queries.Query, ObjectType):
    pass


schema = Schema(query=RootQuery, mutation=RootMutation)
