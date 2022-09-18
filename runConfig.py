#Search the Loxone folder to find the versions of all executables, select a version and run it
import os
from ctypes import *


#All the backend functions to get the scan the folders and get the versions


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

# returns the requested version information from the given file
#
# `language` should be an 8-character string combining both the language and
# codepage (such as "040904b0"); if None, the first language in the translation
# table is used instead
#
def get_version_string(filename, what, language=None):
    # VerQueryValue() returns an array of that for VarFileInfo\Translation
    #
    class LANGANDCODEPAGE(Structure):
        _fields_ = [
            ("wLanguage", c_uint16),
            ("wCodePage", c_uint16)]

    wstr_file = wstring_at(filename)

    # getting the size in bytes of the file version info buffer
    size = windll.version.GetFileVersionInfoSizeW(wstr_file, None)
    if size == 0:
        raise WinError()

    buffer = create_string_buffer(size)

    # getting the file version info data
    if windll.version.GetFileVersionInfoW(wstr_file, None, size, buffer) == 0:
        raise WinError()

    # VerQueryValue() wants a pointer to a void* and DWORD; used both for
    # getting the default language (if necessary) and getting the actual data
    # below
    value = c_void_p(0)
    value_size = c_uint(0)

    if language is None:
        # file version information can contain much more than the version
        # number (copyright, application name, etc.) and these are all
        # translatable
        #
        # the following arbitrarily gets the first language and codepage from
        # the list
        ret = windll.version.VerQueryValueW(
            buffer, wstring_at(r"\VarFileInfo\Translation"),
            byref(value), byref(value_size))

        if ret == 0:
            raise WinError()

        # value points to a byte inside buffer, value_size is the size in bytes
        # of that particular section

        # casting the void* to a LANGANDCODEPAGE*
        lcp = cast(value, POINTER(LANGANDCODEPAGE))

        # formatting language and codepage to something like "040904b0"
        language = "{0:04x}{1:04x}".format(
            lcp.contents.wLanguage, lcp.contents.wCodePage)

    # getting the actual data
    res = windll.version.VerQueryValueW(
        buffer, wstring_at("\\StringFileInfo\\" + language + "\\" + what),
        byref(value), byref(value_size))

    if res == 0:
        raise WinError()

    # value points to a string of value_size characters, minus one for the
    # terminating null
    return wstring_at(value.value, value_size.value - 1)



#Create a dictionary with value:path pair
version_file_dict = {} 
def createDict(pathList):
    versionsList = []
    
    for files in pathList:
        version = get_version_string (files,"FileVersion")
        versionsList.append(version)
        version_file_dict.update({f"{version}": f"{files}"})

    return  [versionsList,version_file_dict]


#createDict()
versionsList = [key for key in version_file_dict.keys()]

#Grab the version keys from the dict so they can select
versionsList = [key for key in version_file_dict.keys()]
