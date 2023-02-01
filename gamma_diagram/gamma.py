def gamma(input_list=[1,2,3,4], fn_list=[lambda i : i, lambda i:i+1], title_width=25):
    def delimeter(value):
        return title_width-len(str(value))
    titles = ["id"]
    while True:
        input_title = input("title_name(1:20)> ").strip()
        #
        print(input_title)
        #
        if input_title=="":
            if len(fn_list)>len(titles)-1:
                titles+=["#"]*(len(fn_list)+1-len(titles))
            #
            print("titles: ",end="")
            [print(str(t)+"/", end="") for t in titles]
            print()
            #
            break
        titles+=[input_title]
    ## print output
    # title
    for t in titles:
        d = delimeter(t)
        print(t+" "*d, end="")
    print()
    # bars
    for t in titles:
        d = delimeter(t)
        for c in t:
            print("-",end="")
        print(" "*d, end="")
    print()
    # data
    for i in input_list:
        index = input_list.index(i)
        d = delimeter(index)
        # id
        print(str(index)+" "*d, end="")
        #others
        for fn in fn_list:
            result = str(fn(i))
            d_fn = delimeter(result)
            print(result+" "*d_fn,end="")
        print()
lambda pr: print()

if __name__ == "__main__":
    gamma()