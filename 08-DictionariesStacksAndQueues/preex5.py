import json
#2

movie1 = {
    "title": "Minority Report",
    "director" :"Steven Spielberg",
    "composer":  "John Williams",
    "actors": ["Tom Cruise","Colin Farell","Samantha Morton","Max von Sydow"],
    "is_awesome": True,
    "budget": 1020000000,
    "cinematographer":"Janusz Kami\u0144ski"
}
movie_file = open('movie.txt',"w", encoding ="utf-8")
done = json.dump(movie1, movie_file, ensure_ascii= False)
print(done)
print(movie1.keys())
movie_file.close()

#stos, LIFO
#Last In First Out
#do zapisywania zawartości rejestrów procesora
#do przechowywania adresów pamięci i zmiennych
#mamy dostęp tylko do elementu na szczycie (astatnio dodanego)
#dodajemy na stos(a) i usuwamy ze stosu(a)

#kolejka
#First In First Out
#nowe dane są dodawane do końca kolejki, ale uwalniamy z niej te dane, które znajdują się na początku do dalszego obracania
#nowy element jest dodawany na końcu, jako pierwszy usuwany jest element z początku kolejki
