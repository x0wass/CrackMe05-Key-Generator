import random, string
#rock
# condition 1 : Should be 19 chars
# condition 2 : should be composed of alphanumeric character
# condition 3 : no special char except for '-' : (char < '-' or '-' < char < '0') -> err
# Only alphabetical and numerical char, only '-' accepted for special char

#paper
# condition 1: 
#   (key[0xa] ^ key[0x8] + 0x30 < 0x3a && key[0xd] ^ key[0x5] + 0x30 < 0x3a)
#   &&
#   (key[0xa] ^ key[0x8] + 0x30 > 0x2f && key[0xd] ^ key[0x5] + 0x30 > 0x2f)
# condition 2: 
#   key[0x3] == key[0xa] ^ key[0x8] + 0x30 && key[0xf] == key[0xa] ^ key[0x8] + 0x30
#   &&
#   key[0x0] == key[0xd] ^ key[0x5] + 0x30 || key[0x12] == key[0xd] ^ key[0x5] + 0x30

#scissors
# condition 1 : key[0x2] + key[0x1] > 0xaa && key[0x11] + key[0x10] > 0xaa
# condition 2 : key[0x2] + key[0x1] != key[0x11] + key[0x10]
    
#cracker
# condition 1: key[0xe] + key[0x4] + key[0x9] == 0x87 (0x87 = 135 and 135/3 = 45 => ascii code for '-')

#key to generate
# 19 characteres key (rock's conditon)
# '-' at the right position (cracker's conditon)
key = ['?','?','?','?','-','?','?','?','?','-','?','?','?','?','-','?','?','?','?']


# generate random ASCII alphanumeric character or '-' (in decimal) 
def randASCII():
    return ord(''.join(random.choices(string.ascii_letters + string.digits + '-')))


#paper
while(True):
    s10 = randASCII()
    s08 = randASCII()
    s13 = randASCII()
    s05 = randASCII()

    c1 = (s10 ^ s08) + 0x30
    c2 = (s13 ^ s05) + 0x30

    if ( (c1 < 0x3a and c2 < 0x3a) and (c1 > 0x2f and c2 > 0x2f)):
        #we add s10 s08 s13 and s05 to the key at the corresponding index
        key[10] = chr(s10)
        key[8] = chr(s08)
        key[13] = chr(s13)
        key[5] = chr(s05)

        #we can now add the new char of the key c1 and c2
        key[3] = chr(c1)
        key[15] = chr(c1)

        key[0] = chr(c2) 
        key[18] = chr(c2)
        break


#scissors
while(True):
    s01 = randASCII()
    s02 = randASCII()
    s16 = randASCII()
    s17 = randASCII()

    c1 = s02 + s01
    c2 = s17 + s16
    if(c1 > 0xaa and c2 > 0xaa and c1 != c2):
        #we add s02 s01 s17 and s16 to the key at the corresponding index
        key[2] = chr(s02)
        key[1] = chr(s01)
        key[16] = chr(s16)
        key[17] = chr(s17)
        break

#Finally we add to the key the remaining characters, those which do not depend on any other character of the key
key[6] = chr(randASCII())
key[7] = chr(randASCII())
key[11] = chr(randASCII())
key[12] = chr(randASCII())

print(''.join(key))
