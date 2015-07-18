def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    lower_alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
    upper_alpha = [upper_alpha.upper() for upper_alpha in lower_alpha]
    dic={}  
    for i in range(0,len(lower_alpha)):  
        dic[lower_alpha[i]]=lower_alpha[(i+shift)%len(lower_alpha)]

    dic2={}
    for i in range(0,len(upper_alpha)):  
        dic2[upper_alpha[i]]=upper_alpha[(i+shift)%len(upper_alpha)]


    d3 = dict(dic, **dic2)
    return d3
