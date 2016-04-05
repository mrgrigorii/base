# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 14:16:35 2016

@author: Григорий
"""

import math

def computing_gc_content(data):
    """
    Given: At most 10 DNA strings in FASTA format 
    (of length at most 1 kbp each).
    Return: The ID of the string having the highest GC-content, 
    followed by the GC-content of that string. 
    
    """
    data = data.split('>')
    rez = []
    for i in data[1:]:
        gc = 0
        at = 0
        i = i.split()
        name = i[0]
        for line in i[1:]:
            for j in line:
                if j == 'G' or j == 'C':
                    gc = gc + 1
                else: at = at + 1
        rez.append([gc*100/(gc+at), name])
    rez.sort()
    return rez
    
def most_frq_kmer(data):
    """
    Find the most frequent k-mers in a string.
    
    Given: A DNA string Text and an integer k.
    Return: All most frequent k-mers in Text (in any order).

    """
    rez = {}
    data = data.split()
    k = int(data[1])
    for i in range(len(data[0]) - k + 1):
        word = data[0][i:i+k] 
        if word not in rez:
            rez[word] = 1
        else:
            rez[word] = rez[word] + 1
    max = 0
    out = []
    for i in rez.keys():
        if rez[i] > max: max = rez[i]
    for i in rez.keys():
        if rez[i] == max: out.append([i,max])
    return out

def finding_motif(data):
    """
    Given: Two DNA strings ss and tt (each of length at most 1 kbp).
    Return: All locations of tt as a substring of ss.
    
    """
    out = ''
    data = data.split()
    motif, string = data[1], data[0]
    for i in range(len(string) - len(motif) + 1):
        eq = 0              # Эквивалентность строк
        for j in motif:
            if j == string[i + eq]:
                eq = eq + 1
        if eq == len(motif): out = out + ' ' + str(i+1)  
    return out

def finding_all_substrings(s1, s2): 
    if len(s1) > len(s2):  # s1 должны быть короче s2
        s1, s2 = s2, s1
    substrings = []
    for i in range(len(s1), 1, -1): #Минимальная длина 2 ( 1 + 1)
        for j in range(len(s1) - i + 1): # Кол-во сдвигов при данной длине i
            if s1[j:j + i] in s2 and i - 1 + j < len(s1):
                substrings.append(s1[j:j + i])
                #print("Совпадение ", s1[j:j + i], i, j)
                s1 = s1[0:j] + s1[j + i + 1:] #Убираем совпавшую часть строк
    return substrings

def finding_shared_motif(data):
    """
    Given: A collection of k(k≤100) DNA strings of length at 
    most 1 kbp each in FASTA format.
    Return: A longest common substring of the collection.
    (If multiple solutions exist, you may return any single solution.)
    
    """
    strings = []
    substrings = []
    data = data.split('>')
    for i in data[1:]:
        i = i.split()
        strings.append([i[0], ''.join(i[1:])])
    substrings.append(strings[0][1])
    strings.remove(strings[0])
    for st in strings:
        for i in substrings:
            s = i
            substrings.remove(i)
            substrings.extend(finding_all_substrings(s, st[1]))
    return substrings

def counting_point_mutations(data):
    s, t = data.split()
    dist = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            dist = dist + 1
    return dist
    
def levenstein_distance(data):
    s = []
    for line in data.split('>')[1:]:
        line = line.split()
        s.append([line[0], ''.join(line[1:])])
    print(s)
    name_1, s1, name_2, s2 = s[0][0], s[0][1], s[1][0], s[1][1]
    d = []
    for i in range(len(s1) + 1):
        d.append([x for x in range(i, i + len(s2) + 1 )])
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + \
                                     (1 if s1[i-1] != s2[j-1] else 0) )
    return d[-1][-1]
    
def nw_glbal_alingment(data):
    s = []
    for line in data.split('>')[1:]:
        line = line.split()
        s.append([line[0], ''.join(line[1:])])
    print(s)
    name_1, s1, name_2, s2 = s[0][0], s[0][1], s[1][0], s[1][1]
    d = []
    b = []
    for i in range(len(s1) + 1):
        d.append([x for x in range(i, i + len(s2) + 1 )])
        b.append(['>'])
        for j in range(len(s2)):
            b[i].append('|')
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1): 
            d[i][j] = d[i-1][j-1] + (1 if s1[i-1] != s2[j-1] else 0)
            b[i][j] = "d"
            if d[i][j] > d[i-1][j] + 1:
                d[i][j] = d[i-1][j] + 1
                b[i][j] = '>'
            if d[i][j] > d[i][j-1] + 1:
                d[i][j] = d[i][j-1] + 1
                b[i][j] = '|'  
    #print(b)
    i = len(s1)
    j = len(s2)
    print(i, j, b[i][j], b[i], len(b), len(b[i]))
    p = ''
    s_1 = ''
    s_2 = ''
    while i > 0 and j > 0:
        print(b[i][j], i, j)
        if b[i][j] is '|':
            p = b[i][j] + p
            s_1 = '-' + s_1
            s_2 = s2[j-1] + s_2
            j = j - 1
        elif b[i][j] is 'd':
            p = b[i][j] + p
            s_1 = s1[i-1] + s_1
            s_2 = s2[j-1] + s_2
            j = j - 1
            i = i - 1
        elif b[i][j] is '>':
            s_1 = s1[i-1] + s_1
            s_2 = '-' + s_2
            p = b[i][j] + p
            i = i - 1
    print(p)
    print("S1 ", s_1)
    print("S2 ", s_2)
#    for i in range(len(b[0])):
#        print([b[j][i] for j in range(len(b))])
#    for i in range(len(b[0])):
#        print([d[j][i] for j in range(len(d))]),
    
    return d[-1][-1]    
    
def mortal_fibonacci_rabbits(data):
    data = data.split()
    m = int(data[0])
    l = int(data[1])
    print(data, m, l)
    pairs = 1
    v = [0]*(l-1) + [1]
    for i in range(1,int(m)):
        born = pairs - v[-1]
        die = v[0]
        pairs = pairs + born - die
        v.append(born)
        v.remove(v[0])
    return pairs

def k_mer_composition(data):
    data = data.split('\n')[1:-1]
    data = ''.join(data)
    words = []
    h = {}
    for i in 'ACGT':
        for j in 'ACGT':
            for l in 'ACGT':
                for q in 'ACGT':
                    words.append(i + j + l + q)
                    h[words[-1]] = 0
    for i in range(len(data) - 3):
        h[data[i:i+4]] = h[data[i:i+4]] + 1
    rez = ''
    for i in words:
        rez = rez + str(h[i]) + ' '
    return rez

def consensus_and_profile(data):
    s = []
    for line in data.split('>')[1:]:
        line = line.split()
        s.append([line[0], ''.join(line[1:])])
    #print(s)
    rez = []
    w = 'ACGT'
    for i in range(len(s[0][1])):
        rez.append([0] * 4)
        for j in s:
            for q in range(4):
                if j[1][i] == w[q]:
                    rez[i][q] = rez[i][q] + 1
        
    print(rez[0:5])
    out = ['', 'A: ', 'C: ', 'G: ', 'T: ']
    for i in rez:
        m = 0
        for j in range(len(i)):
            out[j + 1] = out[j + 1] + str(i[j]) + ' '
            if i[j] > m:
                m = i[j]
                poplar_l = w[j]
        out[0] = out[0] + poplar_l
    for i in range(len(out)):
        out[i] = out[i] + '\n'
    return ''.join(out)

def read_fasta(data):
    """
    Example of data format:
    >Rosalind_0209
    GCAACGCACAACGA
    >Rosalind_2200
    TTATCTGACAAAGA
    out: 
    [['Rosalind_0209', 'GCAACGCACAACGA'],['Rosalind_2200', 'TTATCTGACAAAGA']]
    """
    s = []
    for line in data.split('>')[1:]:
        line = line.split()
        s.append([line[0], ''.join(line[1:])])
    return s
            
def transitions_and_transversions(data):
    s = read_fasta(data)
    transitions = 0
    transversions = 0
    for i in range(len(s[0][1])):
        let_1 = s[0][1][i]
        let_2 = s[1][1][i]
        if let_1 == let_2:
            continue
        if ((let_1 + let_2) in 'AGA') or ((let_1 + let_2) in 'CTC'):
            transitions = transitions + 1
        else:
            transversions = transversions + 1
    return transitions/transversions
  
def modeling_random_genomes(data):
    data = data.split()
    string, gc_contents = data[0], data[1:]
    out = ''
    for i in gc_contents:
        i = float(i)
        p_gc = i / 2
        p_at = (1 - i) / 2
        p = 0
        for j in string:
            if j in 'GC':
                p = p + math.log10(p_gc)
            if j in 'AT':
                p = p + math.log10(p_at)
        out = out + str(p) + ' '
    return out

def get_blosum62():
    f = open('data_rosalind/BLOSUM62.txt')
    l = f.readline().replace(' ', '').rstrip('\n')
    blosum = [[] for i in l]
    for i in f.readlines():
        i = i.split()[1:]
        for j in range(len(i)):
            blosum[j].append(int(i[j]))
    return l, blosum

def get_pam250():
    f = open('data_rosalind/PAM250.txt')
    l = f.readline().replace(' ', '').rstrip('\n')
    pam = [[] for i in l]
    for i in f.readlines():
        i = i.split()[1:]
        for j in range(len(i)):
            pam[j].append(int(i[j]))
    return l, pam   
    
def qlobal_alignment_with_scoring_matrix(data):
    s = read_fasta(data)
    l, blosum = get_blosum62()
    name_1, s1, name_2, s2 = s[0][0], s[0][1], s[1][0], s[1][1]
    d = []
    for i in range(len(s1) + 1):
        d.append([- x * 5 for x in range(i, i + len(s2) + 1 )])
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            d[i][j] = max(d[i-1][j] - 5, \
                      d[i][j-1] - 5, \
                      d[i-1][j-1] + blosum[l.find(s1[i-1])][l.find(s2[j-1])] )
    return d[-1][-1]
      
def local_alignment_with_scoring_matrix(data):
    s = read_fasta(data)
    l, pam = get_pam250()
    name_1, s1, name_2, s2 = s[0][0], s[0][1], s[1][0], s[1][1]
    #print(s)
    d = []
    b = []
    for i in range(len(s1) + 1):
        d.append([0 for x in range(i, i + len(s2) + 1 )])
        b.append(['s'])
        for j in range(len(s2)):
            b[i].append('s')
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if d[i-1][j-1] + pam[l.find(s1[i-1])][l.find(s2[j-1])] > 0:
                d[i][j] = d[i-1][j-1] + pam[l.find(s1[i-1])][l.find(s2[j-1])]
                b[i][j] = "d"
            if d[i][j] < d[i-1][j] - 5:
                d[i][j] = d[i-1][j] - 5
                b[i][j] = '>'
            if d[i][j] < d[i][j-1] - 5:
                d[i][j] = d[i][j-1] - 5
                b[i][j] = '|' 
    # finding max score in matrix
    m = 0
    i_g = 0
    j_g = 0
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1): 
            if d[i][j] > m:
                m = d[i][j]
                i_g = i
                j_g = j
    #print(b)
    print(i, j, b[i][j], len(b), len(b[i]))
    
    print('IJ', i_g, j_g, d[i_g][j_g])
    i = i_g
    j = j_g
    p = ''
    s_1 = ''
    s_2 = ''
    while i > 0 and j > 0:
        #print(b[i][j], i, j)
        if b[i][j] is '|':
            p = b[i][j] + p
            s_1 = '-' + s_1
            s_2 = s2[j-1] + s_2
            j = j - 1
        elif b[i][j] is 'd':
            p = b[i][j] + p
            s_1 = s1[i-1] + s_1
            s_2 = s2[j-1] + s_2
            j = j - 1
            i = i - 1
        elif b[i][j] is '>':
            s_1 = s1[i-1] + s_1
            s_2 = '-' + s_2
            p = b[i][j] + p
            i = i - 1
        elif b[i][j] is 's':
            break
    #print(p)
    print("S1 ", s_1.replace('-',''))
    print("S2 ", s_2.replace('-',''))
#    for i in range(len(b[0])):
#        print([b[j][i] for j in range(len(b))])
#    for i in range(len(b[0])):
#        print([d[j][i] for j in range(len(d))]),
    return m, s_1, s_2        

def local_alignment_with_affine_gap(data):
    s = read_fasta(data)
    l, pam = get_blosum62()
    name_1, s1, name_2, s2 = s[0][0], s[0][1], s[1][0], s[1][1]
    #print(s)
    d = []
    b = []
    for i in range(len(s1) + 1):
        d.append([0 for x in range(i, i + len(s2) + 1 )])
        b.append(['s'])
        for j in range(len(s2)):
            b[i].append('s')
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            #print(i, j, len(s1), len(s2))
            if d[i-1][j-1] + pam[l.find(s1[i-1])][l.find(s2[j-1])] > 0:
                d[i][j] = d[i-1][j-1] + pam[l.find(s1[i-1])][l.find(s2[j-1])]
                b[i][j] = "d" 
            x = 0 
            while x < i:
                var = d[x][j] - i + x - 9
                if var > d[i][j]:
                    d[i][j] = var
                    b[i][j] = '|' + str(x)
                    x = x + 10
                    continue
                x = x + 1
            x = 0
            while x < j:
                var = d[i][x] - j + x - 9
                if var > d[i][j]:
                    d[i][j] = var
                    b[i][j] = '|' + str(x)  
                    x = x + 10
                    continue
                x = x + 1
    # finding max score in matrix
    m = 0
    i_g = 0
    j_g = 0
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1): 
            if d[i][j] > m:
                m = d[i][j]
                i_g = i
                j_g = j
    #print(b)
    print(i, j, b[i][j], len(b), len(b[i]))
    
    print('IJ', i_g, j_g, d[i_g][j_g])
    i = i_g
    j = j_g
    p = ''
    s_1 = ''
    s_2 = ''
    while i > 0 and j > 0:
        #print(b[i][j], i, j)
        if b[i][j][0] is '|':
            dif = int(b[i][j][1:])
            p = b[i][j] + p
            s_1 = '-'*dif + s_1
            s_2 = s2[j-1] + s_2
            j = j - dif
        elif b[i][j] is 'd':
            p = b[i][j] + p
            s_1 = s1[i-1] + s_1
            s_2 = s2[j-1] + s_2
            j = j - 1
            i = i - 1
        elif b[i][j][0] is '>':
            dif = int(b[i][j][1:])
            s_1 = s1[i-1] + s_1
            s_2 = '-'*dif + s_2
            p = b[i][j] + p
            i = i - dif
        elif b[i][j] is 's':
            break
    #print(p)
    print("S1 ", s_1.replace('-',''))
    print("S2 ", s_2.replace('-',''))
#    for i in range(len(b[0])):
#        print([b[j][i] for j in range(len(b))])
#    for i in range(len(b[0])):
#        print([d[j][i] for j in range(len(d))]),
    return m, s_1, s_2        
    
if __name__ == '__main__':
    #f = open('data_rosalind/rosalind_gc.txt', 'r')
    #print(computing_gc_content(f.read()))
    #f = open('data_rosalind/rosalind_ba1b.txt', 'r')
    #print(most_frq_kmer(f.read()))
    #f = open('data_rosalind/rosalind_subs.txt', 'r')
    #print(finding_motif(f.read()))
    #f = open('data_rosalind/rosalind_lcsm.txt', 'r')rosalind_hamm
    #print(finding_shared_motif(f.read()))
    #f = open('data_rosalind/rosalind_hamm.txt', 'r')
    #print(counting_point_mutations(f.read()))
    #f = open('data_rosalind/2_zadacha_rosalind_edit.txt', 'r')
    #print(levenstein_distance(f.read()))
    #f = open('data_rosalind/rosalind_edta.txt', 'r')
    #print(nw_glbal_alingment(f.read()))
    #f = open('data_rosalind/rosalind_fibd.txt', 'r')
    #print(mortal_fibonacci_rabbits(f.read()))
    #f = open('data_rosalind/rosalind_kmer.txt', 'r')
    #print(k_mer_composition(f.read()))
    #f = open('data_rosalind/rosalind_cons.txt', 'r')
    #print(consensus_and_profile(f.read()))
    #f = open('data_rosalind/rosalind_tran.txt', 'r')
    #print(transitions_and_transversions(f.read()))
    #f = open('data_rosalind/rosalind_prob.txt', 'r')
    #print(modeling_random_genomes(f.read())) 
    #f = open('data_rosalind/rosalind_glob.txt', 'r')
    #print(qlobal_alignment_with_scoring_matrix(f.read())) 

    #f = open('data_rosalind/rosalind_loca.txt', 'r')
    ##f = open('data_rosalind/test.txt', 'r')
    #mm, s, s2 = local_alignment_with_scoring_matrix(f.read())
    #s = 'MEANLYPRTEINSTRIN'
    #s2 = 'LEASANTLYEINSTEIN'
#    print(mm)
#    l, pam = get_pam250()
#    m = 0
#    for i in range(len(s)):
#        if (s[i] in l) and (s2[i] in l):
#            m = m + pam[l.find(s[i])][l.find(s2[i])]
#        else:
#            m = m - 5
#    print(m)
    f = open('data_rosalind/rosalind_laff.txt', 'r')
    mm, s, s2 = local_alignment_with_affine_gap(f.read())
    print(mm)
    l, pam = get_blosum62()
    m = 0
    for i in range(len(s)):
        if (s[i] in l) and (s2[i] in l):
            m = m + pam[l.find(s[i])][l.find(s2[i])]
        else:
            m = m - 5
    print(m)            
        

    
    
