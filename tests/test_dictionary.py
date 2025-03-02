from src.dictionary import Dictionary, WordData

def test_load_word():
    dictionary = Dictionary()
    result = dictionary.get_word()
    assert "word" in result 
    assert "dica" in result
    assert "map" in result

    assert isinstance(result["map"],list)
    
    assert all("char" in char_map for char_map in result["map"])
    assert all("position" in char_map for char_map in result["map"])
    assert all("show" in char_map for char_map in result["map"])
    
    assert isinstance(result["word"],str)
    assert isinstance(result["dica"],str)
    
    print("test de load_word() passou :3 ")

def test_random_selection():
    dictionary = Dictionary()
    resultados = set()
    for _ in range(10):
        dictionary.loadWord()
        result = dictionary.get_word()["dica"]
        resultados.add(result)
    assert len(resultados) > 1
    print("test de test_random_selection() passou :3 ")
    