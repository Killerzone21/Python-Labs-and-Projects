scores = [25,21,22,26,19,29]
scores.remove(min(scores))
scores.remove(max(scores))
print(scores)
print(len(scores))
counter = 0
tot = 0
for i in range(len(scores)):
    counter += 1
    tot += scores[i]
print(tot/counter)
