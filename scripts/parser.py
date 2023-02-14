import argparse
import re


parser = argparse.ArgumentParser(prog="Lizard parser", description="Parse lizard output")
parser.add_argument('-f', '--file', help='file to input', default='data/lizard.data')
parser.add_argument('-s', '--sorton', help='sort on (nloc|ccn)', default='ccn')
parser.add_argument('-r', '--reverse', help='reverse sorting', action='store_true')
args = parser.parse_args()

def main():

    # possible values to sort on
    sort_on = { 'ccn': 2, 'nloc': 1, 'n/c': 3, 'c/n': 4 }

    f = open(args.file, 'r').read().rstrip().split('\n')
    lines = []
    for line in f:
        if re.search('^ {1,10}[0-9].*$', line) is not None:
            lines.append(line)
    scores = []
    for line in lines:
        l = list(filter(bool, line.split(' ')))
        # Structure of measurement
        # NLOC    CCN   token  PARAM  length  location  
        nloc = float(l[0])
        ccn = float(l[1])
        token = float(l[2])
        param = float(l[3])
        length = float(l[4])
        filename = l[5]
        nlocpccn = nloc / ccn if ccn > 0 else -1
        ccnpnloc = ccn / nloc if nloc > 0 else -1
        scores.append([filename, nloc, ccn, nlocpccn, ccnpnloc, token, param, length])
    if args.sorton.lower() in sort_on:
        scores = sorted(scores, key=lambda x : x[sort_on[args.sorton.lower()]])
    else:
        print("Error: Sort-On not valid argument. Valid are:\n\t",end="")
        for k in sort_on:
            print("k", end=" ")
        print()

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
    print("--- AVERAGE, TOTAL ---")
    print(f"NLOC: {round(total[0], 5)},\t {round(total[0] / len(scores), 5)}")
    print(f"CCN:  {round(total[1], 5)},\t {round(total[1] / len(scores), 5)}")
    print(f"N/C:  {round(total[2], 5)},\t {round(total[2] / len(scores), 5)}")
    print(f"C/N:  {round(total[3], 5)},\t {round(total[3] / len(scores), 5)}")

if __name__=='__main__':
    main()