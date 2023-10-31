# Given parameters
diameter = 0.50  # m
N = 5
Vinlet = 20  # m/s
T_gas = 345  # K
viscosity_air = 0.0745  # kg/m-h
particle_size = 10e-6  # m (10 µm)
particle_density = 1.2e3  # g/cm³ to kg/m³
rho_g = 1.2041  # kg/m³

# Calculate the cross-sectional area of the cyclone at the inlet
A = math.pi * (diameter / 2) ** 2

# Calculate gas flow rate (Q)
Q = A * Vinlet

# Calculate the tangential velocity (Vt)
R = diameter / 2
Vt = (2 * math.pi * N * R) / 60

# Calculate the cut diameter (dpc)
dpc = (9 * viscosity_air * Q) / (2 * math.pi * rho_g * Vt)

# Calculate the separation factor (S)
S = Vt / (viscosity_air * dpc)

# Calculate the pressure drop (ΔP)
pressure_drop = (rho_g * Vt ** 2) / (2 * R)

print(f"(a) Cut Diameter (dpc): {dpc} meters")
print(f"(b) Separation Factor (S): {S}")
print(f"(c) Pressure Drop: {pressure_drop} Pa")
