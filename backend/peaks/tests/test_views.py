from rest_framework.test import APITestCase
from peaks.models import Peak


class APITestCase(APITestCase):
    def test_create_peak(self):
        peaks = Peak.object.all()
        self.assertEqual(len(peaks), 0)

