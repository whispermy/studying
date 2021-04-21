def solution(brown, yellow):
    # answer = []
    x = ((brown // 2) // 2)
    y = (brown // 2) - x
    rect = (x-1)*(y-1) 
    
    while  rect != yellow:
        x += 1
        y -= 1
        rect = (x-1)*(y-1) 
    
    if x < y:
        x,y = y,x

    return [x+1,y+1]

print(solution(10,2))
