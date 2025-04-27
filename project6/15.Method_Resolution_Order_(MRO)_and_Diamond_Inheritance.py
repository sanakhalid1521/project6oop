class A:
    def show(self):
        print("A's show()")

class B(A):
    def show(self):
        print("B's show()")

class C(A):
    def show(self):
        print("C's show()")

class D(B, C):
    pass

# Object creation
obj = D()
obj.show()  # MRO decides which show() is called
