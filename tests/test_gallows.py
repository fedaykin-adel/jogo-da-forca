import pytest
from unittest import mock
from io import StringIO
from src.gallows import Gallows


def test_win():
    game = Gallows()
    game.stop = True 
    game.win = True
    game.win_display()
    assert game.win
    assert not game.stop

def test_guess_word_correct():
    game = Gallows()
    game.select_word = {"word":"test", "dica":"test", "map": [{"char": "t", "position": 0, "show": False}]}
    game.count_correct_word = 2
    game.tamanho = 4
    game.guess = True 
    game.word = "test"

    with mock.patch('builtins.input', side_effect=["Y", "test"]):
        game.guess_word()

    assert game.win == True

def test_guess_word_incorrect():
    game = Gallows()
    game.select_word = {"word":"test", "dica":"test","map": [{"char": "t", "position": 0, "show": False}]}
    game.count_correct_word = 4
    game.tamanho = 4
    game.guess = True 
    
    with mock.patch('builtins.input', side_effect=["Y", "errado"]):
        game.guess_word()
        
    assert game.errors == 3

def test_help():
    game = Gallows()
    game.errors = 0
    game.need_help = True
    game.select_word = {"word":"test", "dica":"test","map": [{"char": "t", "position": 0, "show": False}]}

    with mock.patch('builtins.input', return_value="Y"):
        with mock.patch("sys.stdout", new=StringIO()) as fake_out:
            game.help()
            output = fake_out.getvalue().strip()

    assert "test" in output
    assert game.errors == 2
    assert not game.need_help

def test_display():
    game = Gallows()
    game.errors = 1
    game.select_word = {"word":"test", "dica":"test","map": [{"char": "t", "position": 0, "show": True},{"char": "e", "position": 1, "show": False}]}
    with mock.patch("builtins.input", return_value="e"):
        with mock.patch("sys.stdout", new=StringIO()) as fake_out:
            char =  game.display()
            output = fake_out.getvalue().strip()
    assert "letras: t , _" in output
    assert char == "e"

def test_fully_word():
    game = Gallows()
    game.select_word = {"word":"te", "dica":"te","map": [{"char": "t", "position": 0, "show": True},{"char": "e", "position": 1, "show": True}]}
    game.tamanho = 2
    
    assert game.fully_word() == True

def test_run_win_condition():
    game = Gallows()
    game.stop = True 
    game.errors = 0 
    game.tamanho = 1
    game.select_word = {"word":"t", "dica":"te","map": [{"char": "t", "position": 0, "show": True}]}
    
    with mock.patch("builtins.input", side_effect=["t"]):
        with mock.patch("sys.stdout", new=StringIO()):
            game.run()

    assert not game.stop