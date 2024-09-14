import graphene

class BookInputType(graphene.InputObjectType):
    title = graphene.String()
    author = graphene.String()
    summary = graphene.String()
