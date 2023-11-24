from typing import Optional

class Person:

    def __init__(self, fname, lname, num = 0):
        self.fname = fname
        self.lname = lname
        self.num = num

    def __enter__(self):
        print(f"entering People Class")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Leaving people class with: {self.fname} {self.lname}")

    def add(self, x: Optional[int] = 1):
        self.num += x
        print(f"The sum is: {self.num}")

    def sub(self, x: Optional[int] = 0):
        self.num -= x
        print(f"The difference is: {self.num}")

def greet(fname: str = "Willy", lname: Optional[str] = None) -> None:
    if lname:
        print(f"first name is {fname} and last name is {lname}")
    else:
        print(f"My name is {fname}")




if __name__ == "__main__":
    greet("Champ", "Pitts")
    with Person(fname = "champ", lname = "pitts") as champ:
        champ.add()
        champ.sub(10)