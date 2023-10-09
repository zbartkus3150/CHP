import itertools

def main():
    try:
        filename = input()
        f = open(filename, "r")
        k = int(f.readline())
        if k < 1:
            return "NO"
        s = f.readline().strip("\n")
        t = []
        tUnique = []
        for i in range(0, k):
            ti = f.readline().strip("\n")
            t.append(ti)
            tUnique.extend(list(ti))
        tUnique = set(filter(lambda x: x.isupper(), tUnique))
        t = list(set(t))
        lines = f.readlines()
        y = {}
        Y = []
        count = 0
        for line in lines:
            count += 1
            upper = line.split(":")[0]
            if upper not in tUnique:
                continue
            lower = line.split(":")[1].strip("\n").split(",")
            elemToRemove = []
            for l in lower:
                if l not in s:
                    elemToRemove.append(l)
            lower = [elem for elem in lower if elem not in elemToRemove]
            y[upper] = lower
            Y.append(upper)
            if count > 26:
                return "NO"
            
        replacement = {}
        isCorrect = False
        for elem in itertools.product(*y.values()):
            isCorrect = True
            replacement = {}
            for i in range(len(elem)):
                replacement[Y[i]] = elem[i]
            for sub in t:
                replaced = ""
                for letter in sub:
                    if letter in Y:
                        replaced += replacement[letter]
                    else:
                        replaced += letter
                if replaced not in s:
                    isCorrect = False
                    break
            if isCorrect:
                answer = []
                for key, value in replacement.items():
                    answer.append(key + ":" + value + "\n")
                    # print(key + ":" + value)
                # print(answer)
                return answer
        # print("NO")
        return "NO"
    except Exception as error:
        # print(error)
        return "NO"

main()