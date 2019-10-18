from app.views import *
import pytest

@pytest.mark.django_db
class TestViews(test.TestCase):
    def test_persona_create_view(self):
        path = reverse('event-dashboard')
        request = RequestFactory().get(path)
        response = dashboard_view(request)
        self.assertEqual(response.status_code, 200)