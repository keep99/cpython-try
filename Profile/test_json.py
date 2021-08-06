import json
import profile

dataList = {}
def make_data():
    data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4.22, 'e' : "aaaa", "f" : [1,2,"444"]} ]

    
    for i in xrange(1000000):
        #dataList.append(data)
        dataList[i] = data


def foo2():
    data2 = json.dumps(dataList)
    # print(data2)

def foo():
    for i in xrange(100000000):
        pass
def foo2():
    i = 0
    while True:
        if i > 100000000:
            break
        i += 1
if __name__ == '__main__':
    make_data()
    #profile.run('foo()')
    import time
    import timeit
    re =  timeit.repeat(foo2, repeat = 3, number  = 1)
    print re, sum(re) /3