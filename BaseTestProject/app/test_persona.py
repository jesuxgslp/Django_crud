import django
from django.test import TestCase
import pytest
from .models import Persona


class Tests(TestCase):
    """ if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(Tests, cls).setUpClass()
            django.setup()

    @pytest.mark.django_db
    def test_persona(self):
        assert Persona.objects.count() == 1 """
    