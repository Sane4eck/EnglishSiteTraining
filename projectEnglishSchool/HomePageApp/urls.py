from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *
# from projectEnglishSchool.HomePageApp.views import OrderView

urlpatterns = [
    path('', func, name="func"),
]

router = SimpleRouter()
router.register('api/orders', OrderView )

urlpatterns += router.urls
