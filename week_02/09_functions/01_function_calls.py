'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.
'''
import math


def BS_vanilla(s, t, k, r, vol):
    '''
    C = s N(d1) - N(d2)* k * exp(-rt)

    :param s: current stock price
    :param t: time to maturity in years
    :param k: strike
    :param r: annualized risk free rate, continuously compounded
    :param vol: volatility
    :return: call option price
    '''
    d1 = d(s, t, k, r, vol, d1=1)
    d2 = d(s, t, k, r, vol, d1=2)
    return s*N(d1) - N(d2) * k * math.exp(-r*t)


def N(d):
    '''
    standard normal cumulative distribution function
    :param: d is function of s, k, r, s, vol
    :return: cum Normal
    '''
    return 1. - 0.5 * erfcc(d / (2 ** 0.5))


def erfcc(x):
    """Complementary error function."""
    z = abs(x)
    t = 1. / (1. + 0.5*z)
    r = t * math.exp(-z*z-1.26551223+t*(1.00002368+t*(.37409196+
        t*(.09678418+t*(-.18628806+t*(.27886807+
        t*(-1.13520398+t*(1.48851587+t*(-.82215223+
        t*.17087277)))))))))
    if x >= 0.:
        return r
    else:
        return 2. - r


def d(s, t, k, r, vol, d1=1):
    """
    returns the d1 in standard Black Scholes formula
    :param s: current stock price
    :param t: time to maturity
    :param k: strike
    :param r: risk free rate
    :param vol: volatility
    :param d1 = 1 indicate it is the first d, otherwise d = 2
    :return: call option price
    """
    x = math.log(s/k + (r + vol ** 2/2) * t)/(vol * t ** 0.5)
    if d1 != 1:
        x = x - vol * (t ** 0.5)
    return x

'''
stock price = 100
ttm = 1 year
strike = 100
r = 2%
vol = 0.2

* checking the price with online calculator
https://www.mystockoptions.com/black-scholes.cfm?ticker=&s=100&x=100&t=1&r=2%25&v=20%25&calculate=Calculate
C= 8.916
'''

print(d(100, 1, 90, 0.02, 0.2, True))
print(BS_vanilla(100, 1, 100, 0.02, 0.2))


# from stack overflow
def normcdf(x, mu, sigma):
    t = x-mu
    y = 0.5*math.erfc(-t/(sigma*math.sqrt(2.0)))
    if y>1.0:
        y = 1.0
    return y


def normpdf(x, mu, sigma):
    u = (x-mu)/abs(sigma)
    y = (1/(math.sqrt(2*math.pi)*abs(sigma)))*math.exp(-u*u/2)
    return y


def normdist(x, mu, sigma, f):
    if f:
        y = normcdf(x,mu,sigma)
    else:
        y = normpdf(x,mu,sigma)
    return y


