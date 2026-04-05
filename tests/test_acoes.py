import pytest
from busca_dados_acoes import calcular_ganho
import pandas as pd


def test_calcular_ganho_positivo():
    dados = pd.DataFrame({"Close": [100.0, 110.0]})
    assert calcular_ganho(dados) == 10.0


def test_calcular_ganho_negativo():
    dados = pd.DataFrame({"Close": [100.0, 90.0]})
    assert calcular_ganho(dados) == -10.0


def test_calcular_ganho_vazio():
    dados = pd.DataFrame({"Close": []})
    assert calcular_ganho(dados) == 0.0
