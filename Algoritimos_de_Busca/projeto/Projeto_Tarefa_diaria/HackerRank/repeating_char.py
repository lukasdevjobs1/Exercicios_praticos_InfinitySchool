s = input().strip()

for i in range(len(s) - 1):
    if s[i].isalnum() and s[i] == s[i + 1]:
        print(s[i])
        exit()

print(-1)