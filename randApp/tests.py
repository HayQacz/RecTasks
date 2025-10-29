from django.test import TestCase
from .utils import mix_word

class RandAppUtilsTests(TestCase):
    def test_word_mixing(self):
        self.assertEqual(mix_word("i"), "i")
        self.assertEqual(mix_word("am"), "am")
        self.assertEqual(mix_word("cat"), "cat")
        self.assertEqual(mix_word(""), "")

        word_before = "Django"
        word_after = mix_word(word_before)

        self.assertEqual(word_before[0], "D")
        self.assertEqual(word_before[-1], "o")

        self.assertEqual(len(word_after), len(word_before))

