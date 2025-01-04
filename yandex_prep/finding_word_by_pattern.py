def my_match(pattern: str, arr: list[str]):
    output = []
    if len(pattern) < 1:
        return arr
    for str in arr:
        cur = 0
        for char in str:
            if pattern[cur] == char:
                cur += 1

                if cur == len(pattern):
                    output.append(str)
                    break
    return output


print(my_match("kbz", ["kobezzza", "iuq", "kibiza", "zprc"]))
