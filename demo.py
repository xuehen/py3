
##################列表#######################################
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

#修改/添加/删除元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
def m(args):
    bicycles[0] = 'kert'
    print(args)
def a(args):
    args.append('Dog')
    args.insert(2, 'insert')
    print(args)
def d(args):
    del args[1]
    print(args)
    args.pop()  #默认最后一个元素,指定索引即可删除指定索引的元素,删除的元素需要使用
    args.remove('redline') #只能删除第一次出现的值,若要删除其他重复的值使用循环
    print(args)

m(bicycles)
a(bicycles)
d(bicycles)

#排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
def e(args):
    args.sort()   #对列表按字母永久性排序
    print(args)
    args.sort(reverse=True)   #永久性方向排序
    print(args)
    print(len(args))
e(cars)



