import oopbank

acct = oopbank.Account('Justn','123-456', 1000)
acct.deposit(500)
acct.withdraw(200)

print("帳戶名稱:", acct.name)
print("帳戶號碼:", acct.number)
print("帳戶餘額:", acct.balance)