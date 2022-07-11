# import json, time



# # with open('info.json', 'w') as f:
# #     json.dump({'time': time.time()}, f)

# # time.sleep(5)

# with open('info.json', 'r') as f:
#     info = json.load(f)


# interval = int(time.time() - info['time'])
# print(interval, type(interval))


import os
print(os.path.join(os.getcwd(), 'info.json'))
cwd = "/function/"
print(os.path.join(cwd, 'info.json'))