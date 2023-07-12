#Write a Python program that inputs a polynomial in standard algebraic notation and outputs the first derivative of that polynomial.


def compute_derivative(polynomial):
    terms=polynomial.split('+')
    derivative_terms=[]
    for term in terms:
        coefficient,exponent=term.split('x')
        if '^' in exponent:
            exponent=int(exponent.split('^')[1])
            coefficient*=exponent
            exponent-=1
        else:
            exponent=0

        derivative_terms.append(f"{coefficient}x^{exponent}")
        derivative_polynomial='+'.join(derivative_terms)
        return derivative_polynomial
