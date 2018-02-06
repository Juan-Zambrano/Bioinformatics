def main():
    with open('Hinfluenzae.txt','r') as f:
        flu = [line.split(",") for line in f.read().splitlines()]
    with open('Taquaticus.txt','r') as g:
        taq = [line.split(",") for line in g.read().splitlines()]
    with open('MysteryGene1.txt','r') as g:
        mys1 = [line.split(",") for line in g.read().splitlines()]
    with open('MysteryGene2.txt','r') as g:
        mys2 = [line.split(",") for line in g.read().splitlines()]
    with open('MysteryGene3.txt','r') as g:
        mys3 = [line.split(",") for line in g.read().splitlines()]
#Single nucleotide
    dic = {}
    ls_to_str = []
    for i in range(len(mys3)):
        for j in range(len(mys3[i])):
            ls_to_str.append(mys3[i][j])
    str1 = ''.join(ls_to_str)
    for char in str1:
        dic[char] = dic.get(char,0) + 1
    for key,value in dic.items():
        print("The nucleotide " + str(key) + " occurs " + str(value) + " times")

#Di-nucleotide
    dic1 = {}
    ls_to_str2 = []
    for i in range(len(mys3)):
        for j in range(len(mys3[i])):
            ls_to_str2.append(mys3[i][j])
    str2 = ''.join(ls_to_str)
    for i in range(len(str2) - 1):
        dinucleotide = str2[i:i+2]
        if(dinucleotide in dic1):
            dic1[dinucleotide] +=1
        else:
            dic1[dinucleotide] = 1
    for key,value in dic1.items():
        print("The Di-nucleotide " + str(key) + " occurs " + str(value) + " times")

main()
