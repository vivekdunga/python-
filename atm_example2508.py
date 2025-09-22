ac_data=["1234 5678 9012","3456 7890 1234","5678 9012 3456"]
data={"1234 5678 9012":[1234,5000.00],"3456 7890 1234":[3456,7000.00],"5678 9012 3456":[5678,10000.00]}
print("welcome")
ac_no=str(input("enter card number: "))
# balance=10000.00
if ac_no in ac_data:
   pin_no=int(input("enter your pin number: "))
   if data[ac_no][0]==pin_no:
      balance=data[ac_no][1]
      print("welcome  xyz")
      x="deposit"
      y="withdrawl"
      z="mini-statement"
      requirmnt=input("enter your requirement from deposit |withdrawl |mini-statement:")
      if requirmnt=="x":
          print("welcome to deposite section")
          depst_amt=float(input("enter deposital amount:"))
          balance+=depst_amt
          data[ac_no][1]=balance
          print("your total balance:",balance)
      elif requirmnt=="y":
         print("welcome to withdrawl section")
         withdrawl_amt=float(input("enter withdrawl amont"))
         if withdrawl_amt<=balance:
            print(" collect the amount")
            balance-=withdrawl_amt
            data[ac_no][1]=balance
            print("your total balance:",balance)

         else:

              print("sorry insuffecient funds")
      elif requirmnt=="z":
         print("your account balance is :",balance)

      else:
         print(("please   enter  deposit |withdrawl |mini-statement:"))

   else:
      print("please  enter valid pin")
      

else:
   print("enter a valid card number")
