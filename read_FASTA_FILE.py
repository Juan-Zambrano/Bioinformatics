def AA_freq(dic,ls):
    return {key: [sum([1 for aa in value if aa == l])/len(value) for l in ls] for key,value in dic.items()}
def morphus(dic,ls):
    with open("cluster.txt", "w") as f:
        f.write("PROTEIN"+ "\t" + "\t".join(ls) + "\n")
        for key,value in dic.items():
            f.write(key + '\t' + '\t'.join(["%2f" %x for x in value]) + "\n")
    return
def regular(dic):
    with open ("frequency_Protein_loc.txt", "w") as f:
        for key,value in dic.items():
            f.write(key + '\t' + '\t'.join(["%2f" %x for x in value]) + "\n")
    return

def main():
    Amino_Acid = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
    dic = {}
    with open ('yeast_aaseqs.txt','r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            elif (line.startswith(">")):
                key = line[1:]
                if(key not in dic):
                    dic[key] = []
                    continue
            dic[key].append(line)
        value = [''.join(dic[key]) for key,value in dic.items()]
        keys = [key for key,value in dic.items()]
        dict_of_all = dict(zip(keys,value))
        #remove unknown locations and AA
        filter_key = [key for key,value in dict_of_all.items() if "unknown" not in key]
        k = []
        final_dict = {}
        last_dict = {}
        for key in filter_key:
                final_dict[key] = dict_of_all[key]
        for key,value in final_dict.items():
            new_value = value
            for char in value:
                if(char not in Amino_Acid):
                    new_value = new_value.replace(char,"")
            last_dict[key] = new_value                  

main()