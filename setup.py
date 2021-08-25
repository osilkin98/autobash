from setuptools import setup, find_packages

setup(
    name='autobash',
    version='0.1.0',
    author='Oleg Silkin',
    author_email='oxsilkin@gmail.com',
    license='MIT',
    description='Provides an autocompleted bash command using the provided user\'s input',
    python_requires='>=3.6',
    packages=find_packages(),
    install_requires=[
        'python-dotenv',
        'openai'
    ],
    entry_points={
        'console_scripts': [
            'autoshell = main:main',
        ],
    },
)