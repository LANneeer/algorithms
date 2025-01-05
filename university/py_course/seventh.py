import re

test_1 = """
1
John Smith
11/02/1990
john@gmail.com
+7(701)777-77-77
KZ12345678901234567890
"""

regexes = {
    "numbers": r"^\n(\d+){1}\n",
    "name": r"([A-Z][a-z]+ [A-Z][a-z]+)",
    "date_of_birth": r"\d+/\d+/\d+",
    "email": r"[\w+]+@[\w+]+\w{2,4}",
    "phone": r"\+?\d{1,3}\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{2}[\s.-]?\d{2}",
    "iban": r"KZ\d{20}",
}
file = open("Output.txt", "w+")
for item, regex in regexes.items():
    if re.findall(regex, test_1):
        file.writelines(re.findall(regex, test_1)[0] + "\n")
    else:
        raise ValueError(f"Missing {item}")
