import pytest

from app.models import Persona

pytestmark = pytest.mark.django_db

class TestPersonaModel:

    def test_save():
        person = Persona.objects.create(
            nombre="Jose de Jesus",
            apellido="Reyes Quevedo",
            fecha_nacimiento="08/02/1987"
        )
        #assert person.name == "Jose de Jesus"
        #assert person.price == "Reyes Quevedo"