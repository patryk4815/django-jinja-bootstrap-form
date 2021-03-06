from setuptools import setup, find_packages
from bootstrapform_jinja.meta import VERSION

description = """
django-jinja-bootstrap-form
===========================

`github.com/samuelcolvin/django-jinja-bootstrap-form <https://github.com/samuelcolvin/django-jinja-bootstrap-form>`_

Port of `django-bootstrap-form <https://github.com/tzangms/django-bootstrap-form>`_
which is compatible with `django-jinja <https://github.com/niwibe/django-jinja>`_.

To install:

.. code-block:: shell

    pip install django-jinja-bootstrap-form
"""

setup(
    name='django-jinja-bootstrap-form',
    version=str(VERSION),
    description='django-jinja-bootstrap-form',
    long_description=description,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    keywords='bootstrap,django,jinja2',
    author='Samuel Colvin',
    author_email='s@muelcolvin.com',
    url='https://github.com/samuelcolvin/django-jinja-bootstrap-form',
    license='BSD',
    install_requires=[
        "django>=1.6",
        "django-jinja>=1.3.3",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
