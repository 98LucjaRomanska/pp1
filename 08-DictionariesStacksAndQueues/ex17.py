ICAO = {
    "a":"Alfa",
    "b":"Bravo",
    "c": "Charlie",
    "d":"Delta",
    "e":"Echo",
    "f":"Foxtrot",
    "g":"Golf",
    "h":"Hotel",
    "i":"India",
    "j":"Juliett",
    "k":"Kilo",
    "l":"Lima",
    "m":"Mike",
    "n":"November",
    "o":"Oscar",
    "p":"Papa",
    "q":"Quebec",
    "r":"Romeo",
    "s":"Sierra",
    "t":"Tango",
    "u":"Uniform",
    "v":"Victor",
    "w":"Whiskey",
    "x":"Xray",
    "y":"Yankee",
    "z":"Zulu"
}



#word = 'uek'
#word = 'barbara'
def spelling(n):
    sum = " " 
    for i in n:
        for key, val in ICAO.items():
            if i== key:
                sum +=val + " "
        else:
            pass
    return sum
if __name__=="__main__":
    word = input('Enter text: ')
    print(spelling(word))