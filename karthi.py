NO = 256

def maxdc(str, n): 
  
   
    count = [0] * NO 
      
    for i in range(n): 
        count[ord(str[i])] += 1
      
    maxd = 0
    for i in range(NO): 
        if (count[i] != 0): 
            maxd += 1    
      
    return maxd 
  
def smdc(str): 
  
    n = len(str)     
  

    maxd = maxdc(str, n) 
    minl = n      
      
 
    for i in range(n): 
        for j in range(n): 
            subs = str[i:j] 
            subs_lenght = len(subs) 
            subdc = maxdc(subs,subs_lenght) 
              
 
            if (subs_lenght < minl and 
                maxd == subdc): 
                minl = subs_lenght 
  
    return minl 
  
 
if __name__ == "__main__": 
      
    str1 = str (input("enter string in lower case: "))
    l = smdc(str1)
    print( "The length of the smallest substring",l) 