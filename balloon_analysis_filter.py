import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Data Master File from M.O.L.E.xlsx")

#production settings
a1lt = df["A1LT"]
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

#Arm1
mylist1 = []
for i in a1lt:
    if i >= 35:
        mylist1.append(i)
a1lt = mylist1

mylist2 = []
for i in a1lb:
    if i >= 35:
        mylist2.append(i)
a1lb = mylist2

mylist3 = []
for i in a1rt:
    if i >= 35:
        mylist3.append(i)
a1rt = mylist3

mylist4 = []
for i in a1rb:
    if i >= 35:
        mylist4.append(i)
a1rb = mylist4

#Arm2
mylist5 = []
for i in a2lt:
    if i >= 35:
        mylist5.append(i)
a2lt = mylist5

mylist6 = []
for i in a2lb:
    if i >= 35:
        mylist6.append(i)
a2lb = mylist6

mylist7 = []
for i in a2rt:
    if i >= 35:
        mylist7.append(i)
a2rt = mylist7

mylist8 = []
for i in a2rb:
    if i >= 35:
        mylist8.append(i)
a2rb = mylist8

#Arm3
mylist9 = []
for i in a3lt:
    if i >= 35:
        mylist9.append(i)
a3lt = mylist9

mylist10 = []
for i in a3lb:
    if i >= 35:
        mylist10.append(i)
a3lb = mylist10

mylist11 = []
for i in a3rt:
    if i >= 35:
        mylist11.append(i)
a3rt = mylist11

mylist12 = []
for i in a3rb:
    if i >= 35:
        mylist12.append(i)
a3rb = mylist12

#modified settings (arm position and loose tray)
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

#Arm1
mylist13 = []
for i in a1lt2:
    if i >= 35:
        mylist13.append(i)
a1lt2 = mylist13

mylist14 = []
for i in a1lb2:
    if i >= 35:
        mylist14.append(i)
a1lb2 = mylist14

mylist15 = []
for i in a1rt2:
    if i >= 35:
        mylist15.append(i)
a1rt2 = mylist15

mylist16 = []
for i in a1rb2:
    if i >= 35:
        mylist16.append(i)
a1rb2 = mylist16

#Arm2
mylist17 = []
for i in a2lt2:
    if i >= 35:
        mylist17.append(i)
a2lt2 = mylist17

mylist18 = []
for i in a2lb2:
    if i >= 35:
        mylist18.append(i)
a2lb2 = mylist18

mylist19 = []
for i in a2rt2:
    if i >= 35:
        mylist19.append(i)
a2rt2 = mylist19

mylist20 = []
for i in a2rb2:
    if i >= 35:
        mylist20.append(i)
a2rb2 = mylist20

#Arm3
mylist21 = []
for i in a3lt2:
    if i >= 35:
        mylist21.append(i)
a3lt2 = mylist21

mylist22 = []
for i in a3lb2:
    if i >= 35:
        mylist22.append(i)
a3lb2 = mylist22

mylist23 = []
for i in a3rt2:
    if i >= 35:
        mylist23.append(i)
a3rt2 = mylist23

mylist24 = []
for i in a3rb2:
    if i >= 35:
        mylist24.append(i)
a3rb2 = mylist24

#trials_all on arm 1 with different tray positions
trial1t = df["A1LTt1"]
trial1b = df["A1LBt1"]
trial2t = df["A1LTt2"]
trial2b = df["A1LBt2"]
trial3t = df["A1LTt3"]
trial3b = df["A1LBt3"]
trial4t = df["A1LTt4"]
trial4b = df["A1LBt4"]
trial5t = df["A1LTt5"]
trial5b = df["A1LBt5"]

#Thermocouple in the top of the moulds

#Arm 1 Left Top
#plt.figure(figsize=(20,10))
plt.plot(a1lt, color = "black", linewidth=1, label = "a1lt_production")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Top Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.savefig("1")
plt.show(block=False)
plt.pause(5)

#Arm 1 Right Top
#plt.figure(figsize=(20,10))
plt.plot(a1rt, color = "blue", linewidth=1, label = "a1rt_production")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Top Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("2")
plt.show(block=False)
plt.pause(5)

#Arm 2 Left Top
##plt.figure(figsize=(20,10))
plt.plot(a2lt, color = "red", linewidth=1, label = "a2lt_production")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Top Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("3")
plt.show(block=False)
plt.pause(5)

#Arm 2 Right Top
#plt.figure(figsize=(20,10))
plt.plot(a2rt, color = "grey", linewidth=1, label = "a2rt_production")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Top Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("4")
plt.show(block=False)
plt.pause(5)

