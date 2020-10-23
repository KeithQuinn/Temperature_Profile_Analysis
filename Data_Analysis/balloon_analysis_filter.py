import pandas as pd
import matplotlib.pyplot as plt
file_name = str(input('Include File Name for Analysis (include extension): '))
df = pd.read_excel(file_name)

#production settings
a1lt = []
for i in df["A1LT"]:
    if i >= 10:
        a1lt.append(i)
a1lb = []
for i in df["A1LB"]:
    if i >= 10:
        a1lb.append(i)
a2lt = []
for i in df["A2LT"]:
    if i >= 10:
        a2lt.append(i)
a2lb = []
for i in df["A2LB"]:
    if i >= 10:
        a2lb.append(i)
a3lt = []
for i in df["A3LT"]:
    if i >= 10:
        a3lt.append(i)
a3lb = []
for i in df["A3LB"]:
    if i >= 10:
        a3lb.append(i)
a1rt = []
for i in df["A1RT"]:
    if i >= 10:
        a1rt.append(i)
a1rb = []
for i in df["A1RB"]:
    if i >= 10:
        a1rb.append(i)
a2rt = []
for i in df["A2RT"]:
    if i >= 10:
        a2rt.append(i)
a2rb = []
for i in df["A2RB"]:
    if i >= 10:
        a2rb.append(i)
a3rt = []
for i in df["A3RT"]:
    if i >= 10:
        a3rt.append(i)
a3rb = []
for i in df["A3RB"]:
    if i >= 10:
        a3rb.append(i)

#modified settings (arm position and loose tray)
a1lt2 = []
for i in df["A1LT2"]:
    if i >= 10:
        a1lt2.append(i)
a1lb2 = []
for i in df["A1LB2"]:
    if i >= 10:
        a1lb2.append(i)
a2lt2 = []
for i in df["A2LT2"]:
    if i >= 10:
        a2lt2.append(i)
a2lb2 = []
for i in df["A2LB2"]:
    if i >= 10:
        a2lb2.append(i)
a3lt2 = []
for i in df["A3LT2"]:
    if i >= 10:
        a3lt2.append(i)
a3lb2 = []
for i in df["A3LB2"]:
    if i >= 10:
        a3lb2.append(i)
a1rt2 = []
for i in df["A1RT2"]:
    if i >= 10:
        a1rt2.append(i)
a1rb2 = []
for i in df["A1RB2"]:
    if i >= 10:
        a1rb2.append(i)
a2rt2 = []
for i in df["A2RT2"]:
    if i >= 10:
        a2rt2.append(i)
a2rb2 = []
for i in df["A2RB2"]:
    if i >= 10:
        a2rb2.append(i)
a3rt2 = []
for i in df["A3RT2"]:
    if i >= 10:
        a3rt2.append(i)
a3rb2 = []
for i in df["A3RB2"]:
    if i >= 10:
        a3rb2.append(i)

#Thermocouple in the top of the moulds
#Arm 1 Left Top
plt.figure(figsize=(20,10))
plt.plot(a1lt, color = "black", linewidth=1, label = "a1lt_production")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.text(61, 137, file_name, color='black', size=12)
plt.title("Temperature Profile - Top Thermocouple - Production Settings")
plt.suptitle("Balloon Length Failure Investigation")
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.savefig("1")
plt.show(block=False)
plt.pause(4)

