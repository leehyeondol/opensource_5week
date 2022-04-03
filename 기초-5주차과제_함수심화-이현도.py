def base2(n):
    if n > 1:
        base2(n // 2)
    return print(n % 2, end='')

def base8(n):
    if n >= 8:
        base8(n // 8)
    return print(n % 8, end='')



def base16(n):
    convertString="0123456789ABCDEF"
    if n <16 :
        return convertString[n]
    b = divmod(n,16)
    return base16(n//16)+ convertString[b[1]]




a = int(input("10진수 입력: "))


print("2진수 : ")
base2(a)
print("\n8진수 : ")
base8(a)
print("\n16진수 : ")
print("%s"%base16(a))

##2019038085_이현도##