#Arm 3 Left Top
#plt.figure(figsize=(20,10))
plt.plot(a3lt, color = "green", linewidth=1, label = "a3lt_production")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Top Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("5")
plt.show(block=False)
plt.pause(5)

#Arm 3 Right Top
#plt.figure(figsize=(20,10))
plt.plot(a3rt, color = "purple", linewidth=1, label = "a3rt_production")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Top Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("6")
plt.show(block=False)
plt.pause(5)
plt.close("all")

'''
#Top Trials

#Trial_1_Top
#plt.figure(figsize=(20,10))
plt.plot(trial1t, color = "violet", linewidth=1, label = "Trial1")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Top Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("7")
plt.show(block=False)
plt.pause(5)

#Trial_2_Top
#plt.figure(figsize=(20,10))
plt.plot(trial2t, color = "orange", linewidth=1, label = "Trial2")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Top Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("8")
plt.show(block=False)
plt.pause(5)

#Trial_3_Top
#plt.figure(figsize=(20,10))
plt.plot(trial3t, color = "pink", linewidth=1, label = "Trial3")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Top Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("9")
plt.show(block=False)
plt.pause(5)

#Trial_4_Top
#plt.figure(figsize=(20,10))
plt.plot(trial4t, color = "brown", linewidth=1, label = "Trial4")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Top Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("10")
plt.show(block=False)
plt.pause(5)

#Trial_5_Top
#plt.figure(figsize=(20,10))
plt.plot(trial5t, color = "indigo", linewidth=1, label = "Trial5")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Top Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("11")
plt.show(block=False)
plt.pause(5)
plt.close("all")
'''

#Thermocouple in the bottom of the mould

#Arm 1 Left Bottom
plt.figure(figsize=(20,10))
plt.plot(a1lb, color = "black", linewidth=1, label = "a1lb_production")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Bottom Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.savefig("12")
plt.show(block=False)
plt.pause(5)

#Arm 1 Right Bottom
#plt.figure(figsize=(20,10))
plt.plot(a1rb, color = "blue", linewidth=1, label = "a1rb_production")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Bottom Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("13")
plt.show(block=False)
plt.pause(5)

#Arm 2 Left Bottom
#plt.figure(figsize=(20,10))
plt.plot(a2lb, color = "red", linewidth=1, label = "a2lb_production")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Bottom Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("14")
plt.show(block=False)
plt.pause(5)

#Arm 2 Right Bottom
#plt.figure(figsize=(20,10))
plt.plot(a2rb, color = "grey", linewidth=1, label = "a2rb_production")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Bottom Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("15")
plt.show(block=False)
plt.pause(5)

#Arm 3 Left Bottom
#plt.figure(figsize=(20,10))
plt.plot(a3lb, color = "green", linewidth=1, label = "a3lb_production")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Bottom Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("16")
plt.show(block=False)
plt.pause(5)

#Arm 3 Right Bottom
#plt.figure(figsize=(20,10))
plt.plot(a3rb, color = "purple", linewidth=1, label = "a3rb_production")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Bottom Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("17")
plt.show(block=False)
plt.pause(5)
plt.close("all")

'''
#Bottom Trials

#Trial_1_Bottom
#plt.figure(figsize=(20,10))
plt.plot(trial1b, color = "violet", linewidth=1, label = "Trial1")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Bottom Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("18")
plt.show(block=False)
plt.pause(5)

#Trial_2_Bottom
#plt.figure(figsize=(20,10))
plt.plot(trial2b, color = "orange", linewidth=1, label = "Trial2")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Bottom Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("19")
plt.show(block=False)
plt.pause(5)

#Trial_3_Bottom
#plt.figure(figsize=(20,10))
plt.plot(trial3b, color = "pink", linewidth=1, label = "Trial3")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Bottom Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("20")
plt.show(block=False)
plt.pause(10)

#Trial_4_Bottom
#plt.figure(figsize=(20,10))
plt.plot(trial4b, color = "brown", linewidth=1, label = "Trial4")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Bottom Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("21")
plt.show(block=False)
plt.pause(5)

#Trial_5_Bottom
#plt.figure(figsize=(20,10))
plt.plot(trial5b, color = "indigo", linewidth=1, label = "Trial5")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Bottom Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("22")
plt.show(block=False)
plt.pause(5)
plt.close("all")
'''

#Loose Tray
#Top of the moulds
#Arm 1 Left Top
plt.figure(figsize=(20,10))
plt.plot(a1lt2, color = "red", linewidth=1, label = "a1lt2_loose tray_arm pos")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Top Thermocouples")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.savefig("23")
plt.show(block=False)
plt.pause(5)

