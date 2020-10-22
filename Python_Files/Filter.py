import pandas as pd # read CSV file
import matplotlib.pyplot as plt

df = pd.read_excel("Data Master File from M.O.L.E.xlsx")
#a1lt = df["A1LT"]
#print(df.head)

#print(df.shape)

'''
booleans = []
a1lt = pd.Series(booleans)
a1lt = df.A1LT >= 35
print(a1lt)
'''

#production settings
a1lt = df["A1LB"]
a1lb = df["A1LB"]
a2lt = df["A2LT"]
a2lb = df["A2LB"]
a3lt = df["A3LT"]
a3lb = df["A3LB"]
a1rt = df["A1RT"]
a1rb = df["A1RB"]
a2rt = df["A2RT"]
a2rb = df["A2RB"]
a3rt = df["A3RT"]
a3rb = df["A3RB"]

mylist = []
for i in a1lt:
    if i >= 80:
        mylist.append(i)
a1lt = mylist


'''
#arm position and loose tray
a1lt2 = df["A1LT2"]
a1lb2 = df["A1LB2"]
a2lt2 = df["A2LT2"]
a2lb2 = df["A2LB2"]
a3lt2 = df["A3LT2"]
a3lb2 = df["A3LB2"]
a1rt2 = df["A1RT2"]
a1rb2 = df["A1RB2"]
a2rt2 = df["A2RT2"]
a2rb2 = df["A2RB2"]
a3rt2 = df["A3RT2"]
a3rb2 = df["A3RB2"]
'''
#Thermocouple in the top of the moulds with production settings
#plt.subplot(1, 2, 1)
plt.plot(a1lt, "violet", linewidth=1, label = "a1lt_production")
#plt.plot(a1rt, "turquoise", linewidth=1, label = "a1rt_production")
#plt.plot(a2lt, "peru", linewidth=1, label = "a2lt_production")
#plt.plot(a2rt, "thistle", linewidth=1, label = "a2rt_production")
#plt.plot(a3lt, "seagreen", linewidth=1, label = "a3lt_production")
#plt.plot(a3rt, "purple", linewidth=1, label = "a3rt_production")
plt.title("Production Settings")
plt.suptitle("Balloon Length Failure Investigation")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
figure = plt.gcf()
figure.set_size_inches(20, 10)
plt.savefig("101", dpi=100)
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show(block=False)
plt.pause(5)
plt.close("all")
'''
#Thermocouple in the top of the moulds with modifications
plt.subplot(1, 2, 2)
plt.plot(a1lt2, "c--", linewidth=1, label = "a1lt2_loose tray_arm pos")
plt.plot(a1rt2, "b--", linewidth=1, label = "a1rt2_loose tray_arm pos")
plt.plot(a2lt2, "r--", linewidth=1, label = "a2lt2_loose tray")
plt.plot(a2rt2, "g--", linewidth=1, label = "a2rt2_loose tray")
plt.plot(a3lt2, "m--", linewidth=1, label = "a3lt2_loose tray")
plt.plot(a3rt2, "y--", linewidth=1, label = "a3rt2_loose tray")
plt.title("Modified Settings")
plt.suptitle("Balloon Length Failure Investigation")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
figure = plt.gcf()
figure.set_size_inches(20, 10)
plt.savefig("101", dpi=100)
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show(block=False)
plt.pause(5)
plt.close("all")

#Thermocouple in the bottom of the moulds with production settings
plt.subplot(1, 2, 1)
plt.plot(a1lb, "violet", linewidth=1, label = "a1lb_production")
plt.plot(a1rb, "turquoise", linewidth=1, label = "a1rb_production")
plt.plot(a2lb, "peru", linewidth=1, label = "a2lb_production")
plt.plot(a2rb, "thistle", linewidth=1, label = "a2rb_production")
plt.plot(a3lb, "seagreen", linewidth=1, label = "a3lb_production")
plt.plot(a3rb, "purple", linewidth=1, label = "a3rb_production")
plt.title("Production Settings")
plt.suptitle("Balloon Length Failure Investigation")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
figure = plt.gcf()
figure.set_size_inches(20, 10)

#Thermocouple in the bottom of the moulds with modifications
plt.subplot(1, 2, 2)
plt.plot(a1lb2, "c--", linewidth=1, label = "a1lb2_loose tray_arm pos")
plt.plot(a1rb2, "b--", linewidth=1, label = "a1rb2_loose tray_arm pos")
plt.plot(a2lb2, "r--", linewidth=1, label = "a2lb2_loose tray")
plt.plot(a2rb2, "g--", linewidth=1, label = "a2rb2_loose tray")
plt.plot(a3lb2, "m--", linewidth=1, label = "a3lb2_loose tray")
plt.plot(a3rb2, "y--", linewidth=1, label = "a3rb2_loose tray")
plt.title("Modified Settings")
plt.suptitle("Balloon Length Failure Investigation")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
figure = plt.gcf()
figure.set_size_inches(20, 10)
plt.savefig("102", dpi=100)
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show(block=False)
plt.pause(5)
plt.close("all")
'''