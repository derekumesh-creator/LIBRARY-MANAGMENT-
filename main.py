from deposit import deposit
from withdraw import withdraw
from display import display
from record import record
def ATM():
    while True:
        print('''    1. Deposit
    2. Withdrawal
    3. Transactions Records  
    4. Display balance 
    5. Exit ''')
        ch=int(input("Enter The Valid Choice"))
        if (ch==1):
            deposit()
        elif(ch==2):
            withdraw()
        elif (ch==3):
            record()
        elif(ch==4):
            display()
        elif(ch==5):
            print("Thanks For Rohit ATM Service")
            break
        else:
            print("Invalid Number!!!")

        
        
ATM()
    