#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Write the current solved status of the problems to a markdown file
"""

import os
import glob
import subprocess
import time

current_path = os.getcwd()
dirs = glob.glob('???')

with open('status.md', 'w') as output:
    output.write('')
    for d in sorted(dirs):
        output.write('\n Problem {0}\n'.format(d))
        output.write('-------------\n\n')
        os.chdir(os.path.join(current_path, d))
        scripts = glob.glob('*.py')
        for script in sorted(scripts):
            solved = False
            start_time = time.time()
            if subprocess.check_output('python2 {0}'.format(script).split()):
                stop_time = time.time()
                solved = True
            if solved:
                time_used = stop_time - start_time
                output.write('    {0:12} {1:.3f}s\n'.format(script, time_used))
            else:
                output.write('  _Unsolved_\n')
