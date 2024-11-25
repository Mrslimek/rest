from django.contrib import admin
from django.urls import path
from django.urls import path
from .views import (ServiceView, get_full_data,
                    CreateServiceCategoryFromList, ServiceCategoryView,
                    PeopleView, PeopleCategoryView)

urlpatterns = [
    path('service/', ServiceView.as_view()),
    # path('subservice/', get_subservice),
    path('full-data/', get_full_data),
    path('service-category/', ServiceCategoryView.as_view()),
    path('service-category/bulk/', CreateServiceCategoryFromList.as_view()),
    path('people/', PeopleView.as_view()),
    path('people-category/', PeopleCategoryView.as_view()),
    path('people-category/bulk/', PeopleCategoryView.as_view()),
]
