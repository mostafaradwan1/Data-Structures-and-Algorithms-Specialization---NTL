def are_equal(s1,s2):
    if len(s1)!=len(s2):
        return False
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            return False
        return True

def find_pattern_naieve(p,s):
    result=[]
    plen=len(p)
    slen=len(s)
    for i in range(slen-plen):
        if are_equal(s[i:i+plen-1],p):
            result.append(i)
    return result 

import random


def poly_hash(s, prime, x):
    ans = 0
    for c in reversed(s):
    	ans = (ans * x + ord(c)) % prime
    return ans

def precompute_hashes(text, plength, p, x):
    H = [0] * (len(text) - plength + 1)
    s = text[-plength:]
    H[len(text)-plength] = poly_hash(s, p, x)
    y = 1
    for i in range(1, plength+1):
        y = (y * x) % p
    for i in reversed(range(len(text) - plength)):
    	prehash = x * H[i + 1] + ord(text[i]) - y * ord(text[i + plength])
    	while(prehash < 0):
    		prehash += p
        H[i] = prehash % p
    return H

def get_occurrences(pattern, text):
    p = 1000000007
    x = random.randint(1, p)
    tlength = len(text)
    plength = len(pattern)
    phash = poly_hash(pattern, p, x)
    H = precompute_hashes(text, plength, p, x)
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if phash == H[i] and text[i:i + len(pattern)] == pattern
    ]


