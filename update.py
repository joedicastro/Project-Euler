#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Generate the python files for the problems from ProjectEuler.net
"""

import os
from glob import glob
from itertools import izip
from lxml.html import fromstring, clean, parse
from re import findall
from subprocess import check_output
from time import time
from urllib import urlretrieve
from urlparse import urlparse, urljoin
try:
    import ghost
    GHOST = True
except ImportError:
    GHOST = False


def get_data(t, c, url_base, root_path):
    """@todo: docstring for get_data

    :t: @todo
    :c: @todo
    :returns: @todo

    """
    problem_number, title = t.text.split(':', 1)
    problem_url = url_base + t.attrib['href']
    number = '{0:03d}'.format(int(problem_number.split()[1]))
    problem_path = os.path.join(root_path, number)
    problem_file = os.path.join(problem_path, number + '.py')

    problem_content, aux_files = get_problem_content(c, url_base)

    problem_text = u'''
    #!/usr/bin/env python2
    # -*- coding: utf8 -*-

    """
    {0}
    {1}
    {2}

    {3}
    """


    ###########################################################################
    #                                  answer                                 #
    ###########################################################################

    #'''.format(title[1:], problem_number, problem_url,
                problem_content).replace('    ', '').lstrip()

    return problem_path, problem_file, problem_text, aux_files


def get_problem_content(problem, url):
    """@todo: Docstring for get_problem_content

    :problem_c: @todo
    :returns: @todo

    """
    superscript = {'0': u'⁰',
                   '1': u'¹',
                   '2': u'²',
                   '3': u'³',
                   '4': u'⁴',
                   '5': u'⁵',
                   '6': u'⁶',
                   '7': u'⁷',
                   '8': u'⁸',
                   '9': u'⁹',
                   'a': u'ᵃ',
                   'b': u'ᵇ',
                   'c': u'ᶜ',
                   'd': u'ᵈ',
                   'e': u'ᵉ',
                   'f': u'ᶠ',
                   'g': u'ᶠ',
                   'h': u'ʰ',
                   'i': u'ⁱ',
                   'j': u'ʲ',
                   'k': u'ᵏ',
                   'l': u'ˡ',
                   'm': u'ᵐ',
                   'n': u'ⁿ',
                   'o': u'ᵒ',
                   'p': u'ᵖ',
                   'q': u'^q',
                   'r': u'ʳ',
                   's': u'ˢ',
                   't': u'ᵗ',
                   'u': u'ᵘ',
                   'v': u'ᵛ',
                   'w': u'ʷ',
                   'x': u'ˣ',
                   'y': u'ʸ',
                   'z': u'ᶻ'}

    subscript = {'0': u'₀',
                 '1': u'₁',
                 '2': u'₂',
                 '3': u'₃',
                 '4': u'₄',
                 '5': u'₅',
                 '6': u'₆',
                 '7': u'₇',
                 '8': u'₈',
                 '9': u'₉',
                 'a': u'ₐ',
                 'b': u'_b',
                 'c': u'_c',
                 'd': u'_d',
                 'e': u'ₑ',
                 'f': u'_f',
                 'g': u'_g',
                 'h': u'ₕ',
                 'i': u'ᵢ',
                 'j': u'_j',
                 'k': u'ₖ',
                 'l': u'ₗ',
                 'm': u'ₘ',
                 'n': u'ₙ',
                 'o': u'ₒ',
                 'p': u'ₚ',
                 'q': u'_q',
                 'r': u'ᵣ',
                 's': u'ₛ',
                 't': u'ₜ',
                 'u': u'ᵤ',
                 'v': u'ᵥ',
                 'w': u'_w',
                 'x': u'ₓ',
                 'y': u'_y',
                 'z': u'_z'}

    to_download = []
    for e in problem.iter():
        if e.tag == 'p' or e.tag == 'div':
            if 'text-align:center' in e.get('style', '') and e.text:
                e.text = '\n'.join(u'    {0}'.format(l) for l in
                                   e.text.split('\n'))
        elif e.tag == 'sup':
            e.text = u''.join([superscript.get(l, u'^{0}'.format(l)) for l in
                              e.text])
        elif e.tag == 'sub':
            e.text = u''.join([subscript.get(l, u'_{0}'.format(l)) for l in
                              e.text])
        elif e.tag == 'img':
            alt, src, tail = e.get('alt'), e.get('src').split('/'), e.tail
            e.clear()
            e.text, e.tail = src[-1] if src[0] == 'project' else alt, tail
            if src[0] == 'project':
                to_download.append(url + '/'.join(src))
        elif e.tag == 'dfn':
            e.text = u'{0} ({1})'.format(e.text, e.get('title'))

    return problem.text_content().replace('\r\n', '\n'), to_download


def offline(links, url, path):
    """@todo: Docstring for offline

    :links: @todo
    :returns: @todo

    """
    web_path = os.path.join(path, 'web')
    if not os.path.exists(web_path):
        os.mkdir(web_path)
    urlretrieve(urljoin(url, 'show=all'), os.path.join(web_path, 'index.html'))

    for link in links:
        if link[2].split('?')[0].split('.')[-1] not in ('php', 'xml'):
            parsed_url = urlparse(link[2])
            file_name = os.path.join(web_path, parsed_url.path.lstrip('/'))
            if os.path.splitext(file_name)[1] and not os.path.exists(file_name):
                if not os.path.exists(os.path.dirname(file_name)):
                    os.makedirs(os.path.dirname(file_name))
                urlretrieve(urljoin(url, parsed_url.path), file_name)


def get_processor():
    """f"""
    with open('/proc/cpuinfo') as cpuinfo:
        processor = findall(r'model name\s+: (.+)\n', cpuinfo.read())[0]
    return processor.replace('(R)', '').replace('(TM)', '')


def main():
    curr_path = os.getcwd()
    url_base = 'http://projecteuler.net/'

    GHOST = False  # Uncomment to debug

    processor = get_processor()

    if GHOST:
        url = url_base + 'show=unsolved'
        g = ghost.Ghost(wait_timeout=120)

        page, resources = g.open(url)
        g.wait_for_page_loaded()
        content = g.content.encode('utf8')
        element = fromstring(content)
    else:
        # element = fromstring(url.read())
        url = open('./web/index.html')
        element = parse(url).getroot()

    links = [link for link in element.iterlinks()]

    offline(links, url_base, curr_path)

    cleaner = clean.Cleaner(style=False, safe_attrs_only=False,
                            remove_tags=['var', 'br', 'i', 'font', 'small',
                                         'span', 'b'])
    element = cleaner.clean_html(element)

    titles = element.xpath('//*[@id="content"]/h3/a')
    contents = element.xpath('//*[@class="problem_content"]')

    problems = izip(titles, contents)
    results = {}

    for title, content in problems:
        problem_dir, problem_file, out, aux_files = get_data(title, content,
                                                             url_base,
                                                             curr_path)
        if not os.path.exists(problem_dir):
            os.mkdir(problem_dir)
        else:
            os.chdir(problem_dir)
            scripts = glob('*.py')
            results[os.path.basename(problem_dir)] = []
            for script in scripts:
                if open(script).readlines()[-1] != '#':
                    start_time = time()
                    if check_output('python2 {0}'.format(script).split()):
                        stop_time = time()
                        time_used = stop_time - start_time
                        results[os.path.basename(problem_dir)].append(
                            {'script': script, 'time': time_used})

        if not os.path.exists(problem_file):
            with open(problem_file, 'w') as output:
                print out
                output.write(out.encode('utf-8'))

            for f in aux_files:
                filename = os.path.join(problem_dir, f.split('/')[-1])
                if not os.path.exists(filename):
                    urlretrieve(f, filename)

    os.chdir(curr_path)
    with open('README.md', 'w') as readme:
        readme_header = '''
        # Project Euler Solutions

        Times computed in a {0} processor.\n

        '''.format(processor).replace('    ', '').lstrip()
        readme.write(readme_header)
        for result in sorted(results):
            if results[result]:
                readme.write('\n Problem {0}\n'.format(result))
                readme.write('-------------\n\n')
                for t in sorted(results[result], key=lambda x: x['script']):
                    readme.write('    {0:12} {1:.3f}s\n'.format(t['script'],
                                                                t['time']))

if __name__ == '__main__':
    main()
