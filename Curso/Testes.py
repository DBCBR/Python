import pytest

# pytest.main(["-v", "Curso/teste_1.py", "Curso/teste_2.py"])
# pytest.main(["-k", "im", "-v", "Curso/teste_1.py", "Curso/teste_2.py"])

# pytest.main(["-m", "primarios", "-v","Curso/teste_1.py", "Curso/teste_2.py"])

pytest.main(["-k", "test_par3", "-v", 'Curso/teste_1.py'])