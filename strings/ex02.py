
# * output text generative 
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] ==  letter:
            return index 
        
        index = index + 1
    return -1 

# * create function models collect 
def is_reserve(models_regression, models_classification):
    if len(models_regression) != len(models_classification):
        return False 
    
    i = 0
    j = len(models_classification)
    
    while j > 0:
        if models_regression[i] != models_classification[j]:
            return False
        i = j+1
        j = j-1 
        return True 