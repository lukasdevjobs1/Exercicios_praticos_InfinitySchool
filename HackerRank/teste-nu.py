def main():
    n = int(input())
    phone_book = {input().split()[0]: input().split()[1] for _ in range(n)}
    
    try:
        while True:
            query = input()
            print(f"{query}={phone_book[query]}" if query in phone_book else "Not found")
    except EOFError:
        pass



