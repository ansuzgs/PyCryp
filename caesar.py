#plainText = raw_input("What is your plaintext? ")
plainText = 'Znoy juky rkzzkx lxkwaktie gtgreyoy. Cnork utk igt ikxzgotre xgtq znk lxkwaktie ul rkzzkxy ot znk Ktmroyn rgtmagmk, znoy oy lgx lxus otlgrrohrk. Znoy skznuj cuarj xkwaoxk g namk ygsvrk zu xkroghre makyy znk qke ul g ycozin iovnkx. Lux kdgsvrk, O vgyzkj znk ktzoxk coqovkjog ktzxe ut krkvngtzy otzu znoy. Oz iuxxkizre makyykj yusk ul znk rkzzkxy, roqk cnoin rkzzkx cgy k, nuckbkx, oz ngj g tashkx ul rkzzkxy ycozinkj ux soyvrgikj'
shift = int(raw_input("What is your shift? "))

key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext):
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % len(key)
            result += key[i]
        except ValueError:
            result += l

    print result

#caesar(plainText.lower(), shift)
decrypt(shift, plainText)
