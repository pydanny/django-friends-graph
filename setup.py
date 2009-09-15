from setuptools import setup, find_packages
 
version = '0.1.0'
 
LONG_DESCRIPTION = """
=====================================
django-friends-graph
=====================================
"""
 
setup(
    name='django-friends-graph',
    version=version,
    description="Maps relationships",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='django,pinax',
    author='Daniel Greenfeld',
    author_email='pydanny@gmail.com',
    url='http://github.com/pydanny/django-friends-graph/tree/master',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
    setup_requires=['setuptools_git'],
)