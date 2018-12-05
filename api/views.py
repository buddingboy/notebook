# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render



# from rest_framework import pagination, generics, LimitOffsetPagination, PageNumberPagination
# from . import serializers



# # class NotePagination(pagination.PageNumberPagination):
# #     page_size = 20  # the no. of company objects you want to send in one go

# # Assume url for this view is /api/v1/companies/
# class NoteListView(generics.ListAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
#     pagination_class = LimitOffsetPagination