import argparse
import os
import re
import sys

# possible values to sort on
sort_on = { 'ccn': 2, 'nloc': 1, 'n/c': 3, 'c/n': 4 }
parser = argparse.ArgumentParser(prog="Lizard parser", description="Parse lizard output")
parser.add_argument('-f', '--file', help='file to input', default='data/lizard.data')
parser.add_argument('-s', '--sorton', help='sort on '+' '.join(sort_on.keys()), default='ccn')
parser.add_argument('--span', help='only include a span, e.g. ccn:a-b', default='', type=str)
parser.add_argument('--nonclass', help='remove classes', action='store_true')
parser.add_argument('-r', '--reverse', help='reverse sorting', action='store_true')
args = parser.parse_args()

def main():
    f = open(args.file, 'r').read().rstrip().split('\n')

    lines = []
    for line in f:
        if re.search('^ {1,10}[0-9].*$', line) is not None:
            lines.append(line)
    scores = []

    nloc_span = [None, None]
    ccn_span = [None, None]

    if args.span:
        conditions = args.span.split(' ')
        for condition in conditions:
            if condition == '':
                continue
            val = condition.split(':')
            if len(val) < 2:
                print(f"Error: Invalid filtering, ignoring '{condition}'", file=sys.stderr)
                continue
            v = val[1].split('-')
            if val[0] == 'ccn':
                ccn_span[0] = int(v[0])
                ccn_span[1] = int(v[1])
            if val[0] == 'nloc':
                nloc_span[0] = int(v[0])
                nloc_span[1] = int(v[1])

    not_in_range = lambda x, r : (r[0] is not None and x < r[0]) or (r[1] is not None and x > r[1])
    for line in lines:
        l = list(filter(bool, line.split(' ')))
        # Structure of measurement
        # NLOC    CCN   token  PARAM  length  location  
        filename = l[5]
        ignore_file = False
        if args.nonclass and os.path.exists(filename):
            temp = open(filename, 'r').read().rstrip().split('\n')
            for ln in temp:
                if ln[:5] == 'class':
                    ignore_file = True
                    break
        if ignore_file:
            break

        nloc = float(l[0])
        if not_in_range(nloc, nloc_span):
            continue
        ccn = float(l[1])
        if not_in_range(ccn, ccn_span):
            continue
        token = float(l[2])
        param = float(l[3])
        length = float(l[4])
        nlocpccn = nloc / ccn if ccn > 0 else -1
        ccnpnloc = ccn / nloc if nloc > 0 else -1
        scores.append([filename, nloc, ccn, nlocpccn, ccnpnloc, token, param, length])
    if args.sorton.lower() in sort_on:
        scores = sorted(scores, key=lambda x : x[sort_on[args.sorton.lower()]], reverse=args.reverse)
    else:
        print("Error: Sort-On not valid argument. Valid are:\n\t",end="", file=sys.stderr)
        for k in sort_on:
            print(k, end=" ", file=sys.stderr)
        print(file=sys.stderr)
        exit(1)

    # nloc ccn nloc/ccn ccn/nloc
    total = [0, 0, 0, 0]
    for score in scores:
        print(score[0])
        print(f"\tNLOC: {round(score[1], 5)}")
        total[0] += score[1]
        print(f"\tCCN: {round(score[2], 5)}")
        total[1] += score[2]
        print(f"\tNLOC/CCN: {round(score[3], 5)}")
        total[2] += score[3]
        print(f"\tCCN/NLOC: {round(score[4], 5)}")
        total[3] += score[4]

    print()
    print("---\t AVERAGE,\t TOTAL ---")
    print(f"NLOC: \t {round(total[0] / len(scores), 3)},\t\t {round(total[0], 3)}")
    print(f"CCN:  \t {round(total[1] / len(scores), 3)},\t\t {round(total[1], 3)}")
    print(f"N/C:  \t {round(total[2] / len(scores), 3)},\t\t {round(total[2], 3)}")
    print(f"C/N:  \t {round(total[3] / len(scores), 3)},\t\t {round(total[3], 3)}")
    print()
    print(f"Sorted by {args.sorton}")

if __name__=='__main__':
    main()
