import time
from colorama import Fore, Back, Style
import pyfiglet
import click
import os
import sys

def animationGenerator(text):
    if text:
        print (Fore.RED  + text)
    else:    
        animation = "|/-\\"
        idx = 0
        while True:
                print (Fore.CYAN  + animation[idx % len(animation)] + "\r", end="")
                idx += 1
                time.sleep(0.1)

def animationAsciiTextGenerator(text):
    result = pyfiglet.figlet_format(text, font = "isometric1")
    print(Fore.CYAN + result)

def createDirectoryStructure(username, repo):
    try:    
        os.mkdir("bin")
        temp = "src/github.com/"+ username + "/"+ repo
        os.makedirs(temp)
    except FileExistsError:
            animationGenerator("Directory Already Exists !!! ")
            animationGenerator("Exited !!!")


@click.command()
@click.option('--d', default=None, help='parent directory name')
@click.option('--u', default="User", help='github username')
@click.option('--r', default='abc', help='github repository name')
def countvalue(d, u, r):
    if d is None:
        createDirectoryStructure(u, r)
    else:
        os.chdir(d)
        createDirectoryStructure(u, r)


if __name__ == '__main__':
    # animationAsciiTextGenerator("GO") /home/getmyuni/Music/github
    # animationGenerator()
    countvalue()