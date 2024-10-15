from django.urls import path

from .views import (
    ModeloCreateView,
    ModeloDeleteView,
    ModeloListView,
    ModeloUpdateView,
    MontadoraCreateView,
    MontadoraDeleteView,
    MontadoraListView,
    MontadoraUpdateView,
    VeiculoCreateView,
    VeiculoDeleteView,
    VeiculoListView,
    VeiculoUpdateView,
)

urlpatterns = [

    path("montadoras/", MontadoraListView.as_view(), name="montadora_list"),
    path("montadoras/nova/", MontadoraCreateView.as_view(), name="montadora_create"),
    path(
        "montadoras/editar/<int:pk>/",
        MontadoraUpdateView.as_view(),
        name="montadora_update",
    ),
    path(
        "montadoras/deletar/<int:pk>/",
        MontadoraDeleteView.as_view(),
        name="montadora_delete",
    ),

    path("modelos/", ModeloListView.as_view(), name="modelo_list"),
    path("modelos/novo/", ModeloCreateView.as_view(), name="modelo_create"),
    path("modelos/editar/<int:pk>/", ModeloUpdateView.as_view(), name="modelo_update"),
    path("modelos/deletar/<int:pk>/", ModeloDeleteView.as_view(), name="modelo_delete"),

    path("veiculos/", VeiculoListView.as_view(), name="veiculo_list"),
    path("veiculos/novo/", VeiculoCreateView.as_view(), name="veiculo_create"),
    path(
        "veiculos/editar/<int:pk>/", VeiculoUpdateView.as_view(), name="veiculo_update"
    ),
    path(
        "veiculos/deletar/<int:pk>/", VeiculoDeleteView.as_view(), name="veiculo_delete"
    ),
]
