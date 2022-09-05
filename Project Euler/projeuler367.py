import functions as f
def main():
    ELEMENTS = 4
    times_table = []
    #sps the number of elements is m, and n are out of proper order
    # mCn * (1, 2, ..., m-n, (n jumbled with none correct))
    # how many are jumbled with none correct? f.derangements()
    for n in range(ELEMENTS + 1):
        times_table.append(f.nchooser(ELEMENTS,n) * f.derangements(n))
    #sps we have a specific arrangements [x_1, x_2, x_3, x_4]
    #how long on average does it take to reach [1,2,3,4]
    # idfk how to do this
    


if __name__ == "__main__":
    main()