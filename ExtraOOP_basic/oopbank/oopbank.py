# 定義方法
# 物件方法第一個參數一定是物件本身
# 通過 mypy 的型態檢查，必須明確地撰寫 -> None
class Account:
    def __init__(self, name: str, number: str, balance: float) -> None:
        self.__name = name
        self.__number = number
        self.__balance = balance
    # 限定使用 self.name 取得值
    # Uniform access principle @property
    @property
    def name(self) -> str:
        return self.__name

    @property
    def number(self) -> str:
        return self.__number

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float):
        if amount <= 0:
            print('存款金額不得為負')
        else:
            self.__balance += amount

    def withdraw(self, amount: float):
        if amount > self.__balance:
            print('餘額不足')
        else:
            self.__balance -= amount

    def __str___(self):
        return f"Account:(' {self.__name}','{self.__number}','{self.__balance}')"

