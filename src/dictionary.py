
import numpy as np
from typing import TypedDict, List, Dict 
class WordData(TypedDict):
    map: List[Dict[str,any]]
    dica:str
    word:str
    length: int
class Dictionary():
    def __init__(self):
        
        self.words = [
            {
                "word":"gabriel", 
                "dica":"nome de um anjo"
            },{
                "word":"adelar", 
                "dica":"não sei o que dizer"
            }
        ]
        self.dict_map = {}
        self.loadWord()
    def loadWord(self) -> None:
        select_word = np.random.randint(len(self.words))
        temp_dict = []

        for i,char in enumerate(self.words[select_word]["word"]):
            map = {
                "char":char, 
                "position":i, 
                "show":False
            }
            temp_dict.append(map)
        data:WordData = {
            "map":temp_dict, 
            "dica":self.words[select_word]["dica"],
            "word":self.words[select_word]["word"], 
            "length": len(self.words[select_word]["word"])
        }
        
        self.dict_map = data
                
    def get_word(self) -> WordData:
        return self.dict_map