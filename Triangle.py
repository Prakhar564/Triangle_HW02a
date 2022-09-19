

def classifyTriangle(a,b,c):

    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'
    
    if (a>= (b + c)) or (b>= (a + c)) or (c >= (a + b)):
        return 'Not A Triangle'
        
    if a == b and b == c and c==a :
        return 'Equilateral'
    elif ((a * a) + (b * b)) == (c * c) or ((b * b) + (c * c)) == (a*a) or ((a * a) + (c * c)) == (b*b) :
        return 'Right'
    elif (a != b) and  (b != c) and (c != a):
        return 'Scalene'
    elif a==b or b==c or c==a:
        return 'Isosceles'    
    
         
        

 