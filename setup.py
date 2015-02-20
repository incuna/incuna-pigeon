from setuptools import setup, find_packages


setup(
    name='incuna-pigeon',

    version='0.0.0',

    description='Notification management',
    url='https://github.com/incuna/incuna-pigeon',
    author='Incuna',
    author_email='admin@incuna.com',
    license='BSD',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Communications',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='notifications',
    packages=find_packages(),
)
