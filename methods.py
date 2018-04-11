#!/bin/python3.6
# -*-coding:Utf-8 -*

import math

def fonc(n, x):
    produit = 1.0
    k = 0

    if (x == 0):
        return (1)
    while (k <= n):
        resultat = x/(2*k+1)
        produit *= (math.sin(resultat)/resultat)
        k += 1
    return produit

def dif_with_pi(value):
    dif = value - (math.pi/2)
    print('diff =', '%.10f' % dif)

def rect(n, h):
    s = 0.0
    i = 0.0
    while (i < 5000):
        s += (fonc(n, i) * h)
        i += 0.5
    print('Rectangles:')
    print('I%d' % n, '=', '%.10f' % s)
    dif_with_pi(s)

def trapeze(n, h):
    s = 0.0
    i = 0.0
    while (i < 5000):
        s += (fonc(n, i) + fonc(n, i + 0.5)) / 2 * h
        i += 0.5
    print('Trapezoids:')
    print('I%d' % n, '=', '%.10f' % s)
    dif_with_pi(s)

def simpson(n, h):
    a1 = 0.0
    a2 = 0.0
    hp = 1/12
    produit = 0.0
    i = 1.0
    j = 0.0

    while (i <= 10000 - 1):
        a1 += fonc(n, i * h)
        i += 1
    while (j <= 10000 - 1):
        a2 += fonc(n, j * h + 0.25)
        j += 1
    produit = hp * (fonc(n, 0) + fonc(n, 5000) + (2.0 * a1) + (4.0 * a2))
    print('Simpson:')
    print('I%d' % n, '=', '%.10f' % produit)
    dif_with_pi(produit)
