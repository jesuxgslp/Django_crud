import pytest

from app.models import Persona

pytestmark = pytest.mark.django_db

class TestPersonaModel:

    def test_save():
        product = Persona.objects.create(
            nombre="Jose de Jesus",
            apellido="Reyes Quevedo",
            fecha_nacimiento="08/02/1987"
        )
        assert product.name == "Jose de Jesus"
        assert product.price == "Reyes Quevedo"