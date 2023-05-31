import pickle
from velo import Velo

def main():
    try:
        with open("velo-pickle.dat", "rb") as f:
            verder_string = input("\nDruk 'v' om verder te gaan op de vorige situatie of 'o' om opnieuw te beginnen:")
            if verder_string == "v":
                app = pickle.load(f) 
            else:
                app = Velo()
    except FileNotFoundError:
        app = Velo()
    app.terminal_interface_weergeven()
    with open("Velo.dat", "wb") as f:
        pickle.dump(app, f)

#main()