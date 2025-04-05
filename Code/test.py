import random
# Exemple de tableau de valeurs aléatoires pour 10 points
gradients = [random.random() * 2 - 1 for _ in range(1000)]

def fade(t):
    return t ** 3 * (t * (t * 6 - 15) + 10)

def perlin_noise(x, gradients):
    x1 = int(x)
    x2 = x1 + 1
    t = x - x1
    fade_t = fade(t)
    return 20*((1 - fade_t) * gradients[x1 % len(gradients)] + fade_t * gradients[x2 % len(gradients)])


def perlin_noise_octave(x, gradients, octaves=19, persistence=0.5):
    total = 0
    frequency = 1
    amplitude = 1
    max_value = 0  # Utilisé pour normaliser le bruit

    for _ in range(octaves):
        total += perlin_noise(x * frequency, gradients) * amplitude
        max_value += amplitude
        amplitude *= persistence
        frequency *= 2

    return total / max_value  # Normalisation

noise_values = []
# Exemple d'utilisation
for x in range(1000):
    noise_values.append(int(perlin_noise_octave(x/100, gradients)))
    
print(noise_values)