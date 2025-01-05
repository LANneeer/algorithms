# File
# 1
ids = []
with open("temp.txt", "r") as file:
    for line in file:
        print(line.strip())
        ids.append(line.strip())
print(ids)

# 2
unique_ids = set(ids)
print(unique_ids, len(unique_ids))

# 3
with open("temp-company.txt", "r") as f:
    for line in f:
        line = line.strip().split()
        medium = line[0]
        source = line[1]
        amount_paid = float(line[2].replace(",", "."))
        print(source, medium, amount_paid)

# 4
with open("temp-company.txt", "r") as f:
    total_sum = 0
    for line in f:
        line = line.strip().split()
        amount_paid = float(line[2].replace(",", "."))
        total_sum += amount_paid
        print(" Current expenses: {:.2f}".format(total_sum))

# 5
with open("temp-company.txt", "r") as f:
    total_sum = 0
    for line in f:
        line = line.strip().split()
        amount_paid = float(line[2].replace(",", "."))
        if line[1] == "google":
            total_sum += amount_paid
            print("Google expenses: {:.2f}".format(total_sum))
