class Family:
    def __init__(self, parent1, parent2, *children):
        self.parent1 = parent1
        self.parent2 = parent2
        self.children = list(children)

    def add(self, child):
        self.children.append(child)

    def __str__(self):
        hasil = []
        hasil.append("Parents:")
        hasil.append(str(self.parent1))
        hasil.append(str(self.parent2))
        hasil.append("Children:")
        for child in self.children:
            hasil.append(str(child))
        return "\n".join(hasil)
    
    def __lt__(self, other):
        return len(self.children) < len(other.children)

    def __eq__(self, other):
        return len(self.children) == len(other.children)

    def __gt__(self, other):
        return len(self.children) > len(other.children)