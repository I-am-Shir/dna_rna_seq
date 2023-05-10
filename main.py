# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
#    print(sys.argv[1])

'''def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')'''

def find_ssr(dna_seq):
    possible_repeat_seq_set = set()
    #checks for every letter till -6
    for i in range(0, len(dna_seq)-7):
        #a list of the repeats of the first letter in the current sub-sequence
        let_repeats = []
        #checks if the first letter in the sub-sequence repeats itself in the next 6 letters
        if dna_seq[i] in dna_seq[i+1:i+7]:
            #adding the repeats locations to a list
            for j in range(i+1 , i+7):
                if dna_seq[i] == dna_seq[j]:
                    let_repeats.append(j)
                #adds possible sub-sequences to a set
                    if j < i + 7:
                        possible_repeat_seq_set.add(dna_seq[i:j])
                    if i == j-1:
                        possible_repeat_seq_set.add(dna_seq[i])
                    else:
                        possible_repeat_seq_set.add(dna_seq[i:j-1])

    #creating dictionary for repeating sequences that follow the requirement.
    repeating_dic = {}
    j = 0
    #checks for biggest number of repeats for the possible sequences found
    for j in range(0, len(possible_repeat_seq_set)):
        num_repeats = 3
        while (list(possible_repeat_seq_set)[j])*num_repeats in dna_seq:
            #updates repeating value for the sub-sequence from 3 repeats onwards
            repeating_dic.update({list(possible_repeat_seq_set)[j]:num_repeats})
            num_repeats+=1
    return {s: repeating_dic[s] for s in sorted(repeating_dic)}

print(find_ssr(sys.argv[1]))




