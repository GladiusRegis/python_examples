class A:
    def run(self):
        print('method in A')


class B:
    def run(self):
        print('method in B')


class Child(A, B):
    def go(self):
        self.run()


a = Child()
a.go()
