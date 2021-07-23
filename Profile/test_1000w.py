import profile

def fun():
    for i in range(10000000):
        pass
    

if __name__ == '__main__':
    profile.run('fun()')