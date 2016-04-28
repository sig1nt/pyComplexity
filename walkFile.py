import zipfile, os
from os import path
from buildScore import buildFile

for score in os.listdir('.'):
    os.chdir(path.join(os.getcwd(), score))
    for user in os.listdir('.'):
        os.chdir(path.join(os.getcwd(), user))
        buildFile(user, "Project 2")
        os.chdir('..')
    os.chdir('..')
