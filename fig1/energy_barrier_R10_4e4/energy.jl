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

function run_dynamics(;u0=10, pulse_width=10e-9)


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


  f = open("energy.txt", "w")
  write(f, "# X     Y    total_energy\n")

  Rx0, Ry0 =  compute_guiding_center(sim)
  JuMag.effective_field(sim, sim.spin, 0.0)
  energy = sum(sim.energy)

  write(f, "$Rx0  $Ry0  $energy\n")

  for i=1:80
    t = i*1e-10
    run_until(sim, t, save_data=false)
    JuMag.effective_field(sim, sim.spin, 0.0)
    Rx0, Ry0 =  compute_guiding_center(sim)
    energy = sum(sim.energy)
    write(f, "$Rx0  $Ry0  $energy\n")
  end
  close(f)
  
end


relax_system()
run_dynamics()

