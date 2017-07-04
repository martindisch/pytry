class Base:
    def print_name(self):
        print "Base"

    def use_print(self):
        self.print_name()

class NewClass(Base):
    def print_name(self):
        print "NewClass"

    def print_parent(self):
        Base.print_name(self)

b = Base()
n = NewClass()

b.use_print()
n.use_print()
