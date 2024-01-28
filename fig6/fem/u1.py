from ast import Expression
from collections import UserDict
from fenics import *
import dolfin as df
import numpy as np

eta = 1.2
alpha = 0.05
beta = 0.1

gamma = 2.21e5
mu_0 = np.pi*4e-7
L = 2e-9
Ms = 3.84e5
rho = gamma/(mu_0*Ms*L)

k_B = 1.38e-23
T = 300
D = alpha*eta*k_B*T/(1+alpha*alpha*eta*eta)*rho/(4*np.pi)*1e9
print("D=", D)

sigma = 11.988
A = 0.945

u0=0

def force_x(x,y):
    return -2*A*np.exp(-(x**2+y**2)/sigma**2)*((x**2+y**2)/sigma**2-1)*x


def force_y(x,y):
    return -2*A*np.exp(-(x**2+y**2)/sigma**2)*((x**2+y**2)/sigma**2-1)*y


class ExpressionA(UserExpression):
    def eval(self, value, xyz):
        x = xyz[0]
        y = xyz[1]
        Fx = force_x(x, y)
        Fy = force_y(x, y)
        value[0] = (-Fy + alpha*eta*Fx + (1+alpha*beta*eta**2)*u0)/(1+alpha**2*eta**2)
        value[1] = (Fx+ alpha*eta*Fy -(alpha-beta)*eta*u0)/(1+alpha**2*eta**2)
        value[2] = 0
    
    def value_shape(self):
        return (3, )


mesh = df.Mesh('R24.xml')

V = FunctionSpace(mesh, 'P', 1)
Vv = VectorFunctionSpace(mesh, 'P', 1)

# Define boundary condition
u_D = Expression('0',  element=V.ufl_element())
Aexp = ExpressionA(Vv.ufl_element())

def boundary(x, on_boundary):
    return on_boundary

bc = DirichletBC(V, u_D, boundary)
# Define variational problem
u = TrialFunction(V)
v = TestFunction(V)

a = D*dot(grad(u), grad(v))*dx  - dot(grad(u), Aexp)*v*dx
L = v*dx

# Compute solution
u = Function(V)
solve(a == L, u, bc)
# Plot solution and mesh

print(u(0,0,0))

# Save solution to file in VTK format
vtkfile = File('u/u0.pvd')
u.rename("f", "u")
vtkfile << u