import sys
import re
from utils import choose_input_file
from lps import solve_lps
from party import solve_party

def main():
    try:
        path = choose_input_file()
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        return
    with open(path, encoding='utf-8') as f:
        lines = [l.rstrip('\n') for l in f]

    # detectamos tipo de problema
    if re.search('[A-Za-z]', lines[1]):
        result = solve_lps(lines)
    else:
        result = solve_party(lines)

    print('\n'.join(result))

if __name__ == '__main__':
    main()
