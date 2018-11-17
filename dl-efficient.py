import sys, re
from math import ceil, sqrt

def pow_x(g_base,a,p_mod):
  x=1
  bits = "{0:b}".format(a)
  for i, bit in enumerate(bits):
    if bit=='1':
        x = (((x**2)*g_base)%p_mod)
    elif bit=='0':
        x = ((x**2)%p_mod)
  return x%p_mod

def babyStepGiantStep(p, g, h):
    N = ceil(sqrt(p - 1))
    table = {pow_x(g, i, p): i for i in range(N)}
    c = pow_x(g, N * (p - 2), p)
    for j in range(N):
        y = (h * pow_x(c, j, p)) % p
        if y in table:
            return j * N + table[y]
    return None

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as my_file1:
        content = my_file1.readlines()
        #Prime P
        x = content[0].split(',')[0]
        pattern = re.findall('\d+', x)
        p = int(pattern[0])
        #Generator g
        y = content[0].split(',')[1]
        pattern = re.findall('\d+', y)
        g = int(pattern[0])
        #g to the power a
        z = content[0].split(',')[2]
        pattern = re.findall('\d+', z)
        ga = int(pattern[0])
        #print(p, g, ga)

    a = babyStepGiantStep(p, g, ga)
    if a:
        print(a)
    else:
        print("Exponent not found.")
