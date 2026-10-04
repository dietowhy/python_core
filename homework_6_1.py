tests = ["PASS", "FAIL", "PASS", "SKIP", "PASS"]

def count_pass(results):
    if not results:
        return 0

    first = results[0]
    rest = results[1:]

    return (1 if first == "PASS" else 0) + count_pass(rest)

print(count_pass(tests))
