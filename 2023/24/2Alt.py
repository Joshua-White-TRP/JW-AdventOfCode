import z3

infile = open("Input.txt")

pos = []
vel = []

for line in infile:
    p, v = line.strip().split(" @ ")
    pos.append(tuple(map(float, p.split(", "))))
    vel.append(tuple(map(float, v.split(", "))))

x = z3.Real('x')
y = z3.Real('y')
z = z3.Real('z')
vx = z3.Real('vx')
vy = z3.Real('vy')
vz = z3.Real('vz')

s = z3.Solver()

for i in range(len(pos)):
    px_i, py_i, pz_i = pos[i]
    vx_i, vy_i, vz_i = vel[i]
    t_i = z3.Real(f"t_{i}")
    s.add(px_i + vx_i * t_i == x + vx * t_i)
    s.add(py_i + vy_i * t_i == y + vy * t_i)
    s.add(pz_i + vz_i * t_i == z + vz * t_i)

s.check()
m = s.model()
print(m[x], m[y], m[z])
print(m[vx], m[vy], m[vz])
print(int(str(m[x])) + int(str(m[y])) + int(str(m[z])))