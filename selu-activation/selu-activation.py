import math

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    # Write code here
    lam = 1.0507009873554804934193349852946 
    alpha = 1.6732632423543772848170429916717
    list = []

    for i in x:
        if i > 0:
            list.append(round(lam * i, 4))
        else:
            list.append(round(lam * alpha * (math.exp(i) - 1), 4))

    return list