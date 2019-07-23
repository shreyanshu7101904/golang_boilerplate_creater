from pexpect import __version__
from colorama import Fore, Back

from libs import GoDirectoryGenerator


__doc__ = """

            .-'''-.                                                       .-'''-.        .-'''-.          
           '   _    \            .---.                                   '   _    \     '   _    \  .---. 
         /   /` '.   \           |   |.--./|                           /   /` '.   \  /   /` '.   \ |   | 
  .--./).   |     \  '           |   ||__|||                          .   |     \  ' .   |     \  ' |   | 
 /.''\\ |   '      |  '          |   |.--.||                       .| |   '      |  '|   '      |  '|   | 
| |  | |\    \     / /           |   ||  |||  __                 .' |_\    \     / / \    \     / / |   | 
 \`-' /  `.   ` ..' /            |   ||  |||/'__ '.            .'     |`.   ` ..' /   `.   ` ..' /  |   | 
 /("'`      '-...-'`             |   ||  ||:/`  '. '          '--.  .-'   '-...-'`       '-...-'`   |   | 
 \ '---.                         |   ||  |||     | |             |  |                               |   | 
  /'""'.\                        |   ||__|||\    / '             |  |                               |   | 
 ||     ||                       '---'    |/\'..' /              |  '.'                             '---' 
 \'. __//                                 '  `'-'`               |   /                                    
  `'---'                                                         `'-'                                     

"""
__version__ = "0.0.2"

if __name__ == '__main__':
    print("Version ", __version__)
    print(Fore.CYAN + __doc__ + Fore.RESET)
    GoDirectoryGenerator.directoryGenerator()