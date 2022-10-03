def plus_row_start():
    print("+", end="")
    
def bar_row_start():
    print("|", end="")
    
def plus_row_end(n):
    print(f"{n*(' -')} +", end="")
    
def bar_row_end(n):
    print(f"{n*('  ')} |", end="")
    
def rows(row_start, row_end ,n,n_prime):
    row_start()
    for i in range(n_prime):
        row_end(n)
    print()

def shape(n, m, n_prime, m_prime):
    for i in range(m_prime):
        rows(plus_row_start, plus_row_end, n, n_prime)
        for x in range(m):
            rows(bar_row_start, bar_row_end, n, n_prime)
    rows(plus_row_start, plus_row_end, n, n_prime)
    
shape(5,4,6,7)
    
    
 
    
    