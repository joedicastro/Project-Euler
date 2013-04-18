#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Generate the python files for the problems from ProjectEuler.net
"""

import json
import os
from collections import defaultdict
from itertools import izip
from re import findall
from subprocess import check_output
from time import time
from urllib import urlretrieve
from urlparse import urlparse, urljoin

from lxml.html import fromstring, parse
from lxml.html.clean import Cleaner


try:
    import ghost
    GHOST = True
except ImportError:
    GHOST = False


def get_problem_data(title, content, url_base, root_path):
    """@todo: docstring for get_problem_data

    :title: @todo
    :content: @todo
    :returns: @todo

    """
    problem_number, problem_title = title.text.split(':', 1)
    problem_url = url_base + title.attrib['href']
    number = '{0:03d}'.format(int(problem_number.split()[1]))
    problem_path = os.path.join(root_path, number)
    problem_file = os.path.join(problem_path, number + '.py')

    problem_content, aux_files = get_problem_content(content, url_base)

    problem_text = u'''
    #!/usr/bin/env python2
    # -*- coding: utf8 -*-

    """
    {0}
    {1}
    {2}

    {3}
    """


    '''.format(problem_title[1:], problem_number, problem_url,
               problem_content).replace('    ', '').lstrip()

    return {'dir': problem_path, 'file': problem_file, 'text': problem_text,
            'aux': aux_files, 'number': number}


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
    for elm in problem.iter():
        if elm.tag == 'p' or elm.tag == 'div':
            if 'text-align:center' in elm.get('style', '') and elm.text:
                elm.text = '\n'.join(u'    {0}'.format(l) for l in
                                     elm.text.split('\n'))

        elif elm.tag == 'sup':
            elm.text = u''.join([superscript.get(l, u'^{0}'.format(l)) for l in
                                elm.text])

        elif elm.tag == 'sub':
            elm.text = u''.join([subscript.get(l, u'_{0}'.format(l)) for l in
                                elm.text])

        elif elm.tag == 'img':
            alt, src, tail = (elm.get('alt'), elm.get('src').split('/'),
                              elm.tail)
            elm.clear()
            elm.text, elm.tail = src[-1] if src[0] == 'project' else alt, tail
            if src[0] == 'project':
                to_download.append(url + '/'.join(src))

        elif elm.tag == 'dfn':
            elm.text = u'{0} ({1})'.format(elm.text, elm.get('title'))

    return problem.text_content().replace('\r\n', '\n'), to_download


def offline(links, url, path):
    """Download an off-line copy of the Euler Project's website

    :links: the links of files to download
    :url: the website's url
    :path: the current working path

    """
    web_path = os.path.join(path, 'web')
    if not os.path.exists(web_path):
        os.mkdir(web_path)

    # download the "all problems" page as the index page for the off-line site
    urlretrieve(urljoin(url, 'show=all'), os.path.join(web_path, 'index.html'))

    for link in links:
        if link[2].split('?')[0].split('.')[-1] not in ('php', 'xml'):
            parsed_url = urlparse(link[2])
            filname = os.path.join(web_path, parsed_url.path.lstrip('/'))
            if os.path.splitext(filname)[1] and not os.path.exists(filname):
                if not os.path.exists(os.path.dirname(filname)):
                    os.makedirs(os.path.dirname(filname))
                urlretrieve(urljoin(url, parsed_url.path), filname)


def get_processor():
    """Get the name of the computer's processor

    :returns: the computer's processor name

    """
    with open('/proc/cpuinfo') as cpuinfo:
        processor = findall(r'model name\s+: (.+)\n', cpuinfo.read())[0]
    return processor.replace('(R)', '').replace('(TM)', '')


def get_git_files(repository, staged=False):
    """Get a list of files under a git repository.

    :repository: the git repository
    :staged: if false return all files, else return only the staged ones
    :returns: the files under git control

    """
    os.chdir(repository)
    if staged:
        git_command = "git diff --cached --name-only".split()
    else:
        git_command = "git ls-files".split()
    git_output = check_output(git_command).split(os.linesep)
    files = [os.path.join(repository, line) for line in git_output if line]

    return files


def scripts_per_problem(files):
    """@todo: Docstring for get_python_files_under_git

    :arg1: @todo
    :returns: @todo

    """
    scripts = defaultdict(list)
    for fil in files:
        if os.path.splitext(fil)[-1] == '.py':
            key = os.path.basename(os.path.dirname(fil))
            scripts[key].append(fil)
    return scripts


def write_readme(path, results):
    """Write the README.md document.

    """
    os.chdir(path)
    with open('README.md', 'w') as readme:
        readme_header = '''
        # Project Euler Solutions

        Times computed in a {0} processor.\n

        Solved {1} out of {2} problems
        '''.format(get_processor(), 46, 422).replace('    ', '').lstrip()
        readme.write(readme_header)
        for result in sorted(results):
            if results[result]:
                readme.write('\n Problem {0}\n'.format(result))
                readme.write('-------------\n\n')
                for sol in sorted(results[result].keys()):
                    readme.write('    {0:12} {1:.3f}s\n'.
                                 format(sol, results[result][sol]))

    # FIXME: get the number of solved problems and total


def clean_element(element):
    """Remove unnecesary tags from the lxml element.

    :element: the lxml element
    :returns: the cleaned lxml element

    """
    tags = ['var', 'br', 'i', 'font', 'small', 'span', 'b']
    cleaner = Cleaner(style=False, safe_attrs_only=False, remove_tags=tags)
    return cleaner.clean_html(element)


def get_element_et_links(url):
    """Get the lxml element

    :url: the webpage url
    :returns: the cleaned lxml element and all the webpage links

    """
    GHOST = False  # Uncomment to debug TODO: delete this line

    if GHOST:
        ghost_object = ghost.Ghost(wait_timeout=120)

        ghost_object.open(url)
        ghost_object.wait_for_page_loaded()
        content = ghost_object.content.encode('utf8')
        element = fromstring(content)
    else:
        element = parse(url).getroot()

    links = [link for link in element.iterlinks()]

    element = clean_element(element)

    return element, links


def get_time(script, problem_dir):
    """Gets the time taken to solve a problem.

    :problem: the python script used to solve a problem
    :problem_dir: the directory where the script is
    :returns: the time taken to solve a problem

    """
    os.chdir(problem_dir)
    start_time = time()
    if check_output('python2 {0}'.format(script).split()):
        stop_time = time()
    return stop_time - start_time


def get_web_content(element):
    """@todo: Docstring for get_web_content

    :element: @todo
    :returns: @todo

    """
    titles = element.xpath('//*[@id="content"]/h3/a')
    contents = element.xpath('//*[@class="problem_content"]')
    return izip(titles, contents)


def download_aux_files(data):
    """Download the auxiliary files to resolve the problems.

    :data:

    """
    for fil in data['aux']:
        filename = os.path.join(data['dir'], fil.split('/')[-1])
        if not os.path.exists(filename):
            urlretrieve(fil, filename)


def read_json(json_file):
    """@todo: Docstring for read_symlinks

    :json_file: @todo
    :returns: @todo

    """
    with open(json_file, 'r') as json_in:
        jjson = json.load(json_in)
    return jjson


def store_json(times, json_file):
    """@todo: Docstring for store_symlinks

    :symbolic_links: store the symbolic links into a json file

    """
    with open(json_file, 'w') as json_out:
        json.dump(times, json_out, indent=4)


def main():
    """The main function."""
    curr_path = os.getcwd()
    json_times = os.path.join(curr_path, 'times.json')

    domain = 'http://projecteuler.net/'
    url = domain + 'show=unsolved'

    element, links = get_element_et_links(url)

    if os.path.exists(json_times):
        times = read_json(json_times)
    else:
        times = defaultdict(dir)

    changes = False

    git_files = scripts_per_problem(get_git_files(curr_path))
    git_staged = scripts_per_problem(get_git_files(curr_path, True))

    for title, content in get_web_content(element):
        problem_data = get_problem_data(title, content, domain, curr_path)

        if not os.path.exists(problem_data['dir']):
            changes = True
            os.mkdir(problem_data['dir'])
        else:
            key = problem_data['number']
            for script in git_files[problem_data['number']]:
                s_name = os.path.basename(script)
                if not times.get(problem_data['number'], {}):
                    total = get_time(script, problem_data['dir'])
                    times[key] = {s_name: total}
                if not times.get(problem_data['number'], {}).get(s_name):
                    total = get_time(script, problem_data['dir'])
                    times[key][s_name] = total

            for script in git_staged[problem_data['number']]:
                s_name = os.path.basename(script)
                if not times.get(problem_data['number'], {}):
                    total = get_time(script, problem_data['dir'])
                    times[key] = {s_name: total}
                elif not times.get(problem_data['number'], {}).get(s_name):
                    total = get_time(script, problem_data['dir'])
                    times[key][s_name] = total
                else:
                    total = get_time(script, problem_data['dir'])
                    times[key][s_name] = total

        if not os.path.exists(problem_data['file']):
            with open(problem_data['file'], 'w') as output:
                output.write(problem_data['text'].encode('utf-8'))

            download_aux_files(problem_data)

    store_json(times, json_times)
    write_readme(curr_path, times)

    if changes:
        offline(links, domain, curr_path)


if __name__ == '__main__':
    main()
