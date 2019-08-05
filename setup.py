import os
import re

from setuptools import find_packages, setup


def read(f):
    return open(f, 'r', encoding='utf-8').read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('swagger_render')


setup(
    name='django-swagger-render',
    version=version,
    license='MIT',
    description='Swagger documentation in Django',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Emir Amanbekov',
    author_email='amanbekoff@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.5",
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
    ],
    project_urls={
        'Source': 'https://github.com/eamanbekov/django-swagger-render',
    },
)
