from distutils.core import setup
setup(
    name='easyopts',
    packages=['easyopts'],
    version='0.1',
    license='MIT',
    description='Stupid simple command-line options parsing for Python 3',
    author='Nishant George Agrwal',
    author_email='nishant.george@hashedin.com',
    url='https://github.com/nishantgeorge/easyopts',
    download_url='https://github.com/nishantgeorge/easyopts/archive/0.1.tar.gz',
    keywords=['arguments', 'command-line', 'parsing'],
    install_requires=[],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 4 - Beta',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
