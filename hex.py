def hex(input,iHex,oHex):
    if checkHex(iHex) == False:
        return Exception("nrfnbhzt7z iHex checkHex["+ str(iHex)+"]")
    if checkHex(oHex) == False:
        return Exception("4xn23cwac5 oHex checkHex["+ str(oHex)+"]")
    if iHex == oHex:
        return input
    slice = to10Slice(input)
    val = 0
    if iHex != 10:
        slice = slice[::-1]
        for index,item in enumerate(slice):
            val+=slice[index]*(iHex**index)
    elif iHex == 10:
        val = int(input)
    if oHex == 10:
        return val
    if val < oHex-1:
        return val
    one = val/oHex
    oneOther = val%oHex
    resultSlice = [oneOther]
    while one>oHex-1:
      resultSlice.append(oneOther)
      one = one/oHex
    resultSlice.append(one%oHex)
    resultSlice=resultSlice[::-1]
    result = ""
    if oHex<=10:
        for one in resultSlice:
            result+=str(one)
        return int(result)
    if oHex>10:
        for one in resultSlice:
            if one<10:
                result+=str(one)
            if one >= 10:
                result+=str(chr(one+87))
        return result
def checkHex(hex):
    return hex>=2 and hex<=16
def to10Slice(input):
    result=[]
    strInput = str(input)
    strInput = strInput.lower()
    for b in strInput:
        if b>='0' and b<='9':
            result.append(int(b))
        elif b>='a' and b<='f':
            result.append(ord(b)-87)
    return result
print("???",hex(255,10,16))
print(hex("FF",16,10))
