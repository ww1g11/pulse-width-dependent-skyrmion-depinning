using DifferentialEquations
using NPZ
using Printf

eta = 1.2
alpha = 0.05;
beta = 0.1;

gamma = 2.21e5
mu_0 = pi*4e-7
L = 2e-9
Ms = 3.87e5
rho = gamma/(mu_0*Ms*L)

k_B = 1.38e-23
T = 100
D = alpha*eta*k_B*T/(1+alpha*alpha*eta*eta)*rho/(4*pi)
println("D=", D)

sigma = 11.988e-9
A = 0.945e9
#A = 0

count=0

function Force_X(x,y)
    return -2*A*exp(-(x^2+y^2)/sigma^2)*((x^2+y^2)/sigma^2-1)*x
end

function Force_Y(x,y)
    return -2*A*exp(-(x^2+y^2)/sigma^2)*((x^2+y^2)/sigma^2-1)*y
end

function rhs(dx, x, p, t)
    u = p[1]
    Fx = Force_X(x[1], x[2])
    Fy = Force_Y(x[1], x[2])
    dx[1] = (-Fy + alpha*eta*Fx + (1+alpha*beta*eta^2)*u)/(1+alpha^2*eta^2)
    dx[2] = (Fx+ alpha*eta*Fy -(alpha-beta)*eta*u)/(1+alpha^2*eta^2)
    return
end

function G(dx,x,p,t)
    d = sqrt(2*D)/(1+alpha^2*eta^2)
    dx[1,1] = d
    dx[1,2] = alpha*eta*d
    dx[2,1] = -alpha*eta*d
    dx[2,2] = d
end

function compute_xy!(all, u, id)
    prob = SDEProblem(rhs, G, [0, 0.0], [0, 20e-9], [u], noise_rate_prototype=zeros(2,2))
    sol = solve(prob,SRA2(),dt=1e-13, saveat=2e-10, abstol=1e-10, reltol=1e-10)
    #print("count:", count)
    for i = 1:101
        all[id, i, 1] = sol.u[i][1]
        all[id, i, 2] = sol.u[i][2]
    end
    return nothing
end

function run_all_u(u, N=10000)
    name = @sprintf("xy_%g.npy", u)
    if isfile(name)
        return 
    end
    all = zeros(N, 101, 2)
    for i=1:N
        print(i," ")
        compute_xy!(all, u, i)
    end
    
    npzwrite(name, all)
end

for i = 0:30
    run_all_u(i*0.2)
end
