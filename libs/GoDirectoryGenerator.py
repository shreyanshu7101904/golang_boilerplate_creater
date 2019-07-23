import time
from colorama import Fore, Back, Style
import pyfiglet
import click
import os
import sys

def animationGenerator(text= None):
    if text:
        print (Fore.RED  + text)
    else:    
        animation = "|/-\\"
        idx = 0
        while True:
                print (Fore.CYAN  + "Generating Directories" +animation[idx % len(animation)] + "\r", end="")
                idx += 1
                time.sleep(0.1)
                if idx ==5:
                        break

def animationAsciiTextGenerator(text):
    result = pyfiglet.figlet_format(text, font = "isometric1")
    print(Fore.YELLOW + result, end="")

def createDirectoryStructure(parent, username, repo):
    try:
            os.mkdir(parent)   
    except FileExistsError:
            pass    
    try:    
        os.mkdir(parent + "/bin")
        temp = parent + "/src/github.com/"+ username + "/"+ repo
        os.makedirs(temp)
        animationGenerator("Directory created at = "+ os.getcwd())
    except FileExistsError:
            animationGenerator("Directory Already Exists !!! ")
            animationGenerator("Exited !!!")


@click.command()
@click.option('--p', default="go", help='path for directory creation')
@click.option('--d', default=None, help='parent directory name')
@click.option('--u', default="User", help='github username')
@click.option('--r', default='abc', help='github repository name')
def directoryGenerator(p, d, u, r):
    animationAsciiTextGenerator("Go Lib Tool")    
    if d is None:
        animationGenerator()
        createDirectoryStructure(p, u, r)
    else:
        animationGenerator()
        os.chdir(d)
        createDirectoryStructure(p, u, r)
        


if __name__ == '__main__':
    directoryGenerator()