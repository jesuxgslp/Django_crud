from mixer.backend.django import mixer
import pytest

@pytest.mark.django_db
def test_persona_tiene_nombre():
  persona = mixer.blend('app.Persona', quantity=1)
  assert len(str(persona)) != 0
