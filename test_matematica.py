import pytest
from matematica import soma

def test_soma_retorna_resultado_correto():
    resultado = soma(1, 2)
    assert resultado == 3

def test_soma_somente_inteiros():
    with pytest.raises((TypeError, ValueError)):
        soma(1, "2")