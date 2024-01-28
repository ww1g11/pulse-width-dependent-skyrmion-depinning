using JuMag
using Printf
using NPZ

JuMag.cuda_using_double(true)

function init_single_skx(i,j,k, dx, dy, dz)
    if (i-30)^2 + (j-60)^2 < 20^2
        return (0,0.1,-1)
    end
    return (0,0,1)
end


function spatial_Ku(i,j,k,dx,dy,dz)
    r = (i-30)^2 + (j-60)^2
    if r <= 10
       return 4e4
    end
    return 0
end

function relax_system(R=6)

  mesh =  FDMeshGPU(nx=200, ny=120, nz=1, dx=1e-9, dy=1e-9, dz=2e-9, pbc="xy")
  sim = Sim(mesh, driver="SD", name="relax")
  set_Ms(sim, 3.87e5)

  mu0 = 4*pi*1e-7
  mT = 0.001/mu0
  A = 5.2e-12
  L = 60e-9
  D = 4*pi*A/L
  add_exch(sim, A)
  add_dmi(sim, D)
  add_zeeman(sim, (0,0,260*mT))
  add_anis(sim, spatial_Ku)

  init_m0(sim, init_single_skx)

  relax(sim, maxsteps=10000, stopping_dmdt=0.1, save_vtk_every = -1)
  npzwrite("skyrmion.npy", Array(sim.spin))
end

function compute_guiding_center(sim)
    Rxs, Rys = JuMag.compute_guiding_center(Array(sim.spin), sim.mesh)
    return Rxs[1]*1e9, Rys[1]*1e9
end

function run_dynamics(;u0=10, pulse_width=5e-9)


  mesh =  FDMeshGPU(nx=200, ny=120, nz=1, dx=1e-9, dy=1e-9, dz=2e-9, pbc="xy")
  sim = Sim(mesh, driver="LLG_STT", name="dyn")
  sim.driver.alpha = 0.05
  sim.driver.beta = 0.1
  sim.driver.gamma = 2.21e5
  sim.driver.ode.tol = 1e-5

  set_Ms(sim, 3.87e5)

  mu0 = 4*pi*1e-7
  mT = 0.001/mu0
  A = 5.2e-12
  L = 60e-9
  D = 4*pi*A/L
  add_exch(sim, A)
  add_dmi(sim, D)
  add_zeeman(sim, (0,0,260*mT))
  add_anis(sim, spatial_Ku)

  set_ux(sim, -u0)

  init_m0(sim, npzread("skyrmion.npy"))
  Rx0, Ry0 =  compute_guiding_center(sim)
  
  run_until(sim, pulse_width, save_data=false)

  set_driver(sim, driver="SD")

  relax(sim, maxsteps=10000, stopping_dmdt=0.1, save_vtk_every = -1)
  Rx, Ry =  compute_guiding_center(sim)
  ds = sqrt((Rx-Rx0)^2 + (Ry-Ry0)^2)
  if ds<2
    return false
  else
  	return true
  end
end


function find_uc(pulse_width)
    u1 = 0
    u2 = 32
    u = (u1+u2)/2
    for i = 1:9
        println("u= ", u)
        u = (u1+u2)/2
        moved = run_dynamics(u0=u, pulse_width=pulse_width)
        if moved
            u2 = u
        else
            u1 = u
        end
    end
    return u
end


relax_system()
f = open("uc.txt", "w")
write(f, "#pulse_width    uc\n")
close(f)
for p in [1, 2, 3, 4, 5, 6, 7, 8, 10]
    uc = find_uc(p*1e-9)
    ic = p*1e-9
    f = open("uc.txt", "a")
    print("#-------------------------------------", ic, uc)
    write(f, "$ic  $uc \n")
    close(f)
end

