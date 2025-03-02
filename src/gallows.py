
import sys
from .dictionary import Dictionary
class Gallows:
    def __init__(self):
        self.used_words = []
        self.dict = Dictionary()    
        self.select_word = self.dict.get_word()
        self.tamanho = len(self.select_word["word"])
        self.stop = True 
        self.count_correct_word = 0
        self.errors = 0
        
        self.word = self.select_word['word']
        self.guess = True
        self.need_help = True
        self.win = False
    def win_display(self) -> None:
        if self.win:
            print("parabens, voce ganhou :3")
            self.stop = False
    # def stage():
        
    def guess_word(self) -> None:
        if self.count_correct_word >= self.tamanho / 2 and self.guess: 
            guess = input("Quer tentar advinhar a palavra? ... se errar havera punicoes (Y/N)")

            if guess == "Y":
                word = input("Digite a palavra: ")

                if word == self.word:
                    self.win = True
                    self.win_display()
                else: 
                    self.errors += 3
                    self.guess = False
            else:
                self.guess = False

    def fully_word(self) -> bool:
        count = 0
        print(self.select_word)
        for x in self.select_word["map"]:
            if x["show"] == True:
                count += 1
        return count == self.tamanho  
    
    def display(self) -> str:
        # os.system('cls' if os.name == 'nt' else 'clear')
        stages = [
            """
            +---+
            |   |
                |
                |
                |
                |
            =========
            """,
            """
            +---+
            |   |
            O   |
                |
                |
                |
            =========
            """,
            """
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========
            """,
            """
            +---+
            |   |
            O   |
           /|   |
                |
                |
            =========
            """,
            """
            +---+
            |   |
            O   |
           /|\\  |
                |
                |
            =========
            """,
            """
            +---+
            |   |
            O   |
           /|\\  |
           /    |
                |
            =========
            """,
            """
            +---+
            |   |
            O   |
           /|\\  |
           / \\  |
                |
            =========
            """
        ]
        sys.stdout.write("\033[H\033[J")
        sys.stdout.flush()

        print(stages[self.errors])
        word_select = [item['char'] if item["show"] else "_" for item in self.select_word["map"]]
       
        print(f"letras: {" , ".join(word_select)}, tamanho: {self.tamanho}, errors: {self.errors}")
        char = input("digite uma letra: ")
        if char in self.used_words:
            print("palavra ja usada ;-;")

        self.used_words.append(char)
        return char
    
    def help(self)->None:
        resp = input("Quer receber ajuda? ... Havera punição (Y/N)")
        if resp == "Y":
            print(f"Dica: {self.select_word["dica"]}")
            self.errors += 2
            self.need_help = False
        else:
            self.need_help = False

    def run(self):
        while self.stop: 
            self.win_display()
            char = self.display()
            print(char)
            

            found = False
            for map in self.select_word["map"]:
                if map["char"] == char:
                    map["show"] = True
                    found = True
                    continue
            if self.fully_word():
                self.win = True
                self.win_display()
                # continue    
            
            self.guess_word()
            
            if not char.isalpha() or len(char) != 1: self.errors += 1
            
            
            if self.errors >= 6:
                print("perdeu otario!")
                self.stop = False
                break 

            if self.errors >= 3 and self.need_help:  
                self.help()
                self.need_help = False
                continue
            
            if not found: 
                self.errors+=1
            else:
                self.count_correct_word += 1
                
        
