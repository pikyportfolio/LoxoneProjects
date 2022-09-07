#Again we will ask for the directory of the def log 
#Later on create a drag and drop GUI

#filePath = input("Enter the DefLog file path")
# example:  D:\\myfiles\welcome.txt
# f = open("filePath", "r")

#Local dir
f = open("DefLog.txt")


#How this should work -pull the file, read it and parse the variable we need, reset,reboot etc
#select a date period between x and y and only pull the data if it's the correct date
#and it contains the correct information


def txtToList():
    with open('DefLog.txt') as f:
        lineList =[line for line in f.readlines()]
        return lineList

txtList = txtToList()

printLine = [l for l in txtList if "reset" in l]
#create new def log with less info
fn = open("SmallDefLog.txt","w")
fn.write("\n".join(printLine))
fn.close()
