import functions as f
numerpfs = []
denompfs = []
desired_prime = 104743
def create_pfs():
    numers = [17,78,19,23,29,77,95,77,1,11,13,15,1,55]
    denoms = [91,85,51,38,33,29,23,19,17,13,11,2,7,1]
    for n in numers:
        numerpfs.append(f.pf(n))
    for d in denoms:
        x = f.pf(d)
        f.pf_inverse(x)
        denompfs.append(x)

def fractran(pf):
    for i in range(len(denompfs)):
        success = True
        for j in denompfs[i].keys():
            if j not in pf.keys():
                success = False
        if success:
            pass
    return {}

def main():
    state = {2:1}
    iters = 0
    while not (len(state.keys()) == 1 and state.keys()[0] == 2):
        state = fractran(state)
        iters += 1
    print("done")
    print(iters)

    


if __name__ == "__main__":
    main()