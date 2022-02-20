import glob
import os

cwd = os.getcwd()
# cwdfiles = os.listdir()

def delete():
    logList = glob.glob(cwd + "/**/*.log", recursive = True)
    for file in logList:
        print(file)



# def main():
#     print(cwd)
#     print(cwdfiles)
#     print(delete())

# main()
delete()