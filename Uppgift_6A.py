import calc

def eval_program(program, value_table={}):
    if calc.isprogram(program):
        statements = program_statements(program)
        return eval_statement(statements)
    else:
        return False
                
def eval_statements(statements):
    if calc.isstatements(statements):
       return eval_statement(calc.first_statement(statement)) \
           + eval_statements(calc.rest_statement(statement))
    else:
        return calc.empty_statements(statements)

def eval_statement(statement):
    if calc.isassignment(s):
     
        return eval_expression(calc.assignment_variable(s)) \
            + eval_expression(calc.assignment_expression(s))
   
    elif calc.isrepetition(s):
        
        return eval_expression(calc.repetition_condition(s)) \
            + eval_statement(calc.repetition_statements(s))
    elif calc.isselection(s):
        
    elif calc.isinput(s):
    
    elif calc.isoutput(s):
        
    else:

def eval_expression(expr):
    if

def eval_coniton(cond):

def eval_binary_expr(bin_expr):
    
def eval_binaty_opr(bin_opr):
    
def eval_cond_opr(cond_opr):

def eval_var(var):

def eval_const(const):
        

            
