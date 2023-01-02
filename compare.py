import numpy as np


a1=[]
b=[]

def m(S1:str,S2:str,i:int,j:int):
    if(S1[i]==S2[j]):
        return 0
    else:
        return 1



def create(s1:str,s2:str):
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            a1.append(0)
        b.append(a1.copy())
        a1.clear()

#расстояние
def Lev(s1:str,s2:str):
    create(s1,s2)
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if (j == 0 and i > 0):
                b[i][j] = i
            if (i == 0 and j > 0):
                b[i][j] = j
            if (i > 0 and j > 0):
                b[i][j] = min(b[i][j - 1] + 1, b[i - 1][j] + 1, b[i - 1][j - 1] + m(s1, s2, i - 1, j - 1))



print("MAIN\n")
if __name__=="__main__":
    paths=[]
    with open(r"input.txt",'r') as f:
        paths=f.read()
    paths=paths.split()
    print(paths)
    k=0
    scrs=[]
    for i in range(int(len(paths)/2)):
        with open(paths[0+2*i],'r') as f:
            txt1=f.read()
        with open(paths[1+2*i],'r') as f:
            txt2=f.read()
        b=[]
        Lev(txt2, txt1)
        b = np.array(b)
        b.reshape(len(txt2) + 1, -1)
        print(b)

        print(b[b.shape[0] - 1][b.shape[1] - 1])
        print((len(txt2) - b[b.shape[0] - 1][b.shape[1] - 1]) / len(txt2))
        scrs.append((len(txt2) - b[b.shape[0] - 1][b.shape[1] - 1]) / len(txt2))
        del b
    with open("scores.txt","w") as f:
        for i in range(len(scrs)):
             f.write(str(scrs[i]))
             f.write("\n")

