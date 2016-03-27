#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Script replaces content of inline JS script for any number of languages.
    Script illustrates EN2DE '''

import jsLangs
import os
import os.path
from os import walk
import codecs
import fnmatch
import argparse
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

JS_REPLACE_FUNCTIONS = {

    'DE': [jsLangs.jsReplaceDE.replaceFirstSection, jsLangs.jsReplaceDE.replaceSecondSection, jsLangs.jsReplaceDE.replaceThirdSection]
    }


def postprocessJS(line, operations):
    for operation in operations:
        line = operation(line)
    return line


def execute(filename, operation):
    with codecs.open(filename, 'r', encoding='UTF-8') as source:
        with codecs.open(filename + '.ready', 'w', encoding='UTF-8') as target:
            for line in source:
                target.write(postprocessJS(line, operation))


def main():

    parser = argparse.ArgumentParser(
        description="Specify the language to replace")
    parser.add_argument("--lang", type=str, dest='language')
    args = parser.parse_args()

    action = JS_REPLACE_FUNCTIONS[args.language.upper()]

    for dirName, subdirlist, filelist in walk("."):
        for filename in filelist:
            if fnmatch.fnmatch(filename, "*.html"):
                execute(os.path.join(dirName, filename), action)

if __name__ == '__main__':
    main()
