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
files = os.popen('find . -type f -name "*.log"').read().split('\n')[0:-1]
files1 = os.popen('find . -type f -name "*.log.1"').read().split('\n')[0:-1]
for count, file in enumerate(files):
    print(f"{count}: {file}")
for count, file in enumerate(files1):
    print(f"{count}: {file}")
