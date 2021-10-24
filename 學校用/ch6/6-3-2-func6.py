from datetime import datetime
def ymd():
    now = datetime.now()
    return (now.year, now.month, now.day)
y, m, d = ymd()
print(y,m,d)