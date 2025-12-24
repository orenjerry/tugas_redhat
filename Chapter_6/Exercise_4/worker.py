class Worker:
    def __init__(self, name, salary, years):
        self.name = name
        self.salary = salary
        self.years = years

    def pension(self):
        return self.years * (0.10 * self.salary)

    def name(self):
        return self.name