from setuptools import setup

setup(
    name='my_extension',
    version='0.1',
    py_modules=['my_extension'],
    install_requires=[
        'notebook',
    ],
    data_files=[
        (
            'etc/jupyter/jupyter_notebook_config.d',
            ['my_extension.json']
        ),
    ],
)