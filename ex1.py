"""
Otwieranie i zapisywanie do pliku
"""
path = r'C:\Users\cp24\Desktop\Akademia Kodu\W1_pliki\ex1.txt'

def files_read(path):
    with open(path, "r", encoding='UTF8') as file:
        print(file.read()) #drukuje całą zawartość pliku
        print(file.read(3)) #drukuje pierwsze 3 znaki
        print((file.read())[1:10]) #traktujemy str jako listę i dobieramy się do konkretnych pozycji

#files_read(path)

def files_readlines(path):
    with open(path, "r", encoding='UTF8') as file:
        lines = [line.strip() for line in file]    #pokazuje zawartość jako listę
        #The strip() method removes any leading (spaces at the beginning) and trailing
        # (spaces at the end) characters (space is the default leading character to remove)
        print(lines, end='')
        #lub
        for line in lines:
            print(line)

        print(lines[-1]) #pokazuje tylko ostatnią

files_readlines(path)

def files_readline(path):
    with open(path, "r", encoding='UTF8') as file:
        print(file.readline(), end='')
        print(file.readline()) #kursor przesówa się dalej

def append_to_file(path, wpisz):
    with open(path, "a", encoding='UTF8') as file:
        file.write("\n{}".format("6 Linijka"))
        file.writelines(wpisz)

if __name__ == '__main__':
    wpisz = ["\n7 Linijka", "\n8 Linijka", "\n9 Linijka"]
    #append_to_file(path)
    files_read(path)