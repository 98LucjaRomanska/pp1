dimensional = [ ['x', 'x'],
                ['x', 'x'],
                ['x', 'x'],
                ['x', 'x'] ]
dimensional1 = [ ['1', 'e'],
                 ['d', 'd'],
                 ['b', 'f'],
                 ['z', 'g'] ]
def dimen2x4(common_arr):
    for row in common_arr:
        for i in row:
            print(i, end=" ")
        print('')

if __name__=="__main__":   
    dimen2x4(dimensional)
    dimen2x4(dimensional1)



        
