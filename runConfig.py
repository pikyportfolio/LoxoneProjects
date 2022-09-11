#Search the Loxone folder to find the versions of all executables, select a version and run it
import os
from win32api import GetFileVersionInfo, LOWORD, HIWORD
import inquirer





#Get the user to input the Loxone folder directory
#Example directory C:\Program Files (x86)\Loxone


def scanPath(path):
    #Search for the executables named LoxoneConfig.exe
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith((".exe")):
                ...           #Will need for the language selector  

    #After finding the .exe take it's path and add it to the list
    exefiles = [os.path.join(root, name)
                for root, dirs, files in os.walk(path)
                for name in files
                if name.endswith(("LoxoneConfig.exe"))]
    return exefiles


#Get the file version
def get_version_number(filename):
    try:
        info = GetFileVersionInfo (filename, "\\")
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)
    except:
        return "Unknown version"


#Create a dictionary with value:path pair

version_file_dict = {} 
def createDict(pathList):
    versionsList = []
    
    for files in pathList:
        version = ".".join([str (i) for i in get_version_number (files)])
        versionsList.append(version)
        version_file_dict.update({f"{version}": f"{files}"})

    return  [versionsList,version_file_dict]

#createDict()
versionsList = [key for key in version_file_dict.keys()]



#Grab the version keys from the dict so they can select
versionsList = [key for key in version_file_dict.keys()]


# Don't need  if we are running TkInter
# questions = [
#   inquirer.List('selectVersion',
#                 message="Which version do you want to run?",
#                 choices= version_file_dict           ),
# ]

# #Once selected, grab the value and execute
# answers = inquirer.prompt(questions)
# selectedVersion = answers["selectVersion"]


#Run the selected version
# open only upon RUN os.popen(version_file_dict[selectedVersion])