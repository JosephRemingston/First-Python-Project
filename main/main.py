import csv
import random
z = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10" , "11" , "12" , "13" , "14" , "15" , "16" , "17" , "18" , "19" , "20"]
alp = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"]
sym = ["!" , "@" , "#" , "$" , "%" , "^" , "&" , "*" , "(" , ")"]
retu = True
def admin():
    x = input("Enter admin username:")
    y = input("Enter admin password:")
    if [x , y] == ["admin","adm"]:
        l = 0
        z1 = []
        z2 = []
        z3 = []
        z4 = []
        z5 = []
        pl = 0
        with open("Saved_tickets_pl.csv","r",newline="") as f1:
            a = csv.reader(f1)
            for i in a:
                z1.append(i)
            for i in z1:
                l += 1
                pl += 1
            
        f1.close()
        laliga = 0
        with open("Saved_tickets_laliga.csv","r",newline="") as f2:
            a = csv.reader(f2)
            for i in a:
                if len(i) > 0:
                    z2.append(i)
            for i in z2:
                l += 1
                laliga += 1
            
        f2.close()
        seriea = 0
        with open("Saved_tickets_seriea.csv","r",newline="") as f3:
            a = csv.reader(f3)
            for i in a:
                if len(i) > 0:
                    z3.append(i)
            for i in z3:
                l += 1
                seriea += 1
            
        f3.close()
        bundesliga = 0
        with open("Saved_tickets_bundesliga.csv","r",newline="") as f4:
            a = csv.reader(f4)
            for i in a:
                if len(i) > 0:
                    z4.append(i)
            for i in z4:
                l += 1
                bundesliga += 1
           
        f4.close()
        ligue_1 = 0
        with open("Saved_tickets_ligue1.csv","r",newline="") as f5:
            a = csv.reader(f5)
            for i in a:
                if len(i) > 0:
                    z5.append(i)
            for i in z5:
                l += 1
                ligue_1 += 1
              
        f5.close()
        print("|----------------------------------------------------------------------------------------------------|")
        print("No of tickets booked in the pl is            ---------->",pl)
        print()
        print("No of tickets booked for laliga is           ---------->",laliga)
        print()
        print("No of tickets booked for seriea is          ----------> ",seriea)
        print()
        print("No of tickets booked for bunesliga is     ----------> ",bundesliga)
        print()
        print("No of tickets booked for ligue_1 is         ---------->",ligue_1)
        print()
        print("Total tickets booked                               ---------->",l)
        print("|----------------------------------------------------------------------------------------------------|")
    else:
        print("invalid login details")

def recursion(t , x):
    if len(t) == 1:
      for i in range(0,len(x) + 1): 
             try :
                  if x[i][0] == t:
                         z = x[i]
                         return z
                         break
                  else:
                        continue
             except IndexError:
                  continue
    elif len(t) == 2:
          for i in range(0,len(x) + 1):
                try:
                      if x[i][0] + x[i][1] == t[0] + t[1]:
                            z = x[i]
                            return z
                            break
                      else:
                            continue                
                except IndexError:
                      continue                    

#saving module
def save(userid , adults , children , league , team , opponent):
    if league == 1:
        with open("saved_tickets_pl.csv","a",newline="") as f:
            x = [userid , adults , children , team , opponent]
            w = csv.writer(f)
            w.writerow(x)
            f.close()
    elif league == 2:
        with open("saved_tickets_laliga.csv","a",newline="") as f:
            x = [userid , adults , children , team , opponent]
            w = csv.writer(f)
            w.writerow(x)
            f.close()
    elif league == 3:
       with open("saved_tickets_seriea.csv","a",newline="") as f:
            x = [userid , adults , children , team , opponent]
            w = csv.writer(f)
            w.writerow(x)
            f.close()
    elif league == 4:
        with open("saved_tickets_bundesliga.csv","a",newline="") as f:
            x = [userid , adults , children , team , opponent]
            w = csv.writer(f)
            w.writerow(x)
            f.close()
    elif league == 5:
        with open("saved_tickets_ligue1.csv","a",newline="") as f:
            x = [userid , adults , children , team , opponent]       
            w = csv.writer(f)
            w.writerow(x)
            f.close()
    else:
        print("Invalid league")
