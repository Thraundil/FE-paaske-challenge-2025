### FE gækkebrev 2025
### Af Emil 'Dota' Bak

brev1 = [1956,1998,1953,1983,1998,1953,1956,1952,1956,1981]
brev2A = [1956,1998,1985,1979,1954,1950,2003,1952,1953,1981,1979,1952,1985,1954,1957,1963,1999,1998,1956,1985,1998,1950,1985,1985,1953,1954]
brev2B = [1981,1953,1998,1962,1952,1956,2003,1953,1952,1956,2003,1950,1971,1953,1954,1963,1953,1981,1971,1979,1963,1985,1953,1971,1956,1963,1958,1953,1955,1998,1953]
brev3 = [4200,4227,4285,4247,4200,4271,4244,4232,4285,4247,4242,4255,4285,4242,4241,4265,4227,4271,4211,4251,4242,4255,4288,4224,4268,4271,4285,4241,4268,4227,4241,4241,4285,4211,4251,4227,4268,4232,4200,4271,4247,4211,4288,4251,4241,4227,4200,4288,4268,4285,4211,4285]
oversigt_1800 = {}
oversigt_1816 = {}

# Implementeret 1:1 direkte fra wiki:
# https://en.wikipedia.org/wiki/Date_of_Easter#Gauss's_Easter_algorithm
def gauss_easter_date(year, error):
    a = year%19
    b = year%4
    c = year%7
    k = year//100
    if error:
        # Fejlen fra Gauss' 1800 version
        p = k // 3
    else:
        # Den opdaterede 1816 version
        p = (13 + 8*k) // 25
    q = k // 4
    M = (15 - p + k - q) % 30
    N = (4 + k - q) % 7
    d = (19*a + M) % 30
    e = (2*b + 4*c + 6*d + N)%7
    if (d+e) <= 9:
        day = 22 + d + e
        month = "March"
    elif (d == 28 and e == 6 and ((11*M + 11) % 30) < 19):
        day = 18
        month = "April"
    elif (d == 29 and e == 6):
        day = 19
        month = "April"
    else:
        day = d + e - 9
        month = "April"
    if error:
        oversigt_1800.update({year: chr(day+96)})
    else:
        oversigt_1816.update({year: chr(day+96)})

list(map(lambda x: gauss_easter_date(x,False), brev1 + brev2A + brev2B))
list(map(lambda x: gauss_easter_date(x,True), brev3))

print ("\nBrev 1:")
for x in brev1:
    print (oversigt_1816[x],end='')

print ("\n\nBrev 2(A)")
for x in brev2A:
    print (oversigt_1816[x],end='')

print ("\n\nBrev 2(B)")
for x in brev2B:
    print (oversigt_1816[x],end='')

print ("\n\nBrev 3")
for x in brev3:
    print (oversigt_1800[x],end='')

# alecleamas
# algoritmesomgrundlagligger
# selvmatematikerneskongekanfejle
# moedmigvedcheckpointcharlieklokkentolvmidnatkomalene