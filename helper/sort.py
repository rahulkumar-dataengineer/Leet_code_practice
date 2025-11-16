def print_help(og, index1, index2, arr=[""]):
    arrp = arr
    arrp[index1] = str(og[index1])
    arrp[index2] = str(og[index2])
    print("[" + ", ".join(x if x != "" else "" for x in arrp) + "]")