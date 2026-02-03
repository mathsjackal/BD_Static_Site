# Unit tests for extract title function

import unittest

from extract_title import extract_title

class Test_Extract_Title(unittest.TestCase):
    def test_extract_title_basic(self):
        md = "# Hello World"
        self.assertEqual(extract_title(md), "Hello World")
    
    def test_extract_title_strips_whitespace(self):
        md = "#    My Title    "
        self.assertEqual(extract_title(md), "My Title")

    def test_extract_title_ignores_h2(self):
        md = "## Subtitle"
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_extract_title_missing(self):
        md = "Just some text"
        with self.assertRaises(ValueError):
            extract_title(md)    
