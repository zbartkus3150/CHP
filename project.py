import itertools
import sys

def main():
    try:
        f = sys.stdin.readlines()
        k = int(f.pop(0).strip("\n"))
        s = f.pop(0).strip("\n")
        t = []
        tUnique = []
        for i in range(0, k):
            ti = f.pop(0).strip("\n")
            t.append(ti)
            tUnique.extend(list(ti))
        tUnique = set(filter(lambda x: x.isupper(), tUnique))
        t = list(set(t))
        subs = []
        for ti in t:
            for tj in t:
                if ti == tj:
                    continue
                if ti in tj:
                    subs.append(ti)
        t = [elem for elem in t if elem not in subs]
        lines = [x.strip("\n") for x in f]
        y = {}
        Y = []
        notUsed = {}
        count = 0
        for line in lines:
            count += 1
            if count > 26:
                print("NO", end ="")
                return
            upper = line.split(":")[0]
            lower = line.split(":")[1].strip("\n").split(",")
            for l in lower:
                if not l.isalpha() and l != '':
                    print("NO", end ="")
                    return
            if upper not in tUnique:
                notUsed[upper] = lower[0]
                continue
            elemToRemove = []
            for l in lower:
                if l not in s:
                    elemToRemove.append(l)
            lower = list(set([elem for elem in lower if elem not in elemToRemove]))
            y[upper] = lower
            Y.append(upper)
            
        replacement = {}
        isCorrect = False
        for elem in itertools.product(*y.values()):
            isCorrect = True
            replacement = {}
            for i in range(len(elem)):
                replacement[Y[i]] = elem[i]
            table = str.maketrans(replacement)
            for sub in t:
                replaced = sub.translate(table)
                if replaced not in s:
                    isCorrect = False
                    break
            if isCorrect:
                for key, value in replacement.items():
                    print(key + ":" + value)
                for key, value in notUsed.items():
                    print(key + ":" + value)
                return
        print("NO", end ="")
    except Exception as error:
        print("NO", end ="")

main()