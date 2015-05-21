#Function to check if the given number is prime

def is_prime(x):
    
    if(x < 2):
        return False;

    for i in range(2, x-1):
        if(x%i == 0):
            return False;
    else: 
        return True