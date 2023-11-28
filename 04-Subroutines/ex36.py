def f(sequence):
    
    a_string =""
    for c in range(len(sequence)):
        a_string += sequence[c] + " "

    # print(type(len(sequence)))
    print(a_string.split())
    new_list = a_string.split()
    # print(type(new_list))

    ppl_in_room =0

    for c in range(len(new_list)):
        if new_list[c] =="+":
            ppl_in_room += 1
            if ppl_in_room >=3:
                ppl3 = True
            else:
                ppl3= False
        elif new_list[c] =="-":
            ppl_in_room -= 1
    print(f'f("{sequence}") returns {ppl3}')
        

if __name__=="__main__":
    f("+-+++-+---")
    f("+-+-+-+-")
    f("+-++--+")
    