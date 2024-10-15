from django import forms

from montadoras.models import Modelo, Montadora, Veiculo


class MontadoraForm(forms.ModelForm):
    class Meta:
        model = Montadora
        fields = ["nome", "pais", "ano_fundacao"]


class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = [
            "nome",
            "montadora",
            "valor_referencia",
            "motorizacao",
            "turbo",
            "automatico",
        ]


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = [
            "modelo",
            "cor",
            "ano_fabricacao",
            "ano_modelo",
            "valor",
            "placa",
            "vendido",
        ]
