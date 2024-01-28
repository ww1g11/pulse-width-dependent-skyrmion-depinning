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
L = 150e-9
Ms = 3.87e5
rho = gamma/(mu_0*Ms*L)

k_B = 1.38e-23
T = 300
D = alpha*eta*k_B*T/(1+alpha*alpha*eta*eta)*rho/(4*np.pi)*1e9
print("D=", D)

sigma = 11.988*1.5
A = 0.945*0.1

def force_x(x,y):
    return -2*A*np.exp(-(x**2+y**2)/sigma**2)*((x**2+y**2)/sigma**2-1)*x


def force_y(x,y):
    return -2*A*np.exp(-(x**2+y**2)/sigma**2)*((x**2+y**2)/sigma**2-1)*y


def boundary(x, on_boundary):
    return on_boundary

class ExpressionA(UserExpression):
    def eval(self, value, xyz):
        x = xyz[0]
        y = xyz[1]
        Fx = force_x(x, y)
        Fy = force_y(x, y)
        value[0] = (-Fy + alpha*eta*Fx + (1+alpha*beta*eta**2)*self.u0)/(1+alpha**2*eta**2)
        value[1] = (Fx+ alpha*eta*Fy -(alpha-beta)*eta*self.u0)/(1+alpha**2*eta**2)
        value[2] = 0
    
    def value_shape(self):
        return (3, )

def compute_mean_time(u0=1):

    mesh = df.Mesh('R36.xml')

    V = FunctionSpace(mesh, 'P', 1)
    Vv = VectorFunctionSpace(mesh, 'P', 1)

    # Define boundary condition
    u_D = Expression('0',  element=V.ufl_element())
    Aexp = ExpressionA(Vv.ufl_element())
    Aexp.u0=u0

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

    return u(0,0,0)

us = np.linspace(0.1, 2, 20)
ts = []
for u in us:
    ts.append(compute_mean_time(u))

print(ts)
print(us)
np.savetxt("time_T300.txt", np.array(np.transpose([us, ts])))