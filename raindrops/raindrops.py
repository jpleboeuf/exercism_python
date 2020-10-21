import sys


def convert(number:int):

    def is_factor(n:int, f:int):
        return n % f == 0

    raindrop_sound = [
            (3, "Pling"),
            (5, "Plang"),
            (7, "Plong"),
        ]
    raindrop_sounds = ""
    for kn, ks in raindrop_sound:
        if is_factor(number, kn):
            raindrop_sounds += ks
    return raindrop_sounds if raindrop_sounds else str(number)


def main():

    def is_intstring(s:str):
        try:
            int(s)
            return True
        except ValueError:
            return False

    argn = len(sys.argv)
    if argn == 2 and is_intstring(sys.argv[1]):
        print(convert(int(sys.argv[1])))
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} [number:int]")

if __name__ == '__main__':
    main()
