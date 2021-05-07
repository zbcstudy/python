import sympy

# 求定积分
x = sympy.symbols('x')
f = 2 * x
result = sympy.integrate(f, (x, 0, 1))
print(result)
print(sympy.pi)
