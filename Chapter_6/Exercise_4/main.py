from worker import Worker
from manager import Manager
from executive import Executive

def main():
    w = Worker("Alice", 50000, 10)
    m = Manager("Bob", 80000, 10)
    e = Executive("Carol", 120000, 10)

    print("Worker pension:", w.pension())
    print("Manager pension:", m.pension())
    print("Executive pension:", e.pension())

if __name__ == "__main__":
    main()