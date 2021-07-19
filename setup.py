from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='PyCA',
    url='https://github.com/atypic/pyca',
    author='Odd Rune',
    author_email='oddrunesl@gmail.com',
    # Needed to actually package something
    packages=['pyca'],
    # Needed for dependencies
    install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.2',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)