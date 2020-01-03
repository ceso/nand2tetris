# Line-of-code -> Integer
def write_asm_f(asm_code, filename):
    filename = filename.replace('.asm', '.hack')
    
    with open(filename, 'w') as f:
        for line in asm_code:
            f.write("%s\n" % line)

def get_abit(comp):
    ''' Set abit. if M then will be C so 1, otherwise is A and is 0 '''
    if comp.find('M') != -1:
        return '1'
    else:
        return '0'

# String Integer Vale=None -> Int/None
def parse_int(s, base=10, val=None):
    ''' Try to check if the value is an integer '''
    try:
        return int(s, base)
    except ValueError:
        return val

# determine if what type of instruction the line of code is
is_a_inst = lambda x: x.find('@') != -1
is_c_inst = lambda x: x.find('(') == -1 and x.find('@') == -1
is_label = lambda x: x.find('(') != -1 and x.find(')') != -1

# File-ASM -> Lines-of-code
def prepare_code(filename):
    ''' Deletes comments and blank lines '''
    new_code = []

    with open(filename) as f:
        for line in f:
            new_line = line.split("//")[0].replace(" ","").rstrip()
            
            if new_line != '':
                new_code.append(new_line)         

    return new_code
       
