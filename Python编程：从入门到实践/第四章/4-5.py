import datetime

def testRunTime():
    start = datetime.datetime.now()
    number = [] 
    number = [i for i in range(1,1000001)]
    print(sum(number))
    end = datetime.datetime.now()
    print(end - start)
    return

if __name__ == "__main__":
    testRunTime()