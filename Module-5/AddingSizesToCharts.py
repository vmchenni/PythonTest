import matplotlib.pyplot as plt

applePrice=[10,20,30,40]
googlePrice=[60,70,80,90]
Year=[2015,2016,2017,2018]
fig_1=plt.figure(1,figsize=(20,4.8))
chart_1=fig_1.add_subplot(121)
chart_2=fig_1.add_subplot(122)

chart_1.plot(Year,applePrice)
plt.show()
