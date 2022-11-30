import argparse
import sys
import math

def main():
    parser = argparse.ArgumentParser(description="Rangkaian Seri")
    parser.add_argument('--u', type=float, default=1.0,
                        help='Berapa resistornya ?')
    parser.add_argument('--o', type=float, default=1.0,
                        help='Berapa nilai resistansi per resistornya ?')
    parser.add_argument('--rumus', type=str, default='Ohm',
                        help='Total Nilai Resistansinya =')
    args = parser.parse_args()
    sys.stdout.write(str(rumus(args)))

def calc(args):
    

if __name__ == '__main__':
    main()