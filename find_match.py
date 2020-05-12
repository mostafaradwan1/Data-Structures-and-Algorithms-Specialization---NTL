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

def precompute_hashes(T,P,p,x):
    H=[]
    tlen=len(T)
    plen=len(P)
    S=T[tlen-plen:tlen-1]
    H=[]
    H[tlen-plen]=polyhash(S,p,x)
    y=1
    for i in range(1,plen):
        y=(y*x)%p
    for i in range(tlen-plen-1,1):
        

