from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)

from montadoras.forms import ModeloForm, MontadoraForm, VeiculoForm
from montadoras.models import Modelo, Montadora, Veiculo


class HomeView(TemplateView):
    template_name = "home.html"


class MontadoraListView(ListView):
    model = Montadora
    template_name = "montadora_list.html"


class MontadoraCreateView(CreateView):
    model = Montadora
    form_class = MontadoraForm
    template_name = "montadora_form.html"
    success_url = reverse_lazy("montadora_list")


class MontadoraUpdateView(UpdateView):
    model = Montadora
    form_class = MontadoraForm
    template_name = "montadora_form.html"
    success_url = reverse_lazy("montadora_list")


class MontadoraDeleteView(DeleteView):
    model = Montadora
    template_name = "montadora_confirm_delete.html"
    success_url = reverse_lazy("montadora_list")


class ModeloListView(ListView):
    model = Modelo
    template_name = "modelo_list.html"


class ModeloCreateView(CreateView):
    model = Modelo
    form_class = ModeloForm
    template_name = "modelo_form.html"
    success_url = reverse_lazy("modelo_list")


class ModeloUpdateView(UpdateView):
    model = Modelo
    form_class = ModeloForm
    template_name = "modelo_form.html"
    success_url = reverse_lazy("modelo_list")


class ModeloDeleteView(DeleteView):
    model = Modelo
    template_name = "modelo_confirm_delete.html"
    success_url = reverse_lazy("modelo_list")


class VeiculoListView(ListView):
    model = Veiculo
    template_name = "veiculo_list.html"


class VeiculoCreateView(CreateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = "veiculo_form.html"
    success_url = reverse_lazy("veiculo_list")


class VeiculoUpdateView(UpdateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = "veiculo_form.html"
    success_url = reverse_lazy("veiculo_list")


class VeiculoDeleteView(DeleteView):
    model = Veiculo
    template_name = "veiculo_confirm_delete.html"
    success_url = reverse_lazy("veiculo_list")
