from utlis import *
from record import irecord
ct=0
def withdraw():
    global ct
    if(account== []):
        print("No balance to Withdraw!!!")
    else:
        wd=int(input("Enter the Amount You want to Withdraw"))
        if(wd>account[0]):
            print("Insufficient Balance to Withdraw!!!!")
        else:
            account[0]-=wd
            print(f"Amount of {wd} has been Successfully Debited!!!")
            ct+=1
            irecord(f"Withdraw{ct}",wd)
