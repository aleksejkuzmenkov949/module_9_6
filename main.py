def all_variants(text):
    for i in range(len(text)):
        for j in range(i+1, len(text)+1):
            yield text[i:j]

a = sorted(all_variants("abc"), key=lambda x: (len(x), x))
for i in a:
    print(i)
