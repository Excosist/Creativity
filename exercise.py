from dataclasses import dataclass
@dataclass
class Temp1:
    Temp1__slots__ = ['a', 'b']
    a: int
    b: int=0
temp=Temp1(1)
print(temp.a)