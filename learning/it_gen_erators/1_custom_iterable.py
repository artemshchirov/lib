import dataclasses


@dataclasses.dataclass
class MyRange:
    start: int
    end: int
    current: int = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


first_range = MyRange(10, 20)
for number in first_range:
    print(number)
