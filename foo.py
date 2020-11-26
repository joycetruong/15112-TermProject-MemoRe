class TA(object):
    tadict = {}

    def __init__(self, name, number):
        self.name, self.number = name, number
        TA.tadict[self.number] = self

    def __repr__(self):
        return f'{self.name}_{self.number}'

    @staticmethod
    def getTA(n):
        return TA.tadict.get(n, None)

ta1 = TA("Kian", 42)
print(TA.getTA(42))