lib_books_count, list_books_count = int(input()), int(input())
lib_books = []
for i in range(lib_books_count):
    lib_books.append(input().lower().strip())
#lib_books = [input() for i in range(lib_books_count)]
for i in range (lib_books_count):
    book = input().lower().strip()
    if book in lib_books:
        print('yes')
    else:
        print('no')

#print('yes' if input().lower().strip() in lib_books else 'no')

# print(input()[-1])
#
# print(map(len, input().split('р'))) opopoppoppooppppppppppp