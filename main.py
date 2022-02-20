import glob
import os

# cwd = os.getcwd()
# cwd = "D:"
# cwdfiles = os.listdir()

# logList = glob.glob(cwd + "/**/*.txt", recursive = True)
# for file in logList:
#     print(file)
# def delete():
#     logList = glob.glob(cwd + "/**/*.log", recursive = True)
#     for file in logList:
#         print(file)



# def main():
#     print(cwd)
#     print(cwdfiles)
#     print(delete())

# main()
# delete()
# var = os.system('find . -type f -name "*.txt"')
var = os.system('find -L / -name "*.txt"')
print(var)
