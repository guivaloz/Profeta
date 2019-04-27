from setuptools import setup

setup(
    name='Profeta',
    version='1.0',
    py_modules=['profeta'],
    install_requires=[
        'Click',
    ],
    entry_points="""
        [console_scripts]
        profeta=profeta:cli
    """,
)