#payment module
def payment(x , user):
    if x == "upi":
        y = ""
        print("Select the upi domain")
        print("1.@apl")
        print("2.@yapl")
        print("3.axisb")
        print("4.idfcbank")
        print("5.@icici")
        print("6.@axisbank")
        print("7.@okaxis")
        print("8.@okhdfcbank")
        print("9.@okicici")
        print("10.@oksbi")
        upi = int(input("Enter the required ipi domain:"))
        if upi == 1:
            y += "@apl"
        elif upi == 2:
            y += "@yapl"
        elif upi == 3:
            y += "@axixb"
        elif upi == 4:
            y += "@idfcbank"
        elif upi == 5:
            y += "@icici"
        elif upi == 6:
            y += "@axisbank"
        elif upi == 7:
            y += "@okaxis"
        elif upi == 8:
            y += "@okkhdfcbank"
        elif upi == 9:
            y += "@okicici"
        elif upi == 10:
            y += "@oksbi"
        else:
            print("Improper domain please try again")
        user = input("Enter your upi id:")
        user = user.join(y)
        pin = input("Enter the upi pin for:")
        return True
    elif x == "card":
        print("Select they type of card")
        print("1.Credit card")
        print("2.Debit card")
        card = int(input("Enter the type of card:"))
        if card == 1:
            print("You have choosen for credit card")
            print("Choose the credit card processor")
            print("1.Mastercard")
            print("2.Visa")
            processor = int(input("Enter the processor type:"))
            if processor == 1:
                print("You have choosen for mastercard")
                num = int(input("Enter the 16 digit card number:"))
                num = str(num)
                if len(num) == 16:
                    c = int(input("Enter the 3 digit cvv present at the back of the card:"))
                    c = str(c)
                    if len(c) == 3:
                        captcha = random.choice(z) + random.choice(alp) + (random.choice(sym)*3)
                        print("captcha is",captcha)
                        o = input("Enter the captcha:")
                        if o == captcha:
                            print("1.Yes")
                            print("2.No")
                            s = int(input("Do you want to save your login details?"))
                            l = [user , num]
                            if s == 1:
                                print("Payment details are saved")
                                with open("Payment.csv","w") as f:
                                    w = csv.writer(f)
                                    w.writerow(l)
                                    f.close()
                                return True
                            else:
                                print("Payment details not saved")
                                return True
                        else:
                            print("captcha is invalid")
                    else:
                        print("Invalid cvv")
                        return False
                else:
                    print("Invalid card number")
                    return False
            elif processor == 2:
                print("You have choosen for visa")
                num = int(input("Enter the 16 digit card number"))
                num = str(num)
                if len(num) == 16:
                    c = int(input("Enter your three digit cvv at the back of your card"))
                    c = str(num)
                    captcha = random.choice(z) + random.choice(alp) + (random.choice(sym)*3)
                    print("captcha is",captcha)
                    o = input("Enter the captcha")
                    if o == captcha:
                        print("1.Yes")
                        print("2.No")
                        s = int(input("Do you want to save your login details"))
                        if s == 1:
                            print("Your login details have been saved")
                            l = [user , num]
                            with open("payment.csv","w") as f:
                                w = csv.writer(f)
                                w.writerow(l)
                                f.close()
                            return True
                        else:
                            print("Login details not saved")
                            return True
                    else:
                        print("invalid captcha")
                        return False
                else:
                    print("Invalid card number")
                    return False
        elif card == 2:
            print("You have choosen for debit card")
            print("Choose the credit card processor")
            print("1.Mastercard")
            print("2.Visa")
            processor = int(input("Enter the processor type:"))
            if processor == 1:
                print("You have choosen for mastercard")
                num = int(input("Enter the 16 digit card number:"))
                num = str(num)
                if len(num) == 16:
                    c = int(input("Enter the 3 digit cvv present at the back of the card:"))
                    c = str(c)
                    if len(c) == 3:
                        captcha = random.choice(z) + random.choice(alp) + (random.choice(sym)*3)
                        print("captcha is",captcha)
                        o = input("Enter the captcha:")
                        if o == captcha:
                            print("1.Yes")
                            print("2.No")
                            s = int(input("Do you want to save your login details"))
                            l = [user, num]
                            if s == 1:
                                print("Payment details are saved")
                                with open("paymnt.csv", "w") as f:
                                    w = csv.writer(f)
                                    w.writerow(l)
                                    f.close()
                                return True
                            else:
                                print("Payment details not saved")
                                return True
                        else:
                            print("invalid captcha")
                            return False
                    else:
                        print("Invalid cvv")
                        return False
                else:
                    print("Invalid card number")
                    return False
            elif processor == 2:
                print("You have choosen for visa")
                num = input("Enter the 16 digit card number")
                if len(num) == 16:
                    c = input("Enter your three digit cvv at the back of your card")
                    if len(c) == 3:
                        captcha = random.choice(z) + random.choice(alp) + (random.choice(sym)*3)
                        print("captcha is",captcha)
                        o = input("Enter the captcha")
                        if o == captcha:
                            print("1.Yes")
                            print("2.No")
                            s = int(input("Do you want to save your login details"))
                            if s == 1:
                                print("Your login details have been saved")
                                l = [user, num]
                                with open("payment.csv", "a") as f:
                                    w = csv.writer(f)
                                    w.writerow(l)
                                    f.close()
                                return True
                            else:
                                print("Login details not saved")
                                return True
                        else:
                            print("invalid captcha")
                            return False
                    else:
                        print("Invalid cvv")
                        return False
                else:
                    print("Invalid card number")
                    return False
    elif x == "Net banking":
        print("You have choosen for net banking")
        bank = int(input("Enter the 16 digit bank account number:"))
        bank = str(bank)
        if len(bank) == 16:
            bank = int(bank)
            login = input("Enter your login details for account:")
            y = int(input("Enter your bank login verification pin:"))
            captcha = random.choice(z) + random.choice(alp) + (random.choice(sym)*3)
            print("captcha is",captcha)
            o = input("Enter the captcha:")
            if o == captcha:
                print("1.Yes")
                print("2.No")
                s = int(input("Enter do you want to save your login details or not:"))
                if s == 1:
                    l = [user , login]
                    with open("payment.csv","a") as f:
                        w = csv.writer(f)
                        w.writerow(l)
                        print("Login details saved")
                        f.close()
                        return True
                else:
                    print("Login details not saved")
                    return True
            else:
                print("invalid captcha")
                return False
        else:
            print("Invalid number")
            return False
