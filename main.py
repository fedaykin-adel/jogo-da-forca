from src import Gallows

if __name__ == "__main__":
    game = Gallows()
    try:
        game.run()
    except:
        print("\n Exit")
