from qmsolve import eV, Å, Hamiltonian, SingleParticle, init_visualization

# define the interaction potential
def harmonic_oscillator(particle):
    k = 100.0 * eV / Å**2
    return 0.5 * k * particle.x**2


# define the Hamiltonian
H = Hamiltonian(
    particles=SingleParticle(),
    potential=harmonic_oscillator,
    spatial_ndim=1,
    N=512,
    extent=20 * Å,
)

eigenstates = H.solve(max_states=30)
print(eigenstates.energies)  # The printed energies are in eV.
