import setuptools

setuptools.setup(
    name="autofire",
    version="0.0.2",
    author="Sergey Slotin",
    author_email="me@sereja.me",
    description="CLI for any Python program",
    url="https://github.com/sslotin/autofire",
    packages=['autofire'],
    install_requires=['fire'],
    entry_points={
        'console_scripts': [
            'fire = autofire.__main__:main'
        ]
    }
)
