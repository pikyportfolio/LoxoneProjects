#Create a simple and clean GUI with TkInter

import tkinter as tk
from tkinter import *         # import more than we need, import the important files later 


#root - is just the name of the window given, as it's the root of the GUI

root = tk.Tk()

root.title("Loxone Version Launcher")
root.geometry("500x300")

#Use the version list created by the get_versions func from runConfig
versions = ["Release","Beta", "Alpha"]
selectedVersion = tk.StringVar(root)
selectedVersion.set("Select a version")

#Creating objects and placing them - usually using pack or grit attributes

##Pass the parent object first aka root, give it text, font and size 

#Createa a frame(container) for the buttons, text etc inside a grid, same way as grid in css

browseFrame = tk.Frame(root)

#For object in the frame inherit from frame not root

label = tk.Label(browseFrame, text= "Select your Loxone folder to scan for Config versions:",font =('Arial', 12))   
browseTextbox = tk.Text(browseFrame,height= 2, width=50,  font =('Arial, 10'))
browseButton = tk.Button(browseFrame,text= "Browse", font= ("Arial, 14"))

label.grid(row=0, column = 0)
browseTextbox.grid(row = 1, column = 0, sticky = "we")           #sticky from west to east left to right 
browseButton.grid(row =1 , column= 1, sticky = "we")

#pack the frame to next item  to display everything made inside of it
browseFrame.pack(padx= 10,pady =50)

versionSelector =tk.OptionMenu(root,selectedVersion,*versions)
versionSelector.config(width=60, height=1, font =("Arial",12),)
versionSelector.pack(padx =20, pady =1 )

launchButton = tk.Button(root, text = "Launch",font =("Arial,16"))
launchButton.pack(pady= 30)




root.mainloop()



