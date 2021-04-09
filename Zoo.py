class Animals:
  def __init__(self, kind, name):
    self.kind = kind
    self.name = name
    self.happy = True
    self.health = True
  def display_info(self):
    print(self.kind, self.name, "1.Is happy?", self.happy,"/ 2.Good health?" ,self.health)
    return self

class Lion(Animals):
  def __init__(self, kind, name):
    super().__init__(kind, name)

class Tiger(Animals):
  def __init__(self, kind, name):
    super().__init__(kind, name)
    self.happy = False

class Bear(Animals):
  def __init__(self, kind, name):
    super().__init__(kind, name)
    self.health = False

class Zoo:
  def __init__(self, zoo_name):
    self.animals = []
    self.name = zoo_name

  def add_lion(self, name):
    self.animals.append(Lion("Lion",name))
    return self

  def add_tiger(self, name):
    self.animals.append(Tiger("Tiger",name))
    return self

  def add_bear(self, name):
    self.animals.append(Bear("Bear",name))
    return self   

  def print_all_info(self):
    print("-"*30, self.name, "_"*30)
    for animal in self.animals:
      animal.display_info()


zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.add_bear("Yogi Bear")
zoo1.print_all_info()