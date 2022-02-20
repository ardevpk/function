import os

files = os.popen('find . -type f -name "*.log"').read().split('\n')[0:-1]
files1 = os.popen('find . -type f -name "*.log.1"').read().split('\n')[0:-1]
for count, file in enumerate(files):
    print(f"{count}: {file}")
    if os.path.exists(file) and os.path.splitext(file)[-1] == '.log':
        os.remove(file)
        print(f"File removed: {file}")
    else:
        print(f"File not removed: {file}")
for count, file in enumerate(files1):
    print(f"{count}: {file}")
    print(f"{count}: {file}")
    if os.path.exists(file) and '.log.1' in file.split('/')[-1]:
        os.remove(file)
        print(f"File removed: {file}")
    else:
        print(f"File not removed: {file}")
