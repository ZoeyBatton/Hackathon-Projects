# g = ground shipping
weight = input("How many Lb does your package weigh?: ")
cost_gr_2 = int(weight) * 1.50 + 20
cost_gr_2_6 = weight * 3.00 + 20
cost_gr_6_10 = weight * 4.00 + 20
cost_gr_10 = weight * 4.75 + 20
if weight <= 2:
  print(f"Your package will cost ${'{0:.2f}'.format(cost_gr_2)} to ship with Ground Shipping.")
elif weight <= 6:
  print(f"Your package will cost ${'{0:.2f}'.format(cost_gr_2_6)} to ship with Ground Shipping.")
elif weight <= 10:
  print(f"Your package will cost ${'{0:.2f}'.format(cost_gr_6_10)} to ship with Ground Shipping.")
else:
    print(f"Your package will cost ${'{0:.2f}'.format(cost_gr_2)} to ship with Ground Shipping.")

#premium shipping:
cost_gr_premium = 125.00
print("\nIf you would like Premium shipping, the Flat charge is " + (str(cost_gr_premium)) + " with no additional weight charges.")

#Drone shipping 
cost_dr_2 = weight * 4.50 
cost_dr_2_6 = weight * 9.00 
# cost_dr_2_6 = round(cost_dr_2_6, 2)
cost_dr_6_10 = weight * 12.00 
cost_dr_10 = weight * 14.25 
if weight <= 2:
  print(f"\nYour package will cost ${'{0:.2f}'.format(cost_dr_2)} to ship with Drone Shipping.")
elif weight <= 6:
  # print("\nYour package will cost $" + (str(cost_dr_2_6) + " to ship with Drone Shipping."))
  print(f"\nYour package will cost ${'{0:.2f}'.format(cost_dr_2_6)} to ship with Drone Shipping.")
elif weight <= 10:
  print(f"\nYour package will cost ${'{0:.2f}'.format(cost_dr_6_10)} to ship with Drone Shipping.")
else:
    print(f"\nYour package will cost ${'{0:.2f}'.format(cost_dr_10)} to ship with Drone Shipping.")

# print(format(cost_dr_2_6, ".2f"))
# "{0:.2f}".format(cost_dr_2) 
# "{0:.2f}".format(cost_dr_2_6)
# "{0:.2f}".format(cost_dr_6_10)
# "{0:.2f}".format(cost_dr_10)