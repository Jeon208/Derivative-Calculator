print("\n[!] Derivative Calculator")
print("""
Caution : Input the expanded polynomial function.
주의 : 전개된 다항함수를 입력하시오.
""")

func_s = input(" f(x) = ").replace(" ", "").replace("-","+-").split("+")
func_e = ''

def prime():
    for term in func_s:

        # to calculate through the formula
        if not('x' in term): # constant (5 = 5x^0)
            term = term+"x^0"

        if not('^' in term): # x = x^1
            term = term.replace("x", "x^1")

        if term[0] == "x": # x = 1x
            term = term.replace("x", "1x")


        number = term.split("x^")
        coefficient_s = float(number[0])
        exponent_s =  float(number[1])

        # ax^n = nax^(n-1)
        coefficient_e = coefficient_s * exponent_s
        exponent_e = exponent_s - 1

        term = f"{coefficient_e:g}x^{exponent_e:g}" # ex) 8.0 -> 8

        # which is...
        if coefficient_e == 0: # 0 * everything = 0
            term = ""
        elif coefficient_e > 0: # plus
            term = "+"+term
        else: # minus
            term = term

        if exponent_e != 0: # except constant case
            if (coefficient_e == 1) or (coefficient_e == -1): # (1)x = x, -(1)x = -x
                term = term.replace("1", "")

        if exponent_e == 0: # 5(n^0) = 5
            term = term.replace("x^0", "")

        if exponent_e == 1: # x(^1) = x
            term = term.replace("^1", "")
        

        global func_e
        func_e += term+" "
        
    return print(f"f'(x) = {func_e}")

# execute
prime()
