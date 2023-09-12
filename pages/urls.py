from django.urls import path
from .views import homePageView

# HERE WILL BE ALL ROUTE CODE FOR PAGES APP
urlpatterns = [path("", homePageView, name="home")]
