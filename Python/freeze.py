try:
    from pip._internal.operations import freeze
except ImportError:  # if your pip version is bigger then 10
    from pip.operations import freeze

requirements = freeze.freeze()
for i in requirements:
    print(i)