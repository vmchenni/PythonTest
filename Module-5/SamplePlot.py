import  matplotlib.pyplot as plt

applePrice=[10,20,30,40]
print(type(applePrice))
googlePrice=[60,70,80,90]
Year=[2015,2016,2017,2018]
plt.plot(Year,applePrice,'k',
         Year,googlePrice,'g')
# plt.plot(Year,googlePrice)
plt.xlabel='Year'
plt.ylabel='Price'
# plt.axis([(min(Year)-10), max(Year),( min(applePrice)-10), max(googlePrice)])
plt.grid(True)
plt.plot();
plt.show()
