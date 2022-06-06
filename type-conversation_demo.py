'''
    Dairenin Alanı : pi*r**2
    Dairenin Çevresi: 2*pi*r


'''

#Benim Çözümüm
# pi = 3.14
# yaricap = 3.14

# daireAlan = int(pi *(yaricap**2))
# print(daireAlan)

# daireCevre = int(2 * pi *yaricap)
# print(daireCevre)

#Hocanın Çözümü
yariCap = float(input("yarı çap: "))
pi = 3.14
alan = pi * (yariCap ** 2)
cevre = 2 * pi * yariCap


print('Alan: '+ str(alan), 'Çevre= ' + str(cevre))
