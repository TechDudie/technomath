class Number:
    def __init__(self, number):
        self.integer = [0]
        self.post_decimal = [0]
        self.floor = int("".join(self.integer))
        self.ceil = int("".join(self.integer)) + 1
        self.value = float(f"{''.join(self.integer)}.{''.join(self.decimal)}")
        self.str = f"{''.join(self.integer)}.{''.join(self.decimal)}"

class Fraction:
    def __init__(self):
        pass

class Polynomial:
    def __init__(self):
        pass