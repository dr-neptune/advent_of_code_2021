from toolz import reduce, nth

with open('input.txt') as f:
    syn = f.read().strip()


match_dict = {'(': ')',
              '[': ']',
              '{': '}',
              '<': '>'}

# part 1
break_scores = {')': 3,
                ']': 57,
                '}': 1197,
                '>': 25137}

stack = []
syntax_errors = []
for fst in syn.split('\n'):
    for c in fst:
        if c in match_dict.keys():
            stack.append(c)
        else:
            lst = stack[-1]
            if c == match_dict[lst]:
                stack.pop()
            else:
                syntax_errors.append(c)
                break

sum([break_scores[d] for d in syntax_errors])

# part 2
add_scores = {')': 1,
              ']': 2,
              '}': 3,
              '>': 4}

results = []
stack = []
syntax_errors = []
for fst in syn.split('\n'):
    for c in fst:
        if c in match_dict.keys():
            stack.append(c)
        else:
            lst = stack[-1]
            if c == match_dict[lst]:
                stack.pop()
            else:
                stack = []
                break
    if stack:
        autocomplete = []
        for s in stack:
            autocomplete.append(match_dict[s])
        results.append("".join(autocomplete))

get_points = lambda ls: reduce(lambda x, y: (5 * x) + y, [add_scores[i] for i in ls], 0)
nth((len(results) - 3) // 2, sorted(map(get_points, results)))
