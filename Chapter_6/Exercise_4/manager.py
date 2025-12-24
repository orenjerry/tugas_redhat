from worker import Worker

class Manager(Worker):
    def pension(self):
        return self.years * (0.20 * self.salary)