import os
import re

from setuptools import find_packages, setup

regexp = re.compile(r'.*__version__ = [\'\"](.*?)[\'\"]', re.S)

base_package = 'game_collecting'
base_path = os.path.dirname(__file__)

init_file = os.path.join(base_path, 'src', 'game_collecting', '__init__.py')
with open(init_file, 'r') as f:
    module_content = f.read()

    match = regexp.match(module_content)
    if match:
        version = match.group(1)
    else:
        raise RuntimeError(
            'Cannot find __version__ in {}'.format(init_file))

with open('README.rst', 'r') as f:
    readme = f.read()

with open('CHANGELOG.rst', 'r') as f:
    changes = f.read()

def parse_requirements(filename):
    ''' Load requirements from a pip requirements file '''
    with open(filename, 'r') as fd:
        lines = []
        for line in fd:
            line.strip()
            if line and not line.startswith("#"):
                lines.append(line)
    return lines

requirements = parse_requirements('requirements.txt')


if __name__ == '__main__':
    setup(
        name='game_collecting',
        description='The ultimate game collecting manager.',
        long_description='\n\n'.join([readme, changes]),
        license='GNU Affero General Public License v3',
        url='https://github.com/boltronics/game-collecting',
        version=version,
        author='Adam Bolte',
        author_email='abolte@systemsaviour.com',
        maintainer='Adam Bolte',
        maintainer_email='abolte@systemsaviour.com',
        install_requires=requirements,
        keywords=['game_collecting'],
        package_dir={'': 'src'},
        packages=find_packages('src'),
        zip_safe=False,
        classifiers=['Development Status :: 2 - Pre-Alpha',
                     'Intended Audience :: End Users/Desktop',
                     'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
                     'Programming Language :: Python :: 3.8',
                     'Programming Language :: Python :: 3.9',
                     'Programming Language :: Python :: 3.10'
                     'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Content Management System']
    )
