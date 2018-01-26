from setuptools import setup, find_packages
setup(
    name = "ganzhiwuxin",
    version = "0.1",
    packages = find_packages(),
    #packages = ['ganzhiwuxin'],
    #py_modules= ['ganzhiwuxin'],
    zip_safe = False,
    #scripts = ['ganzhiwuxin.py'],
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    #install_requires = ['docutils>=0.3'],
    #package_data = {
    #    # If any package contains *.txt or *.rst files, include them:
    #    '': ['*.txt', '*.rst'],
    #    # include any *.msg files found in the 'hello' package, too:
    #    'hello': ['*.msg'],
    #},
    # metadata for upload to PyPI
    author = "penguin",
    author_email = "1216083447@qq.com",
    description = "ganzhiwuxin",
    license = "gpl",
    keywords = "ganzhiwuxin",
    #url = "http://example.com/HelloWorld/",   # project home page, if any
    # could also include long_description, download_url, classifiers, etc.
)
