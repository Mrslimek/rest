from django.contrib import admin
from django.urls import path
from django.urls import path
from .views import (ServiceView, create_service_from_list ,
                    get_full_data, create_service_category_from_list,
                    SubserviceView, ServiceCategoryView,
                    PeopleView, PeopleCategoryView,
                    create_people_category_from_list)

urlpatterns = [
    path('service/', ServiceView.as_view()),
    path('service/bulk/', create_service_from_list),
    path('subservice/', SubserviceView.as_view()),
    path('full-data/', get_full_data),
    path('service-category/', ServiceCategoryView.as_view()),
    path('service-category/bulk/', create_service_category_from_list),
    path('people/', PeopleView.as_view()),
    path('people-category/', PeopleCategoryView.as_view()),
    path('people-category/bulk/', create_people_category_from_list),
]
