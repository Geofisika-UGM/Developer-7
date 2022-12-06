import argparse
import sys
from AlCore import chose
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--jn', type=str, default='none',
                        help='Rangkaian seri (seri) atau paralel (par)')
    parser.add_argument('--jm', type=int, default='Ohm',
                        help='Jumlah Rangkaian')
    args = parser.parse_args()
    sys.stdout.write(str(opr(args)))

def opr (args):
    if args.jn == 'none':
        return 'masukan jenis rangkaian'
    elif args.jn == 'seri':
        chose(args.jn,args.jm)
    elif args.jn == 'par':
        chose(args.jn,args.jm)
    else:
        return 'Gunakan operasi dengan tepat'

if __name__ == '__main__':
    main()