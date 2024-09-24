import pytest
from Primeiroultimo import primeiroultimo

@pytest.mark.parametrize("nomecompleto,resultado", [("David Barcellos Cardoso","David Cardoso"),("Ana Paula de Aquino Barcellos Cardoso", "Ana Cardoso"),("Yasmin de Aquino Barcellos Cardoso","Yasmin Cardoso"),("Aurora de Aquino Barcellos Cardoso", "Aurora Cardoso"),("Mushu de Aquino Barcellos Cardoso", "Mushu Cardoso")])
def test_nomesprimeiroultimo(nomecompleto,resultado):
    assert primeiroultimo(nomecompleto) == resultado