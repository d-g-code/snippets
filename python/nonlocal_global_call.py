"""
The nonlocal keyword is used to work with variables inside nested functions.
The global keyword is used to create global variables from a no-global scope.
Overloading operators makes the class resemble a function callable. The __call__ method intercepts direct call to
an instance so there is no need to call the method.
"""


def tester(start):
    state = start

    def nested(label):
        # nonlocal stat SyntaxError: no binding for nonlocal 'stat' found
        print(label, state)
        # state += 1 UnboundLocalError: local variable 'state' referenced before assignment
    return nested


a = tester(0)
a('spam')
a('ham')
print(20 * '-', 'tester_nonlocal', 20 * '-')


def tester_nonlocal(start):
    state_nonlocal = start

    def nested_1(label):
        nonlocal state_nonlocal
        print(label, state_nonlocal)
        state_nonlocal += 1
    return nested_1


b = tester_nonlocal(0)
b('be')
b('become')
b('begin')
print(20 * '-', 'tester_global', 20 * '-')

global state_global


def tester_global(start):
    global state_global
    state_global = start

    def nested_global(label):
        global state_global
        print(label, state_global)
        state_global += 1
    return nested_global


g = tester_global(0)
g('get')
g('give')
h = tester_global(10)
h('have')
g('go')
print(20 * '-', 'tester_class', 20 * '-')


class TesterClass:
    def __init__(self, start):
        self.state_class = start

    def nested_class(self, label_class):
        print(label_class, self.state_class)
        self.state_class += 1


C = TesterClass(0)
C.nested_class('Choose')
C.nested_class('Chose')
C.nested_class('Chosen')
B = TesterClass(10)
B.nested_class('Buy')
B.nested_class('Bought')
print(20 * '-', 'tester_class_call', 20 * '-')


class TesterClassCall:
    def __init__(self, start):
        self.state_class_call = start

    def __call__(self, label_class_call):
        print(label_class_call, self.state_class_call)
        self.state_class_call += 1


D = TesterClass(0)
D.nested_class('Draw')
D.nested_class('Drew')
D.nested_class('Drawn')
E = TesterClass(10)
E.nested_class('Ete')
E.nested_class('Ate')
E.nested_class('Eaten')
