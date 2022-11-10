import time
bicycles = ['trek', 'cannondale', 'redline', 'specialized']


def showitems(args):
    time.sleep(5)
    for item in args:
        if item == 'redline':
            print(item.lower())
        elif item == 'trek':
            print(item.upper())
        else:
            print(item.title())
start = time.time()
print("Start:{0}".format(start))
showitems(bicycles)
end = time.time()
print("End:{0}".format(end))
run = end - start
print("run_time:{0}".format(run))