#Arm 1 Right Top
#plt.figure(figsize=(20,10))
plt.plot(a1rt2, color = "grey", linewidth=1, label = "a1rt2_loose tray_arm pos")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Top Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("24")
plt.show(block=False)
plt.pause(5)

#Arm 2 Left Top
#plt.figure(figsize=(20,10))
plt.plot(a2lt2, color = "yellow", linewidth=1, label = "a2lt2_loose tray")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Top Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("25")
plt.show(block=False)
plt.pause(5)

#Arm 2 Right Top
#plt.figure(figsize=(20,10))
plt.plot(a2rt2, color = "purple", linewidth=1, label = "a2rt2_loose tray")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Top Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("26")
plt.show(block=False)
plt.pause(5)

#Arm 3 Left Top
#plt.figure(figsize=(20,10))
plt.plot(a3lt2, color = "green", linewidth=1, label = "a3lt2_loose tray")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Top Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("27")
plt.show(block=False)
plt.pause(5)

#Arm 3 Right Top
#plt.figure(figsize=(20,10))
plt.plot(a3rt2, color = "orange", linewidth=1, label = "a3rt2_loose tray")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Top Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("28")
plt.show(block=False)
plt.pause(5)
plt.close("all")

#Loose Tray
#Bottom of the mould

#Arm 1 Left Bottom
plt.figure(figsize=(20,10))
plt.plot(a1lb2, color = "black", linewidth=1, label = "a1lb2_loose tray_arm pos")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Bottom Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.savefig("29")
plt.show(block=False)
plt.pause(5)

#Arm 1 Right Bottom
#plt.figure(figsize=(20,10))
plt.plot(a1rb2, color = "orange", linewidth=1, label = "a1rb2_loose tray_arm pos")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Bottom Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("30")
plt.show(block=False)
plt.pause(5)

#Arm 2 Left Bottom
#plt.figure(figsize=(20,10))
plt.plot(a2lb2, color = "red", linewidth=1, label = "a2lb2_loose tray")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Bottom Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("31")
plt.show(block=False)
plt.pause(5)

#Arm 2 Right Bottom
#plt.figure(figsize=(20,10))
plt.plot(a2rb2, color = "grey", linewidth=1, label = "a2rb2_loose tray")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Bottom Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("32")
plt.show(block=False)
plt.pause(5)

#Arm 3 Left Bottom
#plt.figure(figsize=(20,10))
plt.plot(a3lb2, color = "green", linewidth=1, label = "a3lb2_loose tray")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Bottom Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("33")
plt.show(block=False)
plt.pause(5)

#Arm 3 Right Bottom
#plt.figure(figsize=(20,10))
plt.plot(a3rb2, color = "purple", linewidth=1, label = "a3rb2_loose tray")
plt.title("Balloon Length Failure Investigation")
plt.suptitle("Temperature Profile - Bottom Thermocouple")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("34")
plt.show(block=False)
plt.pause(5)
plt.close("all")

#Side by Side plots
#Thermocouple in the top of the moulds with production settings
plt.subplot(1, 2, 1)
plt.plot(a1lt, "violet", linewidth=1, label = "a1lt_production")
plt.plot(a1rt, "turquoise", linewidth=1, label = "a1rt_production")
plt.plot(a2lt, "peru", linewidth=1, label = "a2lt_production")
plt.plot(a2rt, "thistle", linewidth=1, label = "a2rt_production")
plt.plot(a3lt, "seagreen", linewidth=1, label = "a3lt_production")
plt.plot(a3rt, "purple", linewidth=1, label = "a3rt_production")
plt.title("Production Settings - Top Thermocouple")
plt.suptitle("Balloon Length Failure Investigation")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
figure = plt.gcf()
figure.set_size_inches(20, 10)

#Thermocouple in the top of the moulds with modifications
plt.subplot(1, 2, 2)
plt.plot(a1lt2, "c--", linewidth=1, label = "a1lt2_loose tray_arm pos")
plt.plot(a1rt2, "b--", linewidth=1, label = "a1rt2_loose tray_arm pos")
plt.plot(a2lt2, "r--", linewidth=1, label = "a2lt2_loose tray")
plt.plot(a2rt2, "g--", linewidth=1, label = "a2rt2_loose tray")
plt.plot(a3lt2, "m--", linewidth=1, label = "a3lt2_loose tray")
plt.plot(a3rt2, "y--", linewidth=1, label = "a3rt2_loose tray")
plt.title("Modified Settings - Top Thermocouple")
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
plt.title("Production Settings - Bottom Thermocouple")
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
plt.title("Modified Settings - Bottom Thermocouple")
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