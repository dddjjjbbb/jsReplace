# -*- coding: utf-8 -*-

import re


def replaceFirstSection(line):
    return re.sub('hhaayy wats thhe biig idae\?', 'Was fällt dir denn eigentlich ein?', line)


def replaceSecondSection(line):
    return re.sub('what kind of language is that\?', 'welche Sprache ist das?', line)


def replaceThirdSection(line):
    return re.sub('loosely typed', 'Schwach Typisierte', line)