#login  module
def login():
    z = []
    user = input("Enter your username:")
    auth = input("Enter your password:")
    l = [user , auth]
    with open("user_information.csv","r") as f:
        read = csv.reader(f)
        for i in read:
            z.append(i)
        for i in z:
            if l != i:
                continue
            elif l == i:
                return True
            break
        else:
            print("Invalid login credentials")
    f.close()
#register module
def register():
    z = []
    l = 0
    x = input("Enter your username:")
    con = input("Confirm your username:")
    if x == con:
        with open("user_information.csv","r") as f:
            a = csv.reader(f)
            for i in a:
                z.append(i)
            for i in z:
                l += 1
        f.close()
        for i in range(0 , l):
            if x == z[i][0]:
                print("user id already exist")
                print("use another id")
                
                break
        else:
            y = input("Enter password:")
            conf = input("Confirm your password")
            if y == conf:
                a = [x , conf]
                print("Your account has been created successfully")
                with open("user_information.csv","a",newline="") as f:
                    write = csv.writer(f)
                    write.writerow(a)
                f.close()
            else:
                print(None)
    elif x != con:
        print("Username not matching")
    else:
        print(None)
# program main screen
rand = False
while rand == False:
    print("|--------------------------------------------------------------------------------------------------------------------------------------------------------|")
    print("|----------------------------------------------PEPSI  MATCHES TICKET BOOKING FACILITY-------------------------------------------|")
    print("|--------------------------------------------------------------------------------------------------------------------------------------------------------|")
    print("|-------ADMIN--------|----------(1)------------|")
    print("|-------USER-----------|----------(2)------------|")
    print("|-----------------------------------------------------|")
    print()
    i = input("Enter user or admin:")
    if i == "1":
        admin()
        rand = False
    elif i == "2":
        rand = True
    else:
        print("Invalid choice")
