import sys
randomlist=['a',0,2]
for a in randomlist:
    try:
        print("Entry is ", a)
        r=1/int(a)
        break
    except:
        print("Oops! ",sys.exc_info()[0],"occured")
        print("Next entry")


