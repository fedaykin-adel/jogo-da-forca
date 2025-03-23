
import sys
from .dictionary import Dictionary
class Gallows:
    def __init__(self):
        self.used_words = []
        self.dict = Dictionary()    
        self.select_word = self.dict.get_word()
        self.stop = True 
        self.count_correct_word = 0
        self.errors = 0
        
        self.word = self.select_word['word']
        self.guess = True
        self.need_help = True
        self.char_input = ""
        
    def win_display(self) -> None:
        print("parabens, voce ganhou :3")
        self.stop = False
        
    def guess_word(self) -> None:
        if self.count_correct_word >= self.select_word["length"] / 2 and self.guess: 
            guess = input("Quer tentar advinhar a palavra? ... se errar havera punicoes (Y/N)")

            if guess == "Y":
                word = input("Digite a palavra: ")

                if word == self.word:
                    self.win_display()
                else: 
                    self.errors += 3
                    self.guess = False
            else:
                self.guess = False

    def win(self) -> bool:
        win = all(item["show"] for item in self.select_word["map"])
        if win: self.win_display()
    def draw_stick(self):
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
        print(stages[self.errors])
    def display_chars(self):
        word_select = [item['char'] if item["show"] else "_" for item in self.select_word["map"]]
        print(f"letras: {" , ".join(word_select)}, tamanho: {self.select_word["length"]}, errors: {self.errors}")
       
    def catch_char(self):
        
        char = input("digite uma letra: ")
        if char in self.used_words:
            print("palavra ja usada ;-;")
        
        if self.valid_word(char):
            self.used_words.append(char)
            self.char_input = char
        
    def display_clear(self):
        sys.stdout.write("\033[H\033[J")
        sys.stdout.flush()
        
    def display(self) -> str:
        self.display_clear()
        self.draw_stick()
        self.display_chars()
        self.catch_char()
        self.guess_word()
        self.help()
        
    
    def help(self)->None:
        if self.errors >= 3 and self.need_help:
            resp = input("Quer receber ajuda? ... Havera punição (Y/N)")
            if resp == "Y":
                print(f"Dica: {self.select_word["dica"]}")
                self.errors += 2
                self.need_help = False
            else:
                self.need_help = False
    def valid_word(self,char:str):
        if not char.isalpha() or len(char) != 1: 
            self.errors += 1
            return False 
        return True
        
    def verify_exist_word(self):
        found = False
        
        for map in self.select_word["map"]:
            if map["char"] == self.char_input:
                map["show"] = True
                found = True
                continue
        
        if not found: 
            self.errors+=1
        else:
            self.count_correct_word += 1
    def losse(self):
        if self.errors >= 6:
            print("perdeu otario!")
            self.stop = False
    
    def run(self):
        while self.stop: 
            self.display()
            self.verify_exist_word()
            self.win()
            self.losse()    
            

            
                
        
