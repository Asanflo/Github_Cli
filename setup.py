from setuptools import setup, find_packages

setup(
    name='github_api',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'click'
    ],
    entry_points={
        'console_scripts': [
            'github = github_api.cli:cli',
        ],
    },
    python_requires='>=3.6',
    author='Asanflo',
)