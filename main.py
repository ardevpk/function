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
files = os.popen('find . -type f -name "*.log"').read()[0:-1]
for count, file in enumerate(str(files)):
    print(f"{count}: {file}")
