from pexpect import __version__

from libs import GoDirectoryGenerator

__version__ = "0.0.1"

if __name__ == '__main__':
    print("Version ", __version__)
    GoDirectoryGenerator.directoryGenerator()