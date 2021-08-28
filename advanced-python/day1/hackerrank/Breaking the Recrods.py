#https://www.hackerrank.com/contests/aysi-sci-lesson-1-homework/challenges/breaking-best-and-worst-records

def main():
    n = int(input())
    scores = list(map(int,input().split()))
    if n == 1:
        print('{} {}'.format(0,0))
        return
    maximum = scores[0]
    minimum = scores[0]
    maximum_broken_counter = 0
    minimum_broken_counter = 0
    
    for num in scores[1:]:
        if num > maximum:
            maximum_broken_counter += 1
            maximum = num
        elif num < minimum:
            minimum_broken_counter += 1
            minimum = num
    print('{} {}'.format(maximum_broken_counter,minimum_broken_counter))

    
if __name__ == '__main__':
    main()
