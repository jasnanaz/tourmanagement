from django.urls import path
from . import views
urlpatterns = [
    path('design/', views.design,name="design"),
    # path('designedit/', views.designedit, name="designedit"),
    path('destinations/', views.destinations, name="destinations")
]
