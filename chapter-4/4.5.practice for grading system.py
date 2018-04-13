print("Find a grade of a exam result:-")
from time import clock
start=clock()
mark = eval(input("Please enter the exam mark:"))
if mark <40:
    print("You have got F grade")
else:
    if mark>=40 and mark<45:
        print("You have got D grade")
    else:
        if mark>=45 and mark<50:
            print("You have got C grade")
        else:
            if mark>=50 and mark<55:
                print("You have got C+ grade")
            else:
                if mark>=55 and mark<60:
                    print("You have got B- grade")
                else:
                    if mark>=60 and mark<65:
                        print("You have got B grade")
                    else:
                        if mark>=65 and mark<70:
                            print("You have got B+ grade")
                        else:
                            if mark>=70 and mark<75:
                                print("You have got A- grade")
                            else:
                                if mark>=75 and mark<80:
                                    print("You have got A grade")
                                else:
                                    if mark>=80 and mark<100:
                                        print("You have got A+ grade")
print("End")
elapsed=clock()-start
print("The program is done within", elapsed,"seconds")
                                    
            
