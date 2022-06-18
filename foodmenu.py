print("welcome to our restraunt ")
print("you want our service\n1.yes\n2.no")
a = input("enter your choice(y/n):")
if a =="yes" or a=="y":
    print("""
1 for monday
2 for tuesday
3 for wednesday
4 for thursday
5 for friday
6 for saturday
7 for sunday""")
    day = input("enter the day...:")
    if day == "monday" or day=="mon" or day=="1":
        print("monday's menu")
        print("1.breakfast\n2.lunch\n3.dinner")
        food=input("your choice sir....")
        if food=="1" or food == "breakfast":
            print("1.poha\n2.sewai\n3.maggi")
            your=input("enter your choice:-")
            if your=="1" or your=="poha":
                print("poha")
                print("you have options....\n1.half\n2.full")
                choose = input("enter your choice:")
                if choose =="1":
                    print("50 rupee")
                elif choose =="2":
                    print("100 rupee")
                else:
                    print("Wrong input...")
            elif your=="2" or your=="sewai":
                print("sewai")
                print("you have options....\n1.half\n2.full")
                choose = input("enter your choice:")
                if choose =="1":
                    print("40 rupee")
                elif choose =="2":
                    print("70 rupee")
                else:
                    print("wrong input....")                    
            elif your=="3" or your==("maggi"):
                print("maggi")
                print("you have options....\n1.half\n2.full")
                choose = input("enter your choice:")
                if choose =="1":
                    print("50 rupee")
                elif choose =="2":
                    print("90 rupee")
                else:
                    print("wrong input....")    
            else:
                print("Thank you for your visit:)")        
        elif food=="2" or food=="lunch":
            print("1.rice & sabzi\n2.rice & dal\n3.rice & chole")
            your=input("Enter your choice:-")
            if your=="1":
                print("rice & sabzi")
                print("you have options....\n1.half\n2.full")
                choose=input("chose any option..:-")
                if choose =="1":
                    print("50 rupee")
                elif choose=="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            elif your=="2":
                print("rice & dal")
                print("you have options....\n1.half\n2.full")
                choose=input("chose any option..:-")
                if choose =="1":
                    print("50 rupee")
                elif choose=="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            elif your=="3":
                print("rice & chole")
                print("you have options....\n1.half\n2.full")
                choose=input("chose any option..:-")
                if choose =="1":
                    print("50 rupee")
                elif choose=="2":
                    print("90 rupee")
                else:
                    print("wrong input....") 
            else:
                print("Thank you for your visit:)")  
        elif food=="3" or food=="dinner":
            print(".Roti & panir\n2.Roti & subji\n3.Roti & chole")
            food=input("Enter your choice..:-")
            if food=="1":
                print("roti & paneer")
                choose=input("choose any option..:-\n1.half\n2.full")
                if choose=="1":
                        print("30 rupee")
                elif choose == "2":
                        print("50")
                else:
                        print("wrong input...")
            elif food =="2":
                print("roti & sabzi")
                choose=input("choose any option..:-\n1.half\n2.full")
                if choose=="1":
                        print("30 rupee")
                elif choose == "2":
                        print("50")
                else:
                        print("wrong input...")
            elif food=="3":
                print("roti & chole")
                choose=input("choose any option..:-\n1.half\n2.full")
                if choose=="1":
                        print("30 rupee")
                elif choose == "2":
                        print("50")
                else:
                        print("wrong input...") 
            else:
                print("thank you for your visit sir:)")
    elif day == "tuesday" or day=="tue" or day=="2":
        print("tuesday's menu")
        print("1.breakfast\n2.lunch\n3.dinner")
        food=input("your choice sir....")
        if food=="1" or food == "breakfast":
            print("1.poha\n2.sewai\n3.maggi")
            your=input("enter your choice:-")
            if your=="1" or your=="poha":
                print("poha")
                print("you have options....\n1.half\n2.full")
                choose = input("enter your choice:")
                if choose =="1":
                    print("50 rupee")
                elif choose =="2":
                    print("100 rupee")
                else:
                    print("Wrong input...")
            elif your=="2" or your=="sewai":
                print("sewai")
                print("you have options....\n1.half\n2.full")
                choose = input("enter your choice:")
                if choose =="1":
                    print("40 rupee")
                elif choose =="2":
                    print("70 rupee")
                else:
                    print("wrong input....")                    
            elif your=="3" or your==("maggi"):
                print("maggi")
                print("you have options....\n1.half\n2.full")
                choose = input("enter your choice:")
                if choose =="1":
                    print("50 rupee")
                elif choose =="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            else:
                print("Thank you for your visit :)")
        elif food=="2" or food=="lunch":
            print("1.rice & sabzi\n2.rice & dal\n3.rice & chole")
            your=input("Enter your choice:-")
            if your=="1":
                print("rice & sabzi")
                print("you have options....\n1.half\n2.full")
                choose=input("chose any option..:-")
                if choose =="1":
                    print("50 rupee")
                elif choose=="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            elif your=="2":
                print("rice & dal")
                print("you have options....\n1.half\n2.full")
                choose=input("chose any option..:-")
                if choose =="1":
                    print("50 rupee")
                elif choose=="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            elif your=="3":
                print("rice & chole")
                print("you have options....\n1.half\n2.full")
                choose=input("chose any option..:-")
                if choose =="1":
                    print("50 rupee")
                elif choose=="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            else:
                print("Thank you for your visit :)")
        elif food=="3" or food=="dinner":
            print(".Roti & panir\n2.Roti & subji\n3.Roti & chole")
            food=input("Enter your choice..:-")
            if food=="1":
                print("roti & paneer")
                choose=input("choose any option..:-\n1.half\n2.full")
                if choose=="1":
                        print("30 rupee")
                elif choose == "2":
                        print("50")
                else:
                        print("wrong input...")
            elif food =="2":
                print("roti & sabzi")
                choose=input("choose any option..:-\n1.half\n2.full")
                if choose=="1":
                        print("30 rupee")
                elif choose == "2":
                        print("50")
                else:
                        print("wrong input...")
            elif food=="3":
                print("roti & chole")
                choose=input("choose any option..:-\n1.half\n2.full")
                if choose=="1":
                        print("30 rupee")
                elif choose == "2":
                        print("50")
                else:
                        print("wrong input...")
            else:
                print("Thank you for your visit:)")
    elif day == "wedesday" or day=="wed" or day=="3":
        print("wednesday's menu")
        print("1.breakfast\n2.lunch\n3.dinner")
        food=input("your choice sir....")
        if food=="1" or food == "breakfast":
            print("1.poha\n2.sewai\n3.maggi")
            your=input("enter your choice:-")
            if your=="1" or your=="poha":
                print("poha")
                print("you have options....\n1.half\n2.full")
                choose = input("enter your choice:")
                if choose =="1":
                    print("50 rupee")
                elif choose =="2":
                    print("100 rupee")
                else:
                    print("Wrong input...")
            elif your=="2" or your=="sewai":
                print("sewai")
                print("you have options....\n1.half\n2.full")
                choose = input("enter your choice:")
                if choose =="1":
                    print("40 rupee")
                elif choose =="2":
                    print("70 rupee")
                else:
                    print("wrong input....")                    
            elif your=="3" or your==("maggi"):
                print("maggi")
                print("you have options....\n1.half\n2.full")
                choose = input("enter your choice:")
                if choose =="1":
                    print("50 rupee")
                elif choose =="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            else:
                print("Thank you for your visit:)")
        elif food=="2" or food=="lunch":
            print("1.rice & sabzi\n2.rice & dal\n3.rice & chole")
            your=input("Enter your choice:-")
            if your=="1":
                print("rice & sabzi")
                print("you have options....\n1.half\n2.full")
                choose=input("chose any option..:-")
                if choose =="1":
                    print("50 rupee")
                elif choose=="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            elif your=="2":
                print("rice & dal")
                print("you have options....\n1.half\n2.full")
                choose=input("chose any option..:-")
                if choose =="1":
                    print("50 rupee")
                elif choose=="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            elif your=="3":
                print("rice & chole")
                print("you have options....\n1.half\n2.full")
                choose=input("chose any option..:-")
                if choose =="1":
                    print("50 rupee")
                elif choose=="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            else:
                print("Thank you for your visit:)")
        elif food=="3" or food=="dinner":
            print(".Roti & panir\n2.Roti & subji\n3.Roti & chole")
            food=input("Enter your choice..:-")
            if food=="1":
                print("roti & paneer")
                choose=input("choose any option..:-\n1.half\n2.full")
                if choose=="1":
                        print("30 rupee")
                elif choose == "2":
                        print("50")
                else:
                        print("wrong input...")
            elif food =="2":
                print("roti & sabzi")
                choose=input("choose any option..:-\n1.half\n2.full")
                if choose=="1":
                        print("30 rupee")
                elif choose == "2":
                        print("50")
                else:
                        print("wrong input...")
            elif food=="3":
                print("roti & chole")
                choose=input("choose any option..:-\n1.half\n2.full")
                if choose=="1":
                        print("30 rupee")
                elif choose == "2":
                        print("50")
                else:
                        print("wrong input...")
            else:
                print("Thank you for your visit :)")
    elif day == "thursday" or day=="thu" or day=="4":
        print("thursday's menu")
        print("1.breakfast\n2.lunch\n3.dinner")
        food=input("your choice sir....")
        if food=="1" or food == "breakfast":
            print("1.poha\n2.sewai\n3.maggi")
            your=input("enter your choice:-")
            if your=="1" or your=="poha":
                print("poha")
                print("you have options....\n1.half\n2.full")
                choose = input("enter your choice:")
                if choose =="1":
                    print("50 rupee")
                elif choose =="2":
                    print("100 rupee")
                else:
                    print("Wrong input...")
            elif your=="2" or your=="sewai":
                print("sewai")
                print("you have options....\n1.half\n2.full")
                choose = input("enter your choice:")
                if choose =="1":
                    print("40 rupee")
                elif choose =="2":
                    print("70 rupee")
                else:
                    print("wrong input....")                    
            elif your=="3" or your==("maggi"):
                print("maggi")
                print("you have options....\n1.half\n2.full")
                choose = input("enter your choice:")
                if choose =="1":
                    print("50 rupee")
                elif choose =="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            else:
                print("Thank you for your visit:)")
        elif food=="2" or food=="lunch":
            print("1.rice & sabzi\n2.rice & dal\n3.rice & chole")
            your=input("Enter your choice:-")
            if your=="1":
                print("rice & sabzi")
                print("you have options....\n1.half\n2.full")
                choose=input("chose any option..:-")
                if choose =="1":
                    print("50 rupee")
                elif choose=="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            elif your=="2":
                print("rice & dal")
                print("you have options....\n1.half\n2.full")
                choose=input("chose any option..:-")
                if choose =="1":
                    print("50 rupee")
                elif choose=="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            elif your=="3":
                print("rice & chole")
                print("you have options....\n1.half\n2.full")
                choose=input("chose any option..:-")
                if choose =="1":
                    print("50 rupee")
                elif choose=="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            else:
                print("Thank you for your visit:)")
        elif food=="3" or food=="dinner":
            print(".Roti & panir\n2.Roti & subji\n3.Roti & chole")
            food=input("Enter your choice..:-")
            if food=="1":
                print("roti & paneer")
                choose=input("choose any option..:-\n1.half\n2.full")
                if choose=="1":
                    if choose =="1":
                        print("30 rupee")
                    elif choose == "2":
                        print("50")
                    else:
                        print("wrong input...")
            elif food =="2":
                print("roti & sabzi")
                choose=input("choose any option..:-\n1.half\n2.full")
                if choose=="1":
                    if choose =="1":
                        print("30 rupee")
                    elif choose == "2":
                        print("50")
                    else:
                        print("wrong input...")
            elif food=="3":
                print("roti & chole")
                choose=input("choose any option..:-\n1.half\n2.full")
                if choose=="1":
                        print("30 rupee")
                elif choose == "2":
                        print("50")
                else:
                        print("wrong input...")
            else:
                print("Thank you for your visit:)")
    elif day == "friday" or day=="fri" or day=="5":
        print("friday's menu")
        print("1.breakfast\n2.lunch\n3.dinner")
        food=input("your choice sir....")
        if food=="1" or food == "breakfast":
            print("1.poha\n2.sewai\n3.maggi")
            your=input("enter your choice:-")
            if your=="1" or your=="poha":
                print("poha")
                print("you have options....\n1.half\n2.full")
                choose = input("enter your choice:")
                if choose =="1":
                    print("50 rupee")
                elif choose =="2":
                    print("100 rupee")
                else:
                    print("Wrong input...")
            elif your=="2" or your=="sewai":
                print("sewai")
                print("you have options....\n1.half\n2.full")
                choose = input("enter your choice:")
                if choose =="1":
                    print("40 rupee")
                elif choose =="2":
                    print("70 rupee")
                else:
                    print("wrong input....")                    
            elif your=="3" or your==("maggi"):
                print("maggi")
                print("you have options....\n1.half\n2.full")
                choose = input("enter your choice:")
                if choose =="1":
                    print("50 rupee")
                elif choose =="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            else:
                print("Thankyou for your visit:)")
        elif food=="2" or food=="lunch":
            print("1.rice & sabzi\n2.rice & dal\n3.rice & chole")
            your=input("Enter your choice:-")
            if your=="1":
                print("rice & sabzi")
                print("you have options....\n1.half\n2.full")
                choose=input("chose any option..:-")
                if choose =="1":
                    print("50 rupee")
                elif choose=="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            elif your=="2":
                print("rice & dal")
                print("you have options....\n1.half\n2.full")
                choose=input("chose any option..:-")
                if choose =="1":
                    print("50 rupee")
                elif choose=="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            elif your=="3":
                print("rice & chole")
                print("you have options....\n1.half\n2.full")
                choose=input("chose any option..:-")
                if choose =="1":
                    print("50 rupee")
                elif choose=="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            else:
                print("Thank you for your visit")
        elif food=="3" or food=="dinner":
            print(".Roti & panir\n2.Roti & subji\n3.Roti & chole")
            food=input("Enter your choice..:-")
            if food=="1":
                print("roti & paneer\n1.half\n2.full")
                choose=input("choose any option..:-")
                if choose=="1":
                        print("30 rupee")
                elif choose == "2":
                        print("50")
                else:
                        print("wrong input...")
            elif food =="2":
                print("roti & sabzi")
                choose=input("choose any option..:-\n1.half\n2.full")
                if choose=="1":
                    print("30 rupee")
                elif choose == "2":
                    print("50")
                else:
                    print("wrong input...")

            elif food=="3":
                print("roti & chole\n1.half\n2.full")
                choose=input("choose any option..:-")
                if choose=="1":
                        print("30 rupee")
                elif choose == "2":
                        print("50")
                else:
                        print("wrong input...")  
            else:
                print("Thank you for your visit:)")
    elif day == "saturday" or day=="sat" or day=="6":
        print("monday's menu")
        print("1.breakfast\n2.lunch\n3.dinner")
        food=input("your choice sir....")
        if food=="1" or food == "breakfast":
            print("1.poha\n2.sewai\n3.maggi")
            your=input("enter your choice:-")
            if your=="1" or your=="poha":
                print("poha")
                print("you have options....\n1.half\n2.full")
                choose = input("enter your choice:")
                if choose =="1":
                    print("50 rupee")
                elif choose =="2":
                    print("100 rupee")
                else:
                    print("Wrong input...")
            elif your=="2" or your=="sewai":
                print("sewai")
                print("you have options....\n1.half\n2.full")
                choose = input("enter your choice:")
                if choose =="1":
                    print("40 rupee")
                elif choose =="2":
                    print("70 rupee")
                else:
                    print("wrong input....")                    
            elif your=="3" or your==("maggi"):
                print("maggi")
                print("you have options....\n1.half\n2.full")
                choose = input("enter your choice:")
                if choose =="1":
                    print("50 rupee")
                elif choose =="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            else:
                print("Thank you for your visit:)")
        elif food=="2" or food=="lunch":
            print("1.rice & sabzi\n2.rice & dal\n3.rice & chole")
            your=input("Enter your choice:-")
            if your=="1":
                print("rice & sabzi")
                print("you have options....\n1.half\n2.full")
                choose=input("chose any option..:-")
                if choose =="1":
                    print("50 rupee")
                elif choose=="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            elif your=="2":
                print("rice & dal")
                print("you have options....\n1.half\n2.full")
                choose=input("chose any option..:-")
                if choose =="1":
                    print("50 rupee")
                elif choose=="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            elif your=="3":
                print("rice & chole")
                print("you have options....\n1.half\n2.full")
                choose=input("chose any option..:-")
                if choose =="1":
                    print("50 rupee")
                elif choose=="2":
                    print("90 rupee")
                else:
                    print("wrong input....")
            else:
                print("Thank you for your visit:)")
        elif food=="3" or food=="dinner":
            print(".Roti & panir\n2.Roti & subji\n3.Roti & chole")
            food=input("Enter your choice..:-")
            if food=="1":
                print("roti & paneer")
                choose=input("choose any option..:-\n1.half\n2.full")
                if choose=="1":
                        print("30 rupee")
                elif choose == "2":
                        print("50")
                else:
                        print("wrong input...")
            elif food =="2":
                print("roti & sabzi")
                choose=input("choose any option..:-\n1.half\n2.full")
                if choose=="1":
                        print("30 rupee")
                elif choose == "2":
                        print("50")
                else:
                        print("wrong input...")
            elif food=="3":
                print("roti & chole")
                choose=input("choose any option..:-\n1.half\n2.full")
                if choose=="1":
                        print("30 rupee")
                elif choose == "2":
                        print("50")
                else:
                        print("wrong input...")
            else:
                print("thankyou for your visit :)")
        else:
            print("thank you for your visit:)")
    elif day =="sunday" or day=="sun" or day=="7":
        print("today restraunt is closed....\nplease come tommorow\nTHANKYOU SIR")               
else:
    print("thankyou for your visit sir:)")  