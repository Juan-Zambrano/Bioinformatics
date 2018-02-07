#Single nucleotide
def single_nucleotide(l,name=''):
    dic = {}
    ls_to_str = []
    for i in range(len(l)):
        for j in range(len(l[i])):
            ls_to_str.append(l[i][j])
    str1 = ''.join(ls_to_str)
    for char in str1:
        dic[char] = dic.get(char,0) + 1
    for key,value in dic.items():
        print("The nucleotide {} occurs {} times in {}".format(key,value,name))
    return dic
#Di-nucleotide

def dinucleotide(l,name=''):
    dic1 = {}
    ls_to_str2 = []
    for i in range(len(l)):
        for j in range(len(l[i])):
            ls_to_str2.append(l[i][j])
    str2 = ''.join(ls_to_str2)
    for i in range(len(str2) - 1):
        dinucleotide = str2[i:i+2]
        if(dinucleotide in dic1):
            dic1[dinucleotide] +=1
        else:
            dic1[dinucleotide] = 1
    for key,value in dic1.items():
        print("The di-nucleotide {} occurs {} times in {}".format(key,value,name))
    return dic1
#Function calculates expected values for single and di-nucleotides
def exp_freq(singles):
    freq_si = {}
    for key in singles:
        freq_si[key] = singles[key]/sum(singles.values())
    freq_di = {}
    for key in singles:
        for key2 in singles:
            freq_di[key+key2] = freq_si[key]*freq_si[key2]
    return (freq_si,freq_di)
#Main program with outputs
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
    #Outputs for Single Nucleotides
    print("Question 1:")
    print("Single nucleotide frequencies of H.influenzae and T.aquaticus.")
    single_flu = single_nucleotide(flu,'H.influenzae')
    Single_taq = single_nucleotide(taq,'T.aquaticus')
    print()
    print("Question 2:")
    print("Frequencies of dinucleotides in H.influenzae. ")
    di_flu = dinucleotide(flu,'H.influenzae')
    print()
    print("Question 3:")
    print("Frequencies of dinucleotides in T.aquaticus.")
    di_taq = dinucleotide(taq,'T.aquaticus')
    print()
    print("Question 4:")
    print("Expected frequencies for H.influenzae.")
    freq_si,freq_di = exp_freq(single_flu)
    valid = ['AA','AG','GA','AC','CA','AT','TA','GG','GC','CG','GT','TG','CC','CT','TC','TT']
    for key,value in freq_di.items():
        if(key in valid):
            print(key,value)
    print()
    print("Question 5:")
    print("Single nucleotide and di-nucleotide frequencies of three mystery gene's.")
    print()
    single_mys1 = single_nucleotide(mys1,'MysteryGene1')
    di_mys1 = dinucleotide(mys1,'MysteryGene1')
    print()
    single_mys2 = single_nucleotide(mys2,'MysteryGene2')
    di_mys2 = dinucleotide(mys2,'MysteryGene2')
    print()
    single_mys3 = single_nucleotide(mys1,'MysteryGene3')
    di_mys3 = dinucleotide(mys3,'MysteryGene3')
main()
