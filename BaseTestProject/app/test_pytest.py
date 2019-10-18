from app.views import storePet
import pytest

def test_store_pet():
    assert 'nombre' == 'alex'
    assert 'apellido' == 'Scott'