#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
Generate the python files for the problems from ProjectEuler.net, download a
off-line copy of the Project Euler's website and calculate the times consumed
by each solution. Finally writes a README.md file with a summary.
"""

__author__ = "joe di castro <joe@joedicastro.com>"
__license__ = "GNU General Public License version 3"
__date__ = "21/04/2013"
__version__ = "0.2"

try:
    import json
    import os
    import sys
    from collections import defaultdict
    from itertools import izip
    from re import findall
    from subprocess import check_output
    from time import time
    from urllib import urlretrieve
    from urlparse import urlparse, urljoin

    from lxml.html import fromstring, parse
    from lxml.html.clean import Cleaner
except ImportError:
    # Checks the installation of the necessary python modules
    print((os.linesep * 2).join(["An error found importing one module:",
          str(sys.exc_info()[1]), "You need to install it", "Stopping..."]))
    sys.exit(-2)


try:
    import ghost
    GHOST = True
except ImportError:
    GHOST = False
GHOST = False


def get_element_et_links(url):
    """Get the lxml element.

    :url: the webpage url
    :returns: the cleaned lxml element and all the webpage links

    """

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


def clean_element(element):
    """Remove unnecessary tags from the lxml element.

    :element: the lxml element
    :returns: the cleaned lxml element

    """
    tags = ['var', 'br', 'i', 'font', 'small', 'span', 'b']
    cleaner = Cleaner(style=False, safe_attrs_only=False, remove_tags=tags)
    return cleaner.clean_html(element)


def get_web_content(element):
    """Extract the problem's information from the webpage using xpath.

    :element: the lxml element
    :returns: a iterator with title and content for each problem & total number

    """
    titles = element.xpath('//*[@id="content"]/h3/a')
    contents = element.xpath('//*[@class="problem_content"]')
    return izip(titles, contents), len(titles)


def get_problem_data(title, url_base, problems_path):
    """Extract the problem's information from the web content.

    :title: the problem's title (lxml.html.HtmlElement)
    :url_base: the website's url
    :problems_path: the path where the problems will be stored
    :returns: a dictionary with the problem's information

    """
    problem_et_number, problem_title = title.text.split(':', 1)
    problem_url = url_base + title.attrib['href']
    problem_number = '{0:03d}'.format(int(problem_et_number.split()[1]))
    problem_path = os.path.join(problems_path, problem_number)
    problem_file = os.path.join(problem_path, problem_number + '.py')

    return {'dir': problem_path, 'file': problem_file, 'url': problem_url,
            'title': problem_title[1:], 'number': problem_number,
            'problem': problem_et_number}


def get_problem_formulation(problem_content, url):
    """Get the problem's text content and adapt it for use it as the problem's
    formulation in the python files as a comment string.

    :problem_content: the problem's content (lxml.html.HtmlElement)
    :url: the website's url
    :returns: the problem's formulation in Unicode (utf8) & the auxiliary files
    to download

    """
    # some superscript and subscript alphabet characters are not supported in
    # the Unicode standard. More info at
    # http://en.wikipedia.org/wiki/Unicode_subscripts_and_superscripts
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
    for elm in problem_content.iter():
        if elm.tag in ('p', 'div'):
            if 'text-align:center' in elm.get('style', '') and elm.text:
                elm.text = '\n'.join(u'    {0}'.format(l) for
                                     l in elm.text.split('\n'))

        elif elm.tag == 'sup':
            elm.text = u''.join([superscript.get(l, u'^{0}'.format(l)) for
                                l in elm.text])

        elif elm.tag == 'sub':
            elm.text = u''.join([subscript.get(l, u'_{0}'.format(l)) for
                                l in elm.text])

        elif elm.tag == 'img':
            alt, src = elm.get('alt'), elm.get('src').split('/')
            tail = elm.tail
            elm.clear()
            elm.text, elm.tail = src[-1] if src[0] == 'project' else alt, tail
            if src[0] == 'project':
                to_download.append(url + '/'.join(src))

        elif elm.tag == 'a':
            href = elm.get('href').split('/')
            if href[0] == 'project':
                to_download.append(url + '/'.join(href))
            elm.text = '<{0}>'.format(elm.text)

        elif elm.tag == 'dfn':
            elm.text = u'{0} ({1})'.format(elm.text, elm.get('title'))

    return problem_content.text_content().replace('\r\n', '\n'), to_download


def write_script_et_aux(content, problem_info, url):
    """Write the script & download the auxiliary files to resolve the problem.

    :content: the problem's content
    :problem_info: problem's information dictionary
    :url: the website's url

    """

    problem_formulation, aux_files = get_problem_formulation(content, url)

    script_text = u'''
    #!/usr/bin/env python2
    # -*- coding: utf8 -*-

    """
    {0}
    {1}
    {2}

    {3}
    """


    '''.format(problem_info['title'],
               problem_info['problem'],
               problem_info['url'],
               problem_formulation).replace('    ', '').lstrip().encode('utf8')

    with open(problem_info['file'], 'w') as output:
        output.write(script_text)

    for fil in aux_files:
        filename = os.path.join(problem_info['dir'], fil.split('/')[-1])
        if not os.path.exists(filename):
            urlretrieve(fil, filename)


def offline(links, url, web_path):
    """Download an off-line copy of the Euler Project's website

    :links: the links of files to download
    :url: the website's url
    :web_path: the path where to store the off-line copy

    """
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


def get_processor_info():
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
    """A list of all the solution python scripts grouped by problems' numbers.

    :files: a list with files (under the git repository)
    :returns: a list of python scripts grouped by problem number

    """
    scripts = defaultdict(list)
    for fil in files:
        if os.path.splitext(fil)[-1] == '.py':
            key = os.path.basename(os.path.dirname(fil))
            scripts[key].append(fil)
    return scripts


def read_json(json_file):
    """Read the data stored in a json file.

    :json_file: the json file
    :returns: the data stored in the json file

    """
    with open(json_file, 'r') as json_in:
        json_data = json.load(json_in)
    return json_data


def store_json(times, json_file):
    """Store the consumed times in a json file with a human readable format.

    :times: the information about the time consumed by script & processor info
    :json_file: the json file where to store the information

    """
    with open(json_file, 'w') as json_out:
        json.dump(times, json_out, indent=4)


def initialize_times(processor, json_file):
    """Load the times dictionary from the json file or create it from scratch.

    :processor:  the processor info
    :json_file: the json file with the times & processor information stored
    :returns: the times dict & the flag for compute all scripts if the json
    file not exists or the processor had changed

    """
    compute_all_scripts = False
    if os.path.exists(json_file):
        times = read_json(json_file)
        if times['processor'] != processor:
            times['processor'] = processor
            compute_all_scripts = True
    else:
        times = defaultdict(dir)
        times['processor'] = processor
        compute_all_scripts = True
    return compute_all_scripts, times


def get_time(script, problem_dir):
    """Gets the time taken to execute a script.

    :problem: the python script used to solve a problem
    :problem_dir: the directory where the script is
    :returns: the time taken to execute the script

    """
    os.chdir(problem_dir)
    start_time = time()
    if check_output('python2 {0}'.format(script).split()):
        stop_time = time()
    return stop_time - start_time


def get_times(scripts, problem_info, times):
    """Get the times taken to solve a problem per script.

    :scripts: the python scripts
    :problem_info: the problem information
    :times: the dictionary (defaultdict) where to store the results

    """
    key = problem_info['number']
    for script in scripts[problem_info['number']]:
        script_name = os.path.basename(script)
        time_taken = get_time(script, problem_info['dir'])
        if not times.get(problem_info['number'], {}):
            times[key] = {script_name: time_taken}
        else:
            times[key][script_name] = time_taken


def mark_time(time_to_mark):
    """Mark the time in function to my goal (less than 10s).

    :time_to_mark: the time to mark_time
    :returns: the time string formated according to the criteria

    """
    if time_to_mark < 10:
        mark_sign = '✓'
    elif 10 < time_to_mark < 30:
        mark_sign = '⚠'
    else:
        mark_sign = '✕'

    return '{0:3f}s {1}'.format(time_to_mark, mark_sign)


def write_readme(curr_path, times, total):
    """Write the README.md document.

    :curr_path: the path where to store the README.md file
    :times: the times consumed by script grouped by problem num
    :total: the total num of problems

    """
    os.chdir(curr_path)
    solved = len(times) - 1

    header = '''
    # Project Euler Solutions

    ![profile](http://projecteuler.net/profile/joedicastro.png)

    ## About Project Euler

    [Project Euler](http://projecteuler.net/) is a website to challenge
    mathematicians and programmers with mathematical problems intended to help
    you to improve your mathematical and programming skills.

    Extracted from [Wikipedia](http://en.wikipedia.org/wiki/Project_Euler):

    > Project Euler (named after Leonhard Euler) is a website dedicated to a
    series of computational problems intended to be solved with computer
    programs. The project attracts adults and students interested in
    mathematics and computer programming. It includes over 400 problems, with a
    new one added every weekend. Problems are of varying difficulty but each is
    solvable in less than a minute using an efficient algorithm on a modestly
    powered computer.

    ## About this repository

    There is my attempt to solve some problems of this project, using the
    python language. The target is to solve as many as I can, and keep the time
    consumed by each script below 30 second at a minimum and preferably below
    10s.

    ### Contents:

    - directories from `$ ls -d [0-9][0-9][0-9]`: contains the python script(s)
      with the solution and the auxiliary files needed to solve them. Sometimes
      I have more than one solution to the same problem.
    - `README.md`: this document
    - `times.json`: the time taken to solve each script stored in json format
    - `update.py`: an utility script to automatize some tasks:

      - Downloads an off-line copy of the Project Euler's website with all the
       problems in a single page.

      - Creates this document automatically, computing the solved problems to
       know the time consumed by each solution.

       - Creates a new dir locally for each problem (new problems also),
       downloads automatically all the necessary auxiliary files and create a
       new python file with the problem's formulation as the document string.

         This is an example of a created python file for this script:

    ```python
    #!/usr/bin/env python2
    # -*- coding: utf8 -*-

    """
    Special Pythagorean triplet
    Problem 9
    http://projecteuler.net/problem=9

    A Pythagorean triplet is a set of three natural numbers, a < b < c, for
    which, a² + b² = c²

    For example, 3² + 4² = 9 + 16 = 25 = 5².

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    ```



    ## About Cheating

    Don't cheat! If you cheat, you only fool yourself! If you can't do it, you
    can not do it, that's all! Almost you tried, and if you keep learning and
    studying, maybe one day you can solve those problems that seemed so hard a
    few early.

    Be proud of what you have achieved instead, even if is little. Especially
    if your math skills or education is not so vast (as in my case). I'm very
    proud to have solved all of this problems without cheating or copy another
    else's solutions. That's the right attitude.

    But, once you have a solution, you can learn a lot from the solutions of
    others. That's the purpose of the Project Euler's forum and it's fine.
    That's the main purpose of this repository too. Maybe you couldn't learn a
    lot from my solutions, maybe even you can laugh of the most naive ones, but
    doesn't matter, be humble and remember that even the most idiot can teach
    you always something. The second purpose is to have a online backup of this
    code, some problems were hard to break and I would hate to loose this code.

    __The most important thing isn't the Project Euler's rank that you achieve
    or the number of problems that you solved, the most important thing is what
    you have learned in the process!__


    ## Solved Problems

    Times computed in a {0} processor.\n

    Solved {1} out of {2} problems

    '''.format(times['processor'], solved, total).replace('    ', '').lstrip()

    body = ''
    for num in sorted(times):
        if times[num] and num != 'processor':
            body += ('### Problem {0}\n\n'.format(num))
            for sol in sorted(times[num].keys()):
                weighted_time = mark_time(times[num][sol])
                body += ('    {0:12} {1}\n\n'.format(sol, weighted_time))

    with open('README.md', 'w') as doc:
        doc.write(header)
        doc.write(body)


def main(changes=False):
    """The main function."""
    current_path = os.getcwd()
    json_times = os.path.join(current_path, 'times.json')

    domain = 'http://projecteuler.net/'
    url = domain + 'show=unsolved'

    element, links = get_element_et_links(url)
    web_content, problems_count = get_web_content(element)

    processor = get_processor_info()
    compute_all, times = initialize_times(processor, json_times)

    git_files = scripts_per_problem(get_git_files(current_path))
    git_staged = scripts_per_problem(get_git_files(current_path, True))

    for title, content in web_content:
        problem_data = get_problem_data(title, domain, current_path)

        if not os.path.exists(problem_data['dir']):
            os.mkdir(problem_data['dir'])
            changes = True
        else:
            if compute_all:
                get_times(git_files, problem_data, times)
            else:
                get_times(git_staged, problem_data, times)

        if not os.path.exists(problem_data['file']):
            write_script_et_aux(content, problem_data, domain)

    store_json(times, json_times)
    write_readme(current_path, times, problems_count)

    web_path = os.path.join(current_path, 'web')
    if not os.path.exists(web_path) or changes:
        try:
            os.mkdir(web_path)
            offline(links, domain, web_path)
        except OSError:
            offline(links, domain, web_path)


if __name__ == '__main__':
    main()


###############################################################################
#                                  Changelog                                  #
###############################################################################
#
# 0.2:
#
# * Download also the non-image auxiliary files
#
# 0.1:
#
# * First attempt
#
