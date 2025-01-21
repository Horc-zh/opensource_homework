from z3 import *

chicken, rabbits = z3.Ints("chicken rabbits")
z3.solve(
    chicken >= 1,  # number of chicken
    rabbits >= 1,  # number of rabbits
    chicken + rabbits == 35,
    chicken * 2 + rabbits * 4 == 94,
)


circle, square, triangle = Ints("circle square triangle")
s = Solver()
s.add(circle + circle == 10)
s.add(circle * square + square == 12)
s.add(circle * square - triangle * circle == circle)
print(s.check())
print(s.model())

from z3 import *

a, b, c, d, e, f = z3.Ints("a b c d e f")
z3.solve(
    Distinct(a, b, c, d, e, f),
    a >= 0,
    a <= 5,
    b >= 0,
    b <= 5,
    c >= 0,
    c <= 5,
    d >= 0,
    d <= 5,
    e >= 0,
    e <= 5,
    f >= 0,
    f <= 5,
    f != 5,
    f == 2,
    a >= 4,
    a != 5,
    d != 0,
    d >= 2,
    d <= 3,
    c != 0,
    c != 5,
)


Q = [Int("Q_%i" % (i + 1)) for i in range(8)]

# Each queen is in a column {1, ... 8 }
val_c = [And(1 <= Q[i], Q[i] <= 8) for i in range(8)]

# At most one queen per column
col_c = [Distinct(Q)]

diag_c = [
    If(i == j, True, And(Q[i] - Q[j] != i - j, Q[i] - Q[j] != j - i))
    for i in range(8)
    for j in range(i)
]

solve(val_c + col_c + diag_c)

x = Int("x")
y = Int("y")
f = Function("f", IntSort(), IntSort())
s = Solver()
s.add(f(f(x)) == x, f(x) == y, x != y)
print(s.check())
m = s.model()
print("f(f(x)) =", m.evaluate(f(f(x))))
print("f(x)    =", m.evaluate(f(x)))
