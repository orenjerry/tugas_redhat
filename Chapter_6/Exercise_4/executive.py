from manager import Manager

class Executive(Manager):
    def pension(self):
        return self.years * (0.30 * self.salary)