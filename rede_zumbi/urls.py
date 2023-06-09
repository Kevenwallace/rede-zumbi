from rede_zumbi import views
from django.urls import path

from rest_framework.routers import SimpleRouter

app_name = "rede_zumbi"

router = SimpleRouter()
router.register("rede_zumbi/api", views.sobreviventeViewSet, basename="rede_zumbi/api")
router.register("rede_zumbi/inf", views.infectadoCadastro)
router.register("rede_zumbi/inventario", views.InventarioViewSet)
router.register("rede_zumbi/mercado", views.MercadoZumbi)
router.register("rede_zumbi/item", views.ItemsViewSet)


urlpatterns = [path("", views.view_test)]

urlpatterns += router.urls
