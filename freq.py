def freq(arr):
    freq_dict = {}
    for i in arr:
        if i in freq_dict:    
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    return freq_dict    S