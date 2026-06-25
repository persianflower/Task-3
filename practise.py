
#['p5', 'p1', 'p3', 'p2', 'p6', 'p4', 'p7']

terminals=['AB','BC','BB','CC','CA','SB','AS','CS']
non_terminals=['a','b']

R={
     'S':['AB','BC','a'],
     'A':['BB','CC','a'],
     'B':['CA','SB''b'],
     'C':['AS','CS','b']
    }

def cyk(word):
    w=len(word)
    T=[[set([]) for j in range(w)]for i in range(w)]

    for j in range(0,w):
        for lhs,rule in R.items():
            for rhs in rule:
                if len(rhs)==1 and rhs[0]==word[j]:
                    T[j][j].add(lhs)
        for i in range(j,-1,-1):
            for k in range(i,j+1):
                for lhs,rule in R.items():
                    for rhs in rule:
                        if len(rhs)==2 and rhs[0] in T[i][k] and rhs[1] in T[k+1][j]:
                            T[i][j].add(lhs)
    if len(T[0][w-1])!=0:
        return True
    return False
string="baab"
print(cyk(string))
