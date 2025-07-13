def check_template(template: list[int], string: str) -> str:
    if len(template) != len(string):
        return "NO"
    template_map = {}
    string_map = {}
    for t, s in zip(template, string):
        if t in template_map and template_map[t] != s:
            return "NO"
        if s in string_map and string_map[s] != t:
            return "NO"
        template_map[t] = s
        string_map[s] = t
    return "YES"


t = int(input())
while t != 0:
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    while m != 0:
        print(check_template(template=a, string=input()))
        m -= 1
    t -= 1
