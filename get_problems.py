#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Generate the python files for the problems from ProjectEuler.net
"""

import os
from lxml.html import parse

root_path = os.getcwd()
url_base = 'http://projecteuler.net/'
url = url_base + 'show=unsolved'

element = parse(url).getroot()

titles = element.xpath('//*[@id="content"]/h3/a')

for i in titles:
    problem_number, title = i.text.split(':', 1)
    problem_url = url_base + i.attrib['href']
    number = '{0:03d}'.format(int(problem_number.split()[1]))
    problem_path = os.path.join(root_path, number)
    problem_file = os.path.join(problem_path, number + '.py')

    if not os.path.exists(problem_path):
        os.mkdir(problem_path)

    if not os.path.exists(problem_file):
        out = ''
        out += '#!/usr/bin/env python2' + os.linesep
        out += '# -*- coding: utf8 -*-' + os.linesep * 2
        out += '"""' + os.linesep
        out += title[1:] + os.linesep
        out += problem_number + os.linesep
        out += problem_url + os.linesep * 3
        out += '"""' + os.linesep * 3
        out += '#' * 75 + os.linesep
        out += '#' + ' ' * 34 + 'Answer' + ' ' * 33 + '#' + os.linesep
        out += '#' * 75 + os.linesep * 2 + '#'

        with open(problem_file, 'w') as output:
            output.write(out.encode('utf-8'))
