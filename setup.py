from setuptools import find_packages, setup


setup(
    name='incuna-pigeon',

    version='0.1.0',

    description='Notification management',
    url='https://github.com/incuna/incuna-pigeon',
    author='Incuna',
    author_email='admin@incuna.com',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Communications',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='notifications',
    packages=find_packages(),
    setup_requires=['wheel'],
)
