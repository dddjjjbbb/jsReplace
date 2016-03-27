# -*- coding: utf-8 -*-

from jsLangs.jsReplaceDE import replaceFirstSection, replaceSecondSection, replaceThirdSection
import unittest


class TestJavascriptReplaceFunctions(unittest.TestCase):

    def setUp(self):
        self.firstSection = 'hhaayy wats thhe biig idae?'
        self.secondSection = 'what kind of language is that?'
        self.thirdSection = 'loosely typed'

    def tearDown(self):
        pass

    def test_replace_firstSection(self):

        expected = 'Was fällt dir denn eigentlich ein?'
        self.assertEqual(replaceFirstSection(self.firstSection), expected)

    def test_replace_secondSection(self):

        expected = 'welche Sprache ist das?'
        self.assertEqual(replaceSecondSection(self.secondSection), expected)

    def test_replace_thirdSection(self):

        expected = 'Schwach Typisierte'
        self.assertEqual(replaceThirdSection(self.thirdSection), expected)


if __name__ == '__main__':
    unittest.main()
