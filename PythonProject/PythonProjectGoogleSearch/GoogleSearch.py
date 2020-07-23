import sys
try:
    from googlesearch import  search
except ImportError:
    print("No module named google found")
sQuery=""
for arg in sys.argv:
    sQuery=sQuery+" "+arg
query=sQuery
for i in search(query,tld='co.in', num=10, stop=10, pause=2):
    print(i)