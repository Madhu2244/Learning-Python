#https://www.hackerrank.com/contests/aysi-sci-lesson-1-homework/challenges/the-birthday-bar

def main():
    #initializing everything
    n = int(input())
    bar = list(map(int, input().split()))
    d,m = map(int,input().split())
    result = 0
    
    #edge case
    if len(bar) < m:
        print(0)
    
    #initial pass up from [0,m-1]
    sum = 0
    for i in bar[:m]:
        sum += i
    if sum == d:
        result += 1
    
    #sliding window
    removal_index = 0
    for i in bar[m:]:
        sum += i
        sum -= bar[removal_index]
        if sum == d:
            result += 1
        removal_index += 1
            
    print(result)  
        
        
    #d ron birth day
    #m month
    

    
if __name__ == '__main__':
    main()
