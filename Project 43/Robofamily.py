class Robo:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"{self.name} is talking in binary")
    def charge(self):
        print(f"{self.name} is charging with electricity")

Robo1 = Robo("Robo1")
Robo1.talk()
Robo1.charge()

print("\nCreating Next samll robo........")
favRobo = Robo("favRobo")
favRobo.talk()
favRobo.charge()