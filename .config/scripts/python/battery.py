
file_path = "/sys/class/power_supply/BAT0/"
f1 = open(file_path+"charge_now")
f2 = open(file_path+"charge_full")
charge_now = int(f1.read().strip())
charge_full  = int(f2.read().strip())
percent_charge = (charge_now/charge_full)*100
print("Battery :",round(percent_charge))

