from graphene import Schema, ObjectType
from library_admin_apps.library_app.schema.mutations import library_mutations
from library_admin_apps.library_app.schema.queries import library_queries
from library_admin_apps.users.schema.mutations import user_mutations
from library_admin_apps.users.schema.queries import user_queries




class RootMutation(library_mutations.Mutation, user_mutations.Mutation, ObjectType):
    pass


class RootQuery(library_queries.Query, user_queries.Query, ObjectType):
    pass


schema = Schema(query=RootQuery, mutation=RootMutation)
