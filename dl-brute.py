import sys, re

def pow_x(g_base,a,p_mod):
  x=1
  bits = "{0:b}".format(a)
  for i, bit in enumerate(bits):
    if bit=='1':
        x = (((x**2)*g_base)%p_mod)
    elif bit=='0':
        x = ((x**2)%p_mod)
  return x%p_mod

def attack(p, g, ga):
    for mystry_a in range(p):
        if pow_x(g, mystry_a, p) == ga:
            return mystry_a
    return 0


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


    a = attack(p, g, ga)
    if a:
        print(a)
    else:
        print("Exponent not found.")