#Arm 1 Right Top
#plt.figure(figsize=(20,10))
plt.plot(a1rt, color = "blue", linewidth=1, label = "a1rt_production")
plt.title("Temperature Profile - Top Thermocouple - Production Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("2")
plt.show(block=False)
plt.pause(2)

#Arm 2 Left Top
##plt.figure(figsize=(20,10))
plt.plot(a2lt, color = "red", linewidth=1, label = "a2lt_production")
plt.title("Temperature Profile - Top Thermocouple - Production Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("3")
plt.show(block=False)
plt.pause(2)

#Arm 2 Right Top
#plt.figure(figsize=(20,10))
plt.plot(a2rt, color = "grey", linewidth=1, label = "a2rt_production")
plt.title("Temperature Profile - Top Thermocouple - Production Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("4")
plt.show(block=False)
plt.pause(2)

#Arm 3 Left Top
#plt.figure(figsize=(20,10))
plt.plot(a3lt, color = "green", linewidth=1, label = "a3lt_production")
plt.title("Temperature Profile - Top Thermocouple - Production Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("5")
plt.show(block=False)
plt.pause(2)

#Arm 3 Right Top
#plt.figure(figsize=(20,10))
plt.plot(a3rt, color = "purple", linewidth=1, label = "a3rt_production")
plt.title("Temperature Profile - Top Thermocouple - Production Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("6")
plt.show(block=False)
plt.pause(2)
plt.close("all")

#Thermocouple in the bottom of the mould
#Arm 1 Left Bottom
plt.figure(figsize=(20,10))
plt.plot(a1lb, color = "black", linewidth=1, label = "a1lb_production")
plt.title("Temperature Profile - Bottom Thermocouple - Production Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.savefig("12")
plt.show(block=False)
plt.pause(4)

#Arm 1 Right Bottom
#plt.figure(figsize=(20,10))
plt.plot(a1rb, color = "blue", linewidth=1, label = "a1rb_production")
plt.title("Temperature Profile - Bottom Thermocouple - Production Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("13")
plt.show(block=False)
plt.pause(2)

#Arm 2 Left Bottom
#plt.figure(figsize=(20,10))
plt.plot(a2lb, color = "red", linewidth=1, label = "a2lb_production")
plt.title("Temperature Profile - Bottom Thermocouple - Production Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("14")
plt.show(block=False)
plt.pause(2)

#Arm 2 Right Bottom
#plt.figure(figsize=(20,10))
plt.plot(a2rb, color = "grey", linewidth=1, label = "a2rb_production")
plt.title("Temperature Profile - Bottom Thermocouple - Production Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("15")
plt.show(block=False)
plt.pause(2)

#Arm 3 Left Bottom
#plt.figure(figsize=(20,10))
plt.plot(a3lb, color = "green", linewidth=1, label = "a3lb_production")
plt.title("Temperature Profile - Bottom Thermocouple - Production Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("16")
plt.show(block=False)
plt.pause(2)

#Arm 3 Right Bottom
#plt.figure(figsize=(20,10))
plt.plot(a3rb, color = "purple", linewidth=1, label = "a3rb_production")
plt.title("Temperature Profile - Bottom Thermocouple - Production Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("17")
plt.show(block=False)
plt.pause(2)
plt.close("all")

#Loose Tray
#Top of the moulds
#Arm 1 Left Top
plt.figure(figsize=(20,10))
plt.plot(a1lt2, color = "red", linewidth=1, label = "a1lt2_loose tray_arm pos")
plt.title("Temperature Profile - Top Thermocouple - Modified Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.savefig("23")
plt.show(block=False)
plt.pause(2)

#Arm 1 Right Top
#plt.figure(figsize=(20,10))
plt.plot(a1rt2, color = "grey", linewidth=1, label = "a1rt2_loose tray_arm pos")
plt.title("Temperature Profile - Top Thermocouple - Modified Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("24")
plt.show(block=False)
plt.pause(2)

#Arm 2 Left Top
#plt.figure(figsize=(20,10))
plt.plot(a2lt2, color = "yellow", linewidth=1, label = "a2lt2_loose tray")
plt.title("Temperature Profile - Top Thermocouple - Modified Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("25")
plt.show(block=False)
plt.pause(2)

#Arm 2 Right Top
#plt.figure(figsize=(20,10))
plt.plot(a2rt2, color = "purple", linewidth=1, label = "a2rt2_loose tray")
plt.title("Temperature Profile - Top Thermocouple - Modified Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("26")
plt.show(block=False)
plt.pause(2)

#Arm 3 Left Top
#plt.figure(figsize=(20,10))
plt.plot(a3lt2, color = "green", linewidth=1, label = "a3lt2_loose tray")
plt.title("Temperature Profile - Top Thermocouple - Modified Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("27")
plt.show(block=False)
plt.pause(2)

#Arm 3 Right Top
#plt.figure(figsize=(20,10))
plt.plot(a3rt2, color = "orange", linewidth=1, label = "a3rt2_loose tray")
plt.title("Temperature Profile - Top Thermocouple - Modified Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("28")
plt.show(block=False)
plt.pause(2)
plt.close("all")

#Loose Tray
#Bottom of the mould
#Arm 1 Left Bottom
plt.figure(figsize=(20,10))
plt.plot(a1lb2, color = "black", linewidth=1, label = "a1lb2_loose tray_arm pos")
plt.title("Temperature Profile - Bottom Thermocouple - Modified Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.savefig("29")
plt.show(block=False)
plt.pause(2)

#Arm 1 Right Bottom
#plt.figure(figsize=(20,10))
plt.plot(a1rb2, color = "orange", linewidth=1, label = "a1rb2_loose tray_arm pos")
plt.title("Temperature Profile - Bottom Thermocouple - Modified Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("30")
plt.show(block=False)
plt.pause(2)

#Arm 2 Left Bottom
#plt.figure(figsize=(20,10))
plt.plot(a2lb2, color = "red", linewidth=1, label = "a2lb2_loose tray")
plt.title("Temperature Profile - Bottom Thermocouple - Modified Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("31")
plt.show(block=False)
plt.pause(2)

#Arm 2 Right Bottom
#plt.figure(figsize=(20,10))
plt.plot(a2rb2, color = "grey", linewidth=1, label = "a2rb2_loose tray")
plt.title("Temperature Profile - Bottom Thermocouple - Modified Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("32")
plt.show(block=False)
plt.pause(2)

#Arm 3 Left Bottom
#plt.figure(figsize=(20,10))
plt.plot(a3lb2, color = "green", linewidth=1, label = "a3lb2_loose tray")
plt.title("Temperature Profile - Bottom Thermocouple - Modified Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("33")
plt.show(block=False)
plt.pause(2)

#Arm 3 Right Bottom
#plt.figure(figsize=(20,10))
plt.plot(a3rb2, color = "purple", linewidth=1, label = "a3rb2_loose tray")
plt.title("Temperature Profile - Bottom Thermocouple - Modified Settings")
plt.suptitle("Balloon Length Failure Investigation")
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(61, 137, file_name, color='black', size=12)
plt.text(42, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
plt.savefig("34")
plt.show(block=False)
plt.pause(2)
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
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(65, 137, file_name, color='black', size=12)
plt.text(32, 137, "Data Analysed from:", color='black', size=12)
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
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(65, 137, file_name, color='black', size=12)
plt.text(32, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
figure = plt.gcf()
figure.set_size_inches(20, 10)
plt.savefig("101", dpi=100)
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show(block=False)
plt.pause(2)
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
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(65, 137, file_name, color='black', size=12)
plt.text(32, 137, "Data Analysed from:", color='black', size=12)
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
axes = plt.gca()
axes.set_xlim([0,120])
axes.set_ylim([25,130])
plt.text(65, 137, file_name, color='black', size=12)
plt.text(32, 137, "Data Analysed from:", color='black', size=12)
plt.legend(loc = "upper left")
plt.xticks([])
plt.ylabel("Temperature [C]", color = "black")
figure = plt.gcf()
figure.set_size_inches(20, 10)
plt.savefig("102", dpi=100)
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show(block=False)
plt.pause(2)
plt.close("all")