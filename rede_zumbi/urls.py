from rede_zumbi import views
from django.urls import path

from rest_framework.routers import SimpleRouter

app_name = 'rede_zumbi'

router = SimpleRouter()
router.register(
    'rede_zumbi/api',
    views.sobreviventeViewSet,
    basename='rede_zumbi/api'
)

urlpatterns = [
    path('', views.view_test)
]

urlpatterns += router.urls
