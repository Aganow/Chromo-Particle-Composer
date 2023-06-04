from ChromoParticleComposer import ChromoParticleComposer

# Create an instance of ChromoParticleComposer
composer = ChromoParticleComposer(num_particles=10, num_dimensions=3)

# Compose particles
best_compositions = composer.compose_particles()

# Print the best compositions
print("Best Compositions:")
for i, composition in enumerate(best_compositions):
    print(f"Particle {i+1}: {composition}")
