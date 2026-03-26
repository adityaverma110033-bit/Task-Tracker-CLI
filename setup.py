from setuptools import setup

setup(
    name="task-cli",
    version="1.0",
    py_modules=["task_cli"],  # This must match your filename (task_cli.py)
    entry_points={
        'console_scripts': [
            # format: 'command-name = filename:function'
            'task-cli = task_cli:main',
        ],
    },
)