import pytest
from abreviatura import abreviatura

@pytest.mark.parametrize("nome, abrev_esperada", [
	("David Barcellos Cardoso", "DBC"),
	("Ana Paula de Aquino Barcellos Cardoso", "APDABC"),
	("Yasmin de Aquino Barcellos Cardoso", "YDABC"),
	("Aurora de Aquino Barcellos Cardoso", "ADABC"),
	("Mushu de Aquino Barcellos Cardoso", "MDABC"),
	])
def test_abreviatura(nome, abrev_esperada):
	assert abreviatura(nome) == abrev_esperada
 