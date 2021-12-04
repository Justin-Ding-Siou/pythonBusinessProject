from OOP_basic.bank import bank

acct = bank.account('Justin', '123-456', 1000)
bank.deposit(acct, 500)
bank.withdraw(acct, 200)

print(bank.desc(acct))