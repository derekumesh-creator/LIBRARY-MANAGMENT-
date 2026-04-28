from utlis import account
from record import irecord
ct=0
def deposit():
    global ct
    dep=int(input("Enter the Deposit Amount"))
    if len(account)==0:
        account.append(dep)
        ct+=1
    else:
        account[0]+=dep
        ct+=1
    print(f"Amount of {dep} is Deposited in Your Account Successfully!!!")
    irecord(f"Deposit{ct}",dep)
