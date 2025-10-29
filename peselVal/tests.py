from django.test import TestCase
from .forms import PeselForm
from .utils import get_pesel_info
import datetime

# https://pesel.cstudios.pl/o-generatorze/generator-on-line

Valid_Male_Pesel = "85090957674"
Valid_Female_Pesel = "96072921381"
Invalid_Checksum_Pesel = "85090957671"
Invalid_Chars_Pesel = "850909abcd4"

class PeselFormTests(TestCase):
    def test_pesel_form_is_valid(self):
        form = PeselForm(data = {"pesel": Valid_Male_Pesel})
        self.assertTrue(form.is_valid())

    def test_pesel_form_invalid_checksum(self):
        form = PeselForm(data = {"pesel": Invalid_Checksum_Pesel})
        self.assertFalse(form.is_valid())
        self.assertIn("Invalid PESEL number. Control number is incorrect", form.errors['pesel'][0])

    def test_pesel_form_invalid_length(self):
        form = PeselForm(data = {"pesel": "321123"})
        self.assertFalse(form.is_valid())

    def test_pesel_form_invalid_chars(self):
        form = PeselForm(data = {"pesel": Invalid_Chars_Pesel})
        self.assertFalse(form.is_valid())
        self.assertIn("Only numbers are allowed", form.errors['pesel'][0])

class PeselUtilsTests(TestCase):
    def test_get_info_male(self):
        info = get_pesel_info(Valid_Male_Pesel)
        self.assertEqual(info['gender'], 'Male')
        self.assertEqual(info['date_of_birth'], datetime.date(1985, 9, 9))

    def test_get_info_female(self):
        info = get_pesel_info(Valid_Female_Pesel)
        self.assertEqual(info['gender'], 'Female')
        self.assertEqual(info['date_of_birth'], datetime.date(1996, 7, 29))