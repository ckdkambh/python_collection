def JPQ(length, times):
    count = length
    result = 0
    while count >= 1:
        result = (result + times)%count
        print('f(%d):%d'%(count, result))
        count = count - 1

if __name__=="__main__":
    JPQ(7, 3)