# importing files needed for file integration
import shutil
import git
import sys


# Defining varibles
basepath = 'C:\OBREvents'
defaultfold = basepath + '\\19_00_D_WHE'
year = '2019'
week = '02'
eventtype = 'T'
loc = 'blah'
gitpath = 'C:\\OBREvents'
repo = git.Repo(gitpath)
origin = repo.remote(name='origin')

# Pull from Git
def action1():
    try:
        origin.pull()
        return True
    except:
        return False


# Move files from default location and creates new folder
def action2():
    try:
        pathext = year[2:4] + '_' + week + '_' + eventtype[0:1] + '_' + loc[0:3].upper()
        newpath = basepath + '\\' + pathext
        shutil.copytree(defaultfold, newpath)
        return True
    except:
        return False


# Push new files to Git
def action3():
    try:
        pathext = year[2:4] + '_' + week + '_' + eventtype[0:1] + '_' + loc[0:3].upper()
        repo.git.add('--all')
        repo.index.commit('Creation of ' + pathext)
        origin.push()
        return True
    except:
        return False