class check_itter:
    def __init__(self, start, end=10) -> None:
        self.start = start
        self.end = end

    def __iter__(self):
        if self.start:
            self.a = self.start
        else:
            self.a = 1
        return self

    def __next__(self):
        if self.a <= self.end:
            tmp = self.a
            self.a += 1
            return tmp
        else:
            raise StopIteration


myClass = check_itter(10)
myIter = iter(myClass)

for _ in myIter:
    print(_)
