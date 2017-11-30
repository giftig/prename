from setuptools import setup

setup(
    name='prename',
    version='1.0.0',
    description='Simple CLI tool for enacting regex renames',
    author='Rob Moore',
    author_email='giftiger.wunsch@xantoria.com',
    packages=['prename'],
    entry_points={
        'console_scripts': [
            'prename = prename.prename:entrypoint'
        ]
    }
)
