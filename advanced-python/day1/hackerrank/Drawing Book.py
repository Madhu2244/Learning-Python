#https://www.hackerrank.com/contests/aysi-sci-lesson-1-homework/challenges/drawing-book

def main():
    total_pages = int(input())
    page_number = int(input())
    
    if (total_pages // page_number >= 2):
        print(page_number // 2)
    else:
        print ((total_pages // 2) - (page_number // 2))
    
if __name__ == '__main__':
    main()
