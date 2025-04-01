'''
sad convertion tools
'''

from typing import NamedTuple
import re

from numpy import pi

class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int


def tokenize(code):
    #keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    # Define keywords that are element types in SAD
    keywords  = ['QUAD', 'MARK', 'CAVI', 'BEAMBEAM', 'APERT', 'SOL', 'DRIFT', 'BEND', 'SEXT','OCT', 'MULT', 'MONI', 'LINE','MAP', 'COORD','APERT']
    
    #Regex patterns to identify different token types
    token_specification = [
        ('NUMBER',   r'([+-])?\d+(\.\d*)?(e[-+]\d+)?|([+-])?\d*(\.\d*)(e[-+]\d+)?'),  # Integer or decimal number
        ('ASSIGN',   r':='),           # Assignment operator
        ('EQUAL',    r'='),            # Equality operator
        ('END',      r';'),            # Statement terminator
        ('COMMENT',  r'!'),            # 
        ('LBR',      r'\('),           # 
        ('RBR',      r'\)'),           # 
        ('UNIT',     r'DEG'),          # 
        ('ID',       r'[A-Za-z0-9_]+'), # Identifiers
        ('OP',       r'[+\-*/]'),      # Arithmetic operators
        ('NEWLINE',  r'\n'),           # Line endings
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.'),            # Any other character
    ]

    # Compile regex into one big expression
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            #print(f"debug: number: {value}")
            value = float(value) #if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            #kind = value
            kind = "ELEMENT_TYPE"
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        
        # Return token as a named tuple
        yield Token(kind, value, line_num, column)


class LatticeObject:
    def __init__(self) -> None:
        self.type = "None"
        self.name = None
        self.parameters = {}

    def get_parameter(self,name):
        try:
            return self.parameters[name]
        except:
            return 0.0
    
    def __str__(self):
        #return self.name + " : " + self.type + ":" + str(self.parameters)
        #return self.name + " : " + str(self.parameters)
        return f"{self.type} : {self.name}  :  {self.parameters}"


def process_stack(token_stack):

    debug = False

    if debug: print(f"processing token stack: {token_stack}")

    lattice_objects = []
    line_def = []

    in_element_def = False
    in_line = False

    element_name = None
    element_type = None

    while len(token_stack) > 0: 

        if debug: print(f"remaining stack size {len(token_stack)}, next token {token_stack[-1]}")

        if token_stack[-1].type == 'ELEMENT_TYPE' : #in keywords:
            t1 = token_stack.pop()
            element_type = t1.value
            if element_type == 'LINE':
                in_line = True

        if not in_element_def: # check that stack starts with element definition
            if token_stack[-1].type == "ID" and token_stack[-2].type == "EQUAL" and token_stack[-3].type == "LBR":
                if debug: print(f"starting element def")
                in_element_def = True
                t1 = token_stack.pop()
                token_stack.pop()
                t3 = token_stack.pop()
                element_name = t1.value
                e = LatticeObject()
                e.type = element_type
                e.name = element_name
                if not in_line : lattice_objects.append(e)
            else:
                print(f"ERROR, printing stack")
                print(token_stack)

        if in_element_def:
            if debug: print(f"parsing element def, next token: {token_stack[-1]}")
            if token_stack[-1].type == "RBR":
                if debug: print(f"end elemenyt def")
                in_element_def = False
                token_stack.pop()

            if len(token_stack) > 0:

                if in_line: # line def
                    if token_stack[-1].type == "ID":
                        t1 = token_stack.pop()
                        line_def.append(t1.value)
                    if token_stack[-1].type == "OP":
                        line_def.append(t1.value) # will apply "-" to next element
                else: # element def

                    if token_stack[-1].type == "ID" and token_stack[-2].type == "EQUAL" and token_stack[-3].type == "NUMBER":
                        if debug: print(f"found parameter def")
                        t1 = token_stack.pop()
                        token_stack.pop()
                        t3 = token_stack.pop()
                        lattice_objects[-1].parameters[t1.value] = t3.value

                        if token_stack[-1].type == "UNIT":
                            if token_stack[-1].value == "DEG":
                                lattice_objects[-1].parameters[t1.value] = t3.value * pi / 180.
                            token_stack.pop()

        if len(token_stack) > 0:
            if token_stack[-1].type == "END":
                token_stack.pop()

                
    return lattice_objects, line_def



class SADObject:
    def __init__(self, fname, debug=False) -> None:
        self.lattice_objects = {}
        self.lattice_list = []
        self.fname = fname
        self.debug = debug
        self.parse()

    def parse(self):

        text = open(self.fname).read()
        token_stack = []
        object_defs = []
        object_dict = {}
        line_def = []

        for token in tokenize(text):
            #print(token)
            token_stack = [token] + token_stack # qppend in reverse order, for popping
            if token.type == "END":
                print(f"statement read, processing stack...")
                objs, line_def = process_stack(token_stack)
                token_stack.clear()

                for o in objs:
                    print(f"{o.type} : {o}")
                    object_defs.append(o)
                    object_dict[o.name] = o 

                print(f"line : {line_def}")

        self.lattice_objects = object_defs
        self.object_dict = object_dict
        self.lattice_list = line_def


def read_sad(fname, debug = False):
    sad_object = SADObject(fname)
    return sad_object


def output_elegant():
    pass

def output_ocelot():
    pass