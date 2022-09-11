#Create a simple and clean GUI with TkInter

from cgitb import text
from multiprocessing.sharedctypes import Value
import tkinter as tk
from tkinter import *                   # import more than we need, import the important files later
from tkinter import filedialog      
from runConfig import *

#Globals
x = "Example Path: C:\Program Files (x86)\Loxone"
versions = ["No versions found"]
test_version = [1,2,3,4,5]

loxone_folder = ""
version_path = {}

#creating Functions

def browse_folder():
    loxone_folder = filedialog.askdirectory()
    pathLabel.config(text = f"Selected: {loxone_folder}")
    get_path_version_dict(loxone_folder)
    return loxone_folder

def get_path_version_dict(loxone_folder):
    global version_path
    version_path_list = createDict(scanPath(loxone_folder))
    versions = list(version_path_list[0])
    refresh_options(versions)
    versionSelector.configure()
    version_path = version_path_list[1]

    return print("Executed Succesfully, Select your version")

def refresh_options(newlist):
    # Reset var and delete all old options
    #selectedVersion.set('')
    versionSelector['menu'].delete(0, 'end')

    # Insert list of new options (tk._setit hooks them up to var)
    new_choices = newlist
    for choice in new_choices:
        versionSelector['menu'].add_command(label=choice, command=tk._setit(selectedVersion, choice))

def run_version():
    os.popen(version_path[selectedVersion.get()])
    return print(f"Launching version {selectedVersion} of Loxone Config.")









#root - is just the name of the window given, as it's the root of the GUI

root = tk.Tk()

root.title("Loxone Version Launcher")
root.geometry("500x300")

#Creating objects and placing them - usually using pack or grit attributes

##Pass the parent object first aka root, give it text, font and size 

#Createa a frame(container) for the buttons, text etc inside a grid, same way as grid in css

browseFrame = tk.Frame(root)

#For object in the frame inherit from frame not root

label = tk.Label(browseFrame, text= "Select your Loxone folder to scan for Config versions:",font =('Arial', 12))   
browseButton = tk.Button(browseFrame,text= "Browse", font= ("Arial, 14"),command= browse_folder)
pathLabel = tk.Label(browseFrame,text = x,font = ('Arial,',14))


label.grid(row=0, column = 0)
pathLabel.grid(row = 1, column = 0, sticky = "we")           #sticky from west to east left to right 
browseButton.grid(row =1 , column= 1, sticky = "we")

#pack the frame to next item  to display everything made inside of it
browseFrame.pack(padx= 10,pady =50)

#Use the version list created by the get_versions func from runConfig

selectedVersion = tk.StringVar(root)
selectedVersion.set("Select a version")

versionSelector =tk.OptionMenu(root,selectedVersion,*versions)
versionSelector.config(width=60, height=1, font =("Arial",12),)
versionSelector.pack(padx =20, pady =1 )


launchButton = tk.Button(root, text = "Launch",font =("Arial,16"),command = run_version)
launchButton.pack(pady= 30)




root.mainloop()



