# 鄧義在類別，本質在函數
class Rational:
    def __init__(self, numer: int, denom: int) -> None:
        self.numer = numer
        self.denom = denom
    # '+'
    def __add__(self, that):
        return Rational(
            self.numer * that.denom + that.numer * self.denom,
            self.denom  * that.denom
        )
    # '-'
    def __sub__(self, that):
        return Rational(
            self.numer * that.denom - that.numer * self.denom,
            self.denom  * that.denom
        )
    # '/*'
    def __mul__(self, that):
        return Rational(
            self.numer * that.numer,
            self.denom  * that.denom
        )
    # '/'
    def __truediv__(self, that):
        return  Rational(
            self.numer * that.numer,
            self.denom * that.denom
        )

    # str()用於為最終用戶創建輸出，而repr()主要用於調試和開發。 repr的目標是明確明確，str的可讀性
    def __str__(self):
        return f'{self.numer}/{self.denom}'

    def __repr__(self):
        return f'Rational({self.numer}, {self.denom})'
