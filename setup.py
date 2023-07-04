from setuptools import setup

setup(
    name='jp_ex_py_env',
    version='0.1',
    py_modules=['jp_ex_py_env'],
    install_requires=[
        'notebook',
    ],
    data_files=[
        (
            'etc/jupyter/jupyter_notebook_config.d',
            ['jp_ex_py_env.json']
        ),
    ],
)