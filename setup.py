import os

from setuptools import find_packages, setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name='RailgunS',
    version='0.2',
    url='https://github.com/nyssance/railguns',
    author='NY',
    author_email='nyssance@icloud.com',
    description='Only My Railgun',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=[
        'django[argon2]',
        'djangorestframework',
        'djangorestframework_simplejwt',
        'drf-yasg[validation]',
        'stringcase',
        'uvicorn',
        #
        'django-ckeditor',
        'django-crispy-forms',
        'django-extensions',
        'django-filter',
        'django-htmlmin',
        'django-redis',
        'itunes-iap',
        'mysqlclient'
    ],
    extras_require={
        'dev': ['django-debug-toolbar-force', 'django-rosetta', 'markdown', 'pygments'],
        'prod': ['gunicorn']
    },
    python_requires='>=3.6',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP'
    ],
    project_urls={
        'Source': 'https://github.com/nyssance/railguns'
    })
