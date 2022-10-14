# this function is creating initiate table
def initiate_table(first, last):
    headers = []
    for i in range(ord(first), ord(last) + 1):
       headers.append(chr(i))
    return headers
m_headers = initiate_table("A","E")
M = [
    [],
    [20],
    [60, 50],
    [100, 90, 40],
    [90, 80, 50, 30],
    ]

# this function is responsible for looking for the smallest cell in the whole table
def smallest_cell(M):

    minimum = 1000000000
    x, y =-1, -1

    # looking for the smallest cell in the table and if the minimum is found then it is assigned as the smallest cell
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] < minimum:
                minimum = M[i][j]
                x,y = i,j

    return x,y

# another function responsible for combining points of a group of points with the minimum distance between them
def combine_points(headers, m,n):
    if n < m:
        m, n =n, m
    headers[m] = "(" + headers[m] + "," + headers[n] +")"

    del headers[n]

# third function responsible for combining two entries of a given table and finding the average these entries.
def combine_table(M,m, n):
    if n <m:
        m,n =n,m

    r = []
    for i in range(0,m):
        r.append((M[m][i]+M[n][i])/2)
    M[m]=r
    for i in range(m+1,n):
        M[i][m]=(M[i][m] + M[n][i]) /2
    for i in range(n+1,len(M)):
        M[i][m] = (M[i][m] + M[i][n]) / 2
        del M[i][n]
    del M[n]

# another function responsible for UPGMA algorithm
def UPGMA(M, headers):
    while len(headers) > 1:
        x, y = smallest_cell(M)
        combine_table(M, x, y)
        combine_points(headers, x, y)
    return headers[0]

#main
tree = UPGMA(M,m_headers)
print(tree)
