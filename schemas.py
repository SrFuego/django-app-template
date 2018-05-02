# apps/{{ app_name }}/schemas.py
# Python imports
import graphene

# Django imports

# Third party apps imports
from graphene_django import DjangoObjectType

# Local imports
# from .models import Document


# Create your schemas here.
# class DocumentSchema(DjangoObjectType):
#     class Meta:
#         model = Document
#
#
# class DocumentQuery(graphene.AbstractType):
#     documents = graphene.List(DocumentSchema)
#
#     @graphene.resolve_only_args
#     def resolve_documents(self):
#         return Document.objects.all()
