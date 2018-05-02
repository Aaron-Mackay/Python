status = "y"
while status == "y":
    old = float(raw_input("Input old figure: "))
    new = float(raw_input("Input new figure: "))
    print "Percentage change is " + "{0:.2f}".format(((new/old)-1)*100) + "%"
    status = raw_input("Start again? (y/n) ")
    print ""
