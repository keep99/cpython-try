import json
import profile

def fun():
    data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

    dataList = []
    for i in range(1000000):
        dataList.append(data)

    data2 = json.dumps(data)
    # print(data2)

if __name__ == '__main__':
    profile.run('fun()')