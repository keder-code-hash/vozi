import random 
import string

def gen_random_code(id):
    code_pref_range=len(str(id))
    characters = string.ascii_letters
    code_pref = ''.join(random.choice(characters) for i in range(6-code_pref_range))
    code="VOZI"+str(code_pref)+str(id)
    return code