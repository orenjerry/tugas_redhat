from person import Person
from family import Family

def main():
    mother = Person("Mom", 45, "F")
    father = Person("Dad", 45, "M")
    kid1 = Person("Johnie", 2, "M")
    kid2 = Person("Janie", 3, "F")

    myFamily = Family(mother, father, kid1, kid2)
    kid3 = Person("Paulie", 1, "M")
    myFamily.add(kid3)

    print(myFamily)

    smiths = Family(mother, father, kid1)

    if myFamily > smiths:
        print("we have more kids than smiths")
    if myFamily == smiths:
        print("families have same # of kids")
    if myFamily < smiths:
        print("we have fewer kids than smiths")

if __name__ == "__main__":
    main()