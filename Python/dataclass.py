from dataclasses import dataclass
from dataclasses import field


@dataclass(frozen = True)
class People:
    first_name: str
    last_name: str
    age: int
    kids: list = field(default_factory = lambda: [])
    edict: dict = field(default_factory = lambda: {})



if __name__ == "__main__":
    p1 = People("Wallace", "Pitt", 31)
    p2 = People("Esther", "Pitt", 29)


    print(f"Her first name is: {p2.first_name}")
