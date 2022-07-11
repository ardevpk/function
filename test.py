import json, time



# with open('info.json', 'w') as f:
#     json.dump({'time': time.time()}, f)

# time.sleep(5)

with open('./info.json', 'r') as f:
    info = json.load(f)


interval = int(time.time() - info['time'])
print(interval, type(interval))