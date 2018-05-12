import numpy as np
import pandas as pd

def get_sl(path):
    with open(path) as f:
        st = [line.strip().upper() for line in f.readlines()]
    return st
def gen_mgram(sl):
    complete = ''.join(sl)
    amino_acids = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
    return {acid:len([l for l in complete if l==acid]) for acid in amino_acids}
def gen_broken_digram(sl):
    raw = {}
    for seq in sl:
        for i in range(len(seq)-1):
            if seq[i:i+2] in raw:
                raw[seq[i:i+2]] +=1
            else:
                raw[seq[i:i+2]]=0
    return raw
def count2freq(dic):
    tot = sum(dic.values())
    return {a:b/tot for a,b in dic.items()}
def count2trans(dic):
    return {a:b/sum([d for c,d in dic.items() if c[0]==a[0]]) for a,b in dic.items()}

def run_vitterby(states = ['S','T'],inits = [s_prob,1-s_prob],trs = st_trans,emissions = [sol_emission,tm_emission],read='KNSFFFFFFFLIII'):
    states = ['S','T']
    emitted = list(emissions[0].keys()) + list(emissions[1].keys())
    state = [states[0]]*len(emissions[0]) + [states[1]]*len(emissions[1])
    primer = np.hstack((np.array(state).reshape((-1,1)), np.array(emitted).reshape((-1,1))))
    df = pd.DataFrame(primer, columns=['State','Emitted'])
    pointer = pd.DataFrame(primer, columns=['State','Emitted'])
    df.set_index(['State','Emitted'],inplace=True)
    pointer.set_index(['State','Emitted'],inplace=True)
    count = 1
    for char in read:
        df = df.assign(a = pd.Series([0.0]*len(df)).values)
        pointer = pointer.assign(a=pd.Series(['0']*len(df)).values)
        if count ==1:
            for i in range(len(states)):
                for em in emissions[0].keys():
                    if em == read[0]:
                        val = inits[i]*emissions[i][em]
                        df.loc[states[i]].loc[em]['a'] = float(val)
        else:
            for i in range(len(states)):
                mval = 0
                maxes = [trs[states[j]+states[i]]*max(df.loc[states[j]][str(count-1)].tolist()) for j in range(len(states))]
                mval = max(maxes)
                loc= states[[j for j in range(len(states)) if maxes[j]==mval][0]]
                pointer.loc[states[i]].loc[char]['a']=loc
                df.loc[states[i]].loc[char]['a']= float(mval*emissions[i][char])
        df.rename(columns = {'a':'{}'.format(count)},inplace=True)
        pointer.rename(columns={'a':'{}'.format(count)},inplace=True)
        count = count + 1

    return (df,pointer)

def main():
    #Get list of sequences
    state = get_sl('state_sequences.txt')
    tm = get_sl('transmembrane_sequences.txt')
    sol = get_sl('soluble_sequences.txt')
    #The probability of the initial state going to S
    s_prob = sum([1 for l in state if l[0]=='S'])/len(state)
    tm_mgram = gen_mgram(tm)
    tm_emission = count2freq(tm_mgram)
    sol_mgram = gen_mgram(sol)
    sol_emission = count2freq(sol_mgram)
    st_digram = gen_broken_digram(state)
    st_freq = count2freq(st_digram)
    #Convert frequencies into transition probabilities
    st_trans = count2trans(st_digram)
    dfa,ptr = run_vitterby(states = ['S','T'],inits = [s_prob,1-s_prob],trs = st_trans,emissions = [sol_emission,tm_emission],read='KNSFFFFFFFLIII')
    print('---Problem---1')
    print('This is the data frame')
    print(dfa)
    print('This points to the last state. We start in the T domain (since it has the largest final value) and work backwards')
    print(ptr)
    print('Therefore the path is SSSSTTTTTTTTTTT')
    #Note that this problem is identical to the problem of  how many 'ST' and 'TS' segments there are (subtracting one if the protein starts and ends with 'S' )
    print('--Problem---2')
    num_tm = [sum([1 for i in range(len(l)-1) if l[i:i+2]=='ST' or l[i:i+2]=='TS'])if not (l[0]=='S' and l[-1]=='S') else sum([1 for i in range(len(l)-1) if l[i:i+2]=='ST' or l[i:i+2]=='TS'])-1 for l in state]
    print('The average length is {}'.format(np.average(num_tm)))