rec = True
while rec == True:
    print("+===========================================================================================================================+")
    print("|------Select 1 for login---------------|")
    print("|------Select 2 for register-----------|")
    m = input("Login or Register:")
    if m == "1":
        if login() == True:
            while rec == True:
                print("|-------Your have been successfully logged in------------------------------------------------------+")
                print("|-------Please select the league you want to book the ticket for-----------------------------+")
                print("|--------------|-----------------------------------------------------------------------|--------------------------------+")
                print("|--------------|---------------LEAGUE-------------------------------------------------------------------KEY----+")
                print("|--------------|             English Premier League                ----------->               (  1  )")
                print("|--------------|             Spanish Laliga                              ----------->               (  2  )")
                print("|--------------|             German Bundesliga                      ----------->               (  3  )")
                print("|--------------|             Italian Serie A                              ----------->               (  4  )")
                print("|--------------|             French Ligue 1                             ----------->               (  5  )")
                print("|--------------|----------------------------------------------------------------------------------|-----------------------|")
                print()
                league = int(input("Enter the league you want:"))
                if league == 1:
                    print()
                    print("You have choosen the English Premier League")
                    l = []
                    f = open("premier_league.txt","r",newline = "")
                    a = f.readlines()
                    for i in a:
                        l.append(i)
                    for i in l:
                        if i == '\r\n':
                            l.remove('\r\n')
                        else:
                            continue
                    for i in l:
                        print(i)
                        print("---------")
                    print()
                    x = input("Enter the number of the team you want to watch the match for:")
                    team = recursion(x , l)
                    print()
                    if x in z:
                        if int(x) > 0 and int(x) < 21:
                            x = str(x)
                            for i in l:
                                if i == '\r\n':
                                    l.remove('\r\n')
                                else:
                                    continue
                            for i in l:
                                print(i)
                                print("---------")
                            f.close()
                            print("|-------------------------------------------|")
                            o = input("Enter the number of the opponent:")
                            print("|-------------------------------------------|")
                            print("|-------------------------------------------|")
                            if x != o:
                                if int(x) > 0 and int(x) < 21:
                                    op = recursion(o , l)
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    print("You have choosen to watch for",team,"vs",op)
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    place = int(input("Enter 1 for home game , Enter 2 for away game"))
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    if place == 1:
                                        print("|------You have choosen for home game-----|")
                                        print("|----------Matchday hospitality-------------|","------","(1)")
                                        print("|----------Normal hospitality-----------------|","------","(2)")
                                        hos = int(input("Enter hospitality:"))
                                        if hos == 1:
                                            print("|----------------Ticket costs----------------|")
                                            print("|----------------70$ for adults-------------|")
                                            print("|------55$ for kids below the age of 16-----|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            adult = int(input("Enter number of adults:"))
                                            print()
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            child = int(input("Enter number of children:"))
                                            print()
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            if adult + child < 101:
                                                costadult = 70*adult
                                                costchild = 55*child
                                                t = costadult + costchild
                                                print("upi,card,Net banking")
                                                mode = input("Enter mode of payment:")
                                                uid = input("Renter your user id:")
                                                r = payment(mode , uid)
                                                if r == True:
                                                    print("Your ticket has been booked successfully for the match against",op)
                                                    save(uid , adult , child , league , team , op)
                                                    print("Total cost for your ticket is $",t)
                                                    rec = False
                                                else:
                                                    print("Payment unsuccessful")
                                                    rec = True
                                            else:
                                                print("you can only book 100 tickets at a time")
                                                rec = True
                                        elif hos == 2:
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("Ticket costs")
                                            print("30$ for adults")
                                            print("15$ for kids below the age of 16")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            adult = int(input("Enter number of adults:"))
                                            print("|-------------------------------------------|")
                                            child = int(input("Enter number of children:"))
                                            print("|-------------------------------------------|")
                                            if adult + child < 101:
                                                costadult = 30*adult
                                                costchild = 15*child
                                                t = costadult + costchild
                                                print("|-------------------------------------------|")
                                                print("upi,card,Net banking")
                                                print("|-------------------------------------------|")
                                                mode = input("Enter mode of payment:")
                                                uid = input("Renter your user id:")
                                                print("|-------------------------------------------|")
                                                print("|-------------------------------------------|")
                                                r = payment(mode , uid)
                                                if r == True:
                                                    print("Your ticket has been booked successfully for the match against",op)
                                                    save(uid , adult , child , league , team , op)
                                                    print("Total cost for your ticket is $",t)
                                                    rec = False
                                                else:
                                                    print("Payment unsuccessful")
                                                    rec = True
                                            else:
                                                print("you can only book 100 tickets at a time")
                                                rec = True
                                        else:
                                            print("|------------------------------Invalid input--------------------------|")
                                            print("|-----------enter a number between 1 and 2 only---------|")
                                            rec = True
                                    elif place == 2:
                                        print("Ticket costs")
                                        print("30$ for adults")
                                        print("15$ for kids below the age of 16")
                                        adult = int(input("Enter number of adults:"))
                                        child = int(input("Enter number of children:"))
                                        if adult + child < 101:
                                                costadult = 30*adult
                                                costchild = 15*child
                                                t = costadult + costchild
                                                print("|-------------------------------------------|")
                                                print("upi,card,Net banking")
                                                print("|-------------------------------------------|")
                                                mode = input("Enter mode of payment:")
                                                uid = input("Renter your user id:")
                                                print("|-------------------------------------------|")
                                                print("|-------------------------------------------|")
                                                r = payment(mode , uid)
                                                if r == True:
                                                    print("Your ticket has been booked successfully for the match against",op)
                                                    save(uid , adult , child , league , team , op)
                                                    print("Total cost for your ticket is $",t)
                                                    rec = False
                                                else:
                                                    print("Payment unsuccessful")
                                                    rec = True
                                        else:
                                            print("you can only book 100 tickets at a time")
                                            rec = True  
                                    else:
                                        print("|------------------------------Invalid input--------------------------|")
                                        print("|---------------------Enter a number between 1 and 2 only-------------|")
                                        rec = True
                                else:
                                    print("|------------------------------Invalid input--------------------------|")
                                    print("|-----------enter a number between 1 and 20 only---------|")
                                    rec = True
                            else:
                                print("|------------------------------Invalid input--------------------------|")
                                print("|---------------------opponent and team cannot be the same-------------|") 
                                rec = True
                        else:
                            print("|------------------------------Invalid input--------------------------|")
                            print("|---------------------Enter a number between 1 and 20 only-------------|")
                            rec = True
                    else:
                        print("Invalid input")
                        rec = True       
                elif league == 2:
                    print()
                    print("You have choosen the Spanish LaLiga")
                    l = []
                    f = open("laliga.txt","r",newline = "")
                    a = f.readlines()
                    for i in a:
                        l.append(i)
                    for i in l:
                        if i == '\r\n':
                            l.remove('\r\n')
                        else:
                            continue
                    for i in l:
                        print(i)
                        print("---------")
                    print()
                    x = input("Enter the number of the team you want to watch the match for:")
                    team = recursion(x , l)
                    print()
                    if x in z:
                        if int(x) > 0 and int(x) < 21:
                            x = str(x)
                            for i in l:
                                if i == '\r\n':
                                    l.remove('\r\n')
                                else:
                                    continue
                            for i in l:
                                print(i)
                                print("---------")
                            f.close()
                            print("|-------------------------------------------|")
                            o = input("Enter the number of the opponent:")
                            print("|-------------------------------------------|")
                            print("|-------------------------------------------|")
                            if x != o:
                                if int(x) > 0 and int(x) < 21:
                                    op = recursion(o , l)
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    print("You have choosen to watch for",team,"vs",op)
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    place = int(input("Enter 1 for home game , Enter 2 for away game"))
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    if place == 1:
                                        print("|------You have choosen for home game-----|")
                                        print("|----------Matchday hospitality-------------|","------","(1)")
                                        print("|----------Normal hospitality-----------------|","------","(2)")
                                        hos = int(input("Enter hospitality:"))
                                        if hos == 1:
                                            print("|----------------Ticket costs----------------|")
                                            print("|----------------70$ for adults-------------|")
                                            print("|------55$ for kids below the age of 16-----|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            adult = int(input("Enter number of adults:"))
                                            print()
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            child = int(input("Enter number of children:"))
                                            print()
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            if adult + child < 101:
                                                costadult = 70*adult
                                                costchild = 55*child
                                                t = costadult + costchild
                                                print("upi,card,Net banking")
                                                mode = input("Enter mode of payment:")
                                                uid = input("Renter your user id:")
                                                r = payment(mode , uid)
                                                if r == True:
                                                    print("Your ticket has been booked successfully for the match against",op)
                                                    save(uid , adult , child , league , team , op)
                                                    print("Total cost for your ticket is $",t)
                                                    rec = False
                                                else:
                                                    print("Payment unsuccessful")
                                                    rec = True
                                            else:
                                                print("you can only book 100 tickets at a time")
                                                rec = True
                                        elif hos == 2:
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("Ticket costs")
                                            print("30$ for adults")
                                            print("15$ for kids below the age of 16")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            adult = int(input("Enter number of adults:"))
                                            print("|-------------------------------------------|")
                                            child = int(input("Enter number of children:"))
                                            print("|-------------------------------------------|")
                                            if adult + child < 101:
                                                costadult = 30*adult
                                                costchild = 15*child
                                                t = costadult + costchild
                                                print("|-------------------------------------------|")
                                                print("upi,card,Net banking")
                                                print("|-------------------------------------------|")
                                                mode = input("Enter mode of payment:")
                                                uid = input("Renter your user id:")
                                                print("|-------------------------------------------|")
                                                print("|-------------------------------------------|")
                                                r = payment(mode , uid)
                                                if r == True:
                                                    print("Your ticket has been booked successfully for the match against",op)
                                                    save(uid , adult , child , league , team , op)
                                                    print("Total cost for your ticket is $",t)
                                                    rec = False
                                                else:
                                                    print("Payment unsuccessful")
                                                    rec = True
                                            else:
                                                print("you can only book 100 tickets at a time")
                                                rec = True
                                        else:
                                            print("|------------------------------Invalid input--------------------------|")
                                            print("|-----------enter a number between 1 and 2 only---------|")
                                            rec = True
                                    elif place == 2:
                                        print("Ticket costs")
                                        print("30$ for adults")
                                        print("15$ for kids below the age of 16")
                                        adult = int(input("Enter number of adults:"))
                                        child = int(input("Enter number of children:"))
                                        if adult + child < 101:
                                                costadult = 30*adult
                                                costchild = 15*child
                                                t = costadult + costchild
                                                print("|-------------------------------------------|")
                                                print("upi,card,Net banking")
                                                print("|-------------------------------------------|")
                                                mode = input("Enter mode of payment:")
                                                uid = input("Renter your user id:")
                                                print("|-------------------------------------------|")
                                                print("|-------------------------------------------|")
                                                r = payment(mode , uid)
                                                if r == True:
                                                    print("Your ticket has been booked successfully for the match against",op)
                                                    save(uid , adult , child , league , team , op)
                                                    print("Total cost for your ticket is $",t)
                                                    rec = False
                                                else:
                                                    print("Payment unsuccessful")
                                                    rec = True
                                        else:
                                            print("you can only book 100 tickets at a time")
                                            rec = True  
                                    else:
                                        print("|------------------------------Invalid input--------------------------|")
                                        print("|---------------------Enter a number between 1 and 2 only-------------|")
                                        rec = True
                                else:
                                    print("|------------------------------Invalid input--------------------------|")
                                    print("|-----------enter a number between 1 and 20 only---------|")
                                    rec = True
                            else:
                                print("|------------------------------Invalid input--------------------------|")
                                print("|---------------------opponent and team cannot be the same-------------|") 
                                rec = True
                        else:
                            print("|------------------------------Invalid input--------------------------|")
                            print("|---------------------Enter a number between 1 and 20 only-------------|")
                            rec = True
                    else:
                        print("Invalid input")
                        rec = True       
                elif league == 3:
                    print()
                    print("You have choosen the German Bundesliga")
                    l = []
                    f = open("bundesliga.txt","r",newline = "")
                    a = f.readlines()
                    for i in a:
                        l.append(i)
                    for i in l:
                        if i == '\r\n':
                            l.remove('\r\n')
                        else:
                            continue
                    for i in l:
                        print(i)
                        print("---------")
                    print()
                    x = input("Enter the number of the team you want to watch the match for:")
                    team = recursion(x , l)
                    print()
                    if x in z:
                        if int(x) > 0 and int(x) < 21:
                            x = str(x)
                            for i in l:
                                if i == '\r\n':
                                    l.remove('\r\n')
                                else:
                                    continue
                            for i in l:
                                print(i)
                                print("---------")
                            f.close()
                            print("|-------------------------------------------|")
                            o = input("Enter the number of the opponent:")
                            print("|-------------------------------------------|")
                            print("|-------------------------------------------|")
                            if x != o:
                                if int(x) > 0 and int(x) < 21:
                                    op = recursion(o , l)
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    print("You have choosen to watch for",team,"vs",op)
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    place = int(input("Enter 1 for home game , Enter 2 for away game"))
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    if place == 1:
                                        print("|------You have choosen for home game-----|")
                                        print("|----------Matchday hospitality-------------|","------","(1)")
                                        print("|----------Normal hospitality-----------------|","------","(2)")
                                        hos = int(input("Enter hospitality:"))
                                        if hos == 1:
                                            print("|----------------Ticket costs----------------|")
                                            print("|----------------70$ for adults-------------|")
                                            print("|------55$ for kids below the age of 16-----|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            adult = int(input("Enter number of adults:"))
                                            print()
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            child = int(input("Enter number of children:"))
                                            print()
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            if adult + child < 101:
                                                costadult = 70*adult
                                                costchild = 55*child
                                                t = costadult + costchild
                                                print("upi,card,Net banking")
                                                mode = input("Enter mode of payment:")
                                                uid = input("Renter your user id:")
                                                r = payment(mode , uid)
                                                if r == True:
                                                    print("Your ticket has been booked successfully for the match against",op)
                                                    save(uid , adult , child , league , team , op)
                                                    print("Total cost for your ticket is $",t)
                                                    rec = False
                                                else:
                                                    print("Payment unsuccessful")
                                                    rec = True
                                            else:
                                                print("you can only book 100 tickets at a time")
                                                rec = True
                                        elif hos == 2:
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("Ticket costs")
                                            print("30$ for adults")
                                            print("15$ for kids below the age of 16")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            adult = int(input("Enter number of adults:"))
                                            print("|-------------------------------------------|")
                                            child = int(input("Enter number of children:"))
                                            print("|-------------------------------------------|")
                                            if adult + child < 101:
                                                costadult = 30*adult
                                                costchild = 15*child
                                                t = costadult + costchild
                                                print("|-------------------------------------------|")
                                                print("upi,card,Net banking")
                                                print("|-------------------------------------------|")
                                                mode = input("Enter mode of payment:")
                                                uid = input("Renter your user id:")
                                                print("|-------------------------------------------|")
                                                print("|-------------------------------------------|")
                                                r = payment(mode , uid)
                                                if r == True:
                                                    print("Your ticket has been booked successfully for the match against",op)
                                                    save(uid , adult , child , league , team , op)
                                                    print("Total cost for your ticket is $",t)
                                                    rec = False
                                                else:
                                                    print("Payment unsuccessful")
                                                    rec = True
                                            else:
                                                print("you can only book 100 tickets at a time")
                                                rec = True
                                        else:
                                            print("|------------------------------Invalid input--------------------------|")
                                            print("|-----------enter a number between 1 and 2 only---------|")
                                            rec = True
                                    elif place == 2:
                                        print("Ticket costs")
                                        print("30$ for adults")
                                        print("15$ for kids below the age of 16")
                                        adult = int(input("Enter number of adults:"))
                                        child = int(input("Enter number of children:"))
                                        if adult + child < 101:
                                                costadult = 30*adult
                                                costchild = 15*child
                                                t = costadult + costchild
                                                print("|-------------------------------------------|")
                                                print("upi,card,Net banking")
                                                print("|-------------------------------------------|")
                                                mode = input("Enter mode of payment:")
                                                uid = input("Renter your user id:")
                                                print("|-------------------------------------------|")
                                                print("|-------------------------------------------|")
                                                r = payment(mode , uid)
                                                if r == True:
                                                    print("Your ticket has been booked successfully for the match against",op)
                                                    save(uid , adult , child , league , team , op)
                                                    print("Total cost for your ticket is $",t)
                                                    rec = False
                                                else:
                                                    print("Payment unsuccessful")
                                                    rec = True
                                        else:
                                            print("you can only book 100 tickets at a time")
                                            rec = True  
                                    else:
                                        print("|------------------------------Invalid input--------------------------|")
                                        print("|---------------------Enter a number between 1 and 2 only-------------|")
                                        rec = True
                                else:
                                    print("|------------------------------Invalid input--------------------------|")
                                    print("|-----------enter a number between 1 and 20 only---------|")
                                    rec = True
                            else:
                                print("|------------------------------Invalid input--------------------------|")
                                print("|---------------------opponent and team cannot be the same-------------|") 
                                rec = True
                        else:
                            print("|------------------------------Invalid input--------------------------|")
                            print("|---------------------Enter a number between 1 and 20 only-------------|")
                            rec = True
                    else:
                        print("Invalid input")
                        rec = True       
                elif league == 4:
                    print()
                    print("You have choosen the Italian Serie A")
                    l = []
                    f = open("serie_a.txt","r",newline = "")
                    a = f.readlines()
                    for i in a:
                        l.append(i)
                    for i in l:
                        if i == '\r\n':
                            l.remove('\r\n')
                        else:
                            continue
                    for i in l:
                        print(i)
                        print("---------")
                    print()
                    x = input("Enter the number of the team you want to watch the match for:")
                    team = recursion(x , l)
                    print()
                    if x in z:
                        if int(x) > 0 and int(x) < 21:
                            x = str(x)
                            for i in l:
                                if i == '\r\n':
                                    l.remove('\r\n')
                                else:
                                    continue
                            for i in l:
                                print(i)
                                print("---------")
                            f.close()
                            print("|-------------------------------------------|")
                            o = input("Enter the number of the opponent:")
                            print("|-------------------------------------------|")
                            print("|-------------------------------------------|")
                            if x != o:
                                if int(x) > 0 and int(x) < 21:
                                    op = recursion(o , l)
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    print("You have choosen to watch for",team,"vs",op)
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    place = int(input("Enter 1 for home game , Enter 2 for away game"))
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    if place == 1:
                                        print("|------You have choosen for home game-----|")
                                        print("|----------Matchday hospitality-------------|","------","(1)")
                                        print("|----------Normal hospitality-----------------|","------","(2)")
                                        hos = int(input("Enter hospitality:"))
                                        if hos == 1:
                                            print("|----------------Ticket costs----------------|")
                                            print("|----------------70$ for adults-------------|")
                                            print("|------55$ for kids below the age of 16-----|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            adult = int(input("Enter number of adults:"))
                                            print()
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            child = int(input("Enter number of children:"))
                                            print()
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            if adult + child < 101:
                                                costadult = 70*adult
                                                costchild = 55*child
                                                t = costadult + costchild
                                                print("upi,card,Net banking")
                                                mode = input("Enter mode of payment:")
                                                uid = input("Renter your user id:")
                                                r = payment(mode , uid)
                                                if r == True:
                                                    print("Your ticket has been booked successfully for the match against",op)
                                                    save(uid , adult , child , league , team , op)
                                                    print("Total cost for your ticket is $",t)
                                                    rec = False
                                                else:
                                                    print("Payment unsuccessful")
                                                    rec = True
                                            else:
                                                print("you can only book 100 tickets at a time")
                                                rec = True
                                        elif hos == 2:
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("Ticket costs")
                                            print("30$ for adults")
                                            print("15$ for kids below the age of 16")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            adult = int(input("Enter number of adults:"))
                                            print("|-------------------------------------------|")
                                            child = int(input("Enter number of children:"))
                                            print("|-------------------------------------------|")
                                            if adult + child < 101:
                                                costadult = 30*adult
                                                costchild = 15*child
                                                t = costadult + costchild
                                                print("|-------------------------------------------|")
                                                print("upi,card,Net banking")
                                                print("|-------------------------------------------|")
                                                mode = input("Enter mode of payment:")
                                                uid = input("Renter your user id:")
                                                print("|-------------------------------------------|")
                                                print("|-------------------------------------------|")
                                                r = payment(mode , uid)
                                                if r == True:
                                                    print("Your ticket has been booked successfully for the match against",op)
                                                    save(uid , adult , child , league , team , op)
                                                    print("Total cost for your ticket is $",t)
                                                    rec = False
                                                else:
                                                    print("Payment unsuccessful")
                                                    rec = True
                                            else:
                                                print("you can only book 100 tickets at a time")
                                                rec = True
                                        else:
                                            print("|------------------------------Invalid input--------------------------|")
                                            print("|-----------enter a number between 1 and 2 only---------|")
                                            rec = True
                                    elif place == 2:
                                        print("Ticket costs")
                                        print("30$ for adults")
                                        print("15$ for kids below the age of 16")
                                        adult = int(input("Enter number of adults:"))
                                        child = int(input("Enter number of children:"))
                                        if adult + child < 101:
                                                costadult = 30*adult
                                                costchild = 15*child
                                                t = costadult + costchild
                                                print("|-------------------------------------------|")
                                                print("upi,card,Net banking")
                                                print("|-------------------------------------------|")
                                                mode = input("Enter mode of payment:")
                                                uid = input("Renter your user id:")
                                                print("|-------------------------------------------|")
                                                print("|-------------------------------------------|")
                                                r = payment(mode , uid)
                                                if r == True:
                                                    print("Your ticket has been booked successfully for the match against",op)
                                                    save(uid , adult , child , league , team , op)
                                                    print("Total cost for your ticket is $",t)
                                                    rec = False
                                                else:
                                                    print("Payment unsuccessful")
                                                    rec = True
                                        else:
                                            print("you can only book 100 tickets at a time")
                                            rec = True  
                                    else:
                                        print("|------------------------------Invalid input--------------------------|")
                                        print("|---------------------Enter a number between 1 and 2 only-------------|")
                                        rec = True
                                else:
                                    print("|------------------------------Invalid input--------------------------|")
                                    print("|-----------enter a number between 1 and 20 only---------|")
                                    rec = True
                            else:
                                print("|------------------------------Invalid input--------------------------|")
                                print("|---------------------opponent and team cannot be the same-------------|") 
                                rec = True
                        else:
                            print("|------------------------------Invalid input--------------------------|")
                            print("|---------------------Enter a number between 1 and 20 only-------------|")
                            rec = True
                    else:
                        print("Invalid input")
                        rec = True       

                elif league == 5:
                    print()
                    print("You have choosen the French Ligue 1")
                    l = []
                    f = open("ligue_1.txt","r",newline = "")
                    a = f.readlines()
                    for i in a:
                        l.append(i)
                    for i in l:
                        if i == '\r\n':
                            l.remove('\r\n')
                        else:
                            continue
                    for i in l:
                        print(i)
                        print("---------")
                    print()
                    x = input("Enter the number of the team you want to watch the match for:")
                    team = recursion(x , l)
                    print()
                    if x in z:
                        if int(x) > 0 and int(x) < 21:
                            x = str(x)
                            for i in l:
                                if i == '\r\n':
                                    l.remove('\r\n')
                                else:
                                    continue
                            for i in l:
                                print(i)
                                print("---------")
                            f.close()
                            print("|-------------------------------------------|")
                            o = input("Enter the number of the opponent:")
                            print("|-------------------------------------------|")
                            print("|-------------------------------------------|")
                            if x != o:
                                if int(x) > 0 and int(x) < 21:
                                    op = recursion(o , l)
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    print("You have choosen to watch for",team,"vs",op)
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    place = int(input("Enter 1 for home game , Enter 2 for away game"))
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    print("|-------------------------------------------|")
                                    if place == 1:
                                        print("|------You have choosen for home game-----|")
                                        print("|----------Matchday hospitality-------------|","------","(1)")
                                        print("|----------Normal hospitality-----------------|","------","(2)")
                                        hos = int(input("Enter hospitality:"))
                                        if hos == 1:
                                            print("|----------------Ticket costs----------------|")
                                            print("|----------------70$ for adults-------------|")
                                            print("|------55$ for kids below the age of 16-----|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            adult = int(input("Enter number of adults:"))
                                            print()
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            child = int(input("Enter number of children:"))
                                            print()
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            if adult + child < 101:
                                                costadult = 70*adult
                                                costchild = 55*child
                                                t = costadult + costchild
                                                print("upi,card,Net banking")
                                                mode = input("Enter mode of payment:")
                                                uid = input("Renter your user id:")
                                                r = payment(mode , uid)
                                                if r == True:
                                                    print("Your ticket has been booked successfully for the match against",op)
                                                    save(uid , adult , child , league , team , op)
                                                    print("Total cost for your ticket is $",t)
                                                    rec = False
                                                else:
                                                    print("Payment unsuccessful")
                                                    rec = True
                                            else:
                                                print("you can only book 100 tickets at a time")
                                                rec = True
                                        elif hos == 2:
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("Ticket costs")
                                            print("30$ for adults")
                                            print("15$ for kids below the age of 16")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            print("|-------------------------------------------|")
                                            adult = int(input("Enter number of adults:"))
                                            print("|-------------------------------------------|")
                                            child = int(input("Enter number of children:"))
                                            print("|-------------------------------------------|")
                                            if adult + child < 101:
                                                costadult = 30*adult
                                                costchild = 15*child
                                                t = costadult + costchild
                                                print("|-------------------------------------------|")
                                                print("upi,card,Net banking")
                                                print("|-------------------------------------------|")
                                                mode = input("Enter mode of payment:")
                                                uid = input("Renter your user id:")
                                                print("|-------------------------------------------|")
                                                print("|-------------------------------------------|")
                                                r = payment(mode , uid)
                                                if r == True:
                                                    print("Your ticket has been booked successfully for the match against",op)
                                                    save(uid , adult , child , league , team , op)
                                                    print("Total cost for your ticket is $",t)
                                                    rec = False
                                                else:
                                                    print("Payment unsuccessful")
                                                    rec = True
                                            else:
                                                print("you can only book 100 tickets at a time")
                                                rec = True
                                        else:
                                            print("|------------------------------Invalid input--------------------------|")
                                            print("|-----------enter a number between 1 and 2 only---------|")
                                            rec = True
                                    elif place == 2:
                                        print("Ticket costs")
                                        print("30$ for adults")
                                        print("15$ for kids below the age of 16")
                                        adult = int(input("Enter number of adults:"))
                                        child = int(input("Enter number of children:"))
                                        if adult + child < 101:
                                                costadult = 30*adult
                                                costchild = 15*child
                                                t = costadult + costchild
                                                print("|-------------------------------------------|")
                                                print("upi,card,Net banking")
                                                print("|-------------------------------------------|")
                                                mode = input("Enter mode of payment:")
                                                uid = input("Renter your user id:")
                                                print("|-------------------------------------------|")
                                                print("|-------------------------------------------|")
                                                r = payment(mode , uid)
                                                if r == True:
                                                    print("Your ticket has been booked successfully for the match against",op)
                                                    save(uid , adult , child , league , team , op)
                                                    print("Total cost for your ticket is $",t)
                                                    rec = False
                                                else:
                                                    print("Payment unsuccessful")
                                                    rec = True
                                        else:
                                            print("you can only book 100 tickets at a time")
                                            rec = True  
                                    else:
                                        print("|------------------------------Invalid input--------------------------|")
                                        print("|---------------------Enter a number between 1 and 2 only-------------|")
                                        rec = True
                                else:
                                    print("|------------------------------Invalid input--------------------------|")
                                    print("|-----------enter a number between 1 and 20 only---------|")
                                    rec = True
                            else:
                                print("|------------------------------Invalid input--------------------------|")
                                print("|---------------------opponent and team cannot be the same-------------|") 
                                rec = True
                        else:
                            print("|------------------------------Invalid input--------------------------|")
                            print("|---------------------Enter a number between 1 and 20 only-------------|")
                            rec = True
                    else:
                        print("Invalid input")
                        rec = True       
    elif m == "2":
        if register() == True:
            print("|--------------------------Registered successfully-------------------------------|")
    else:
        print("|------------------------------Invalid choice--------------------------------------------|")
