def issafe(mat, r, c):
    for i in range(r):
        if mat[i][c] == 'Q':
            return False


    (i,j)=(r,c)
    while (i>=0 and j>=0):
        if mat[i][j] == 'Q':
            return False
        i = i-1
        j = j-1

    (i,j) = (r,c)
    while(i>=0 and j< len(mat)):
        if mat[i][j] == 'Q':
            return False
        i =i-1
        j=j+1

    return True


def printsolution(mat):
    for r in mat:
        print(str(r).replace(',', ' ').replace('\'',' '))
    print()


def Nqueen(mat, r):
    if r == len(mat):
        printsolution(mat)
        return

    for i in range(len(mat)):
        if issafe(mat,r,i):
            mat[r][i]='Q'

            Nqueen(mat, r+1)

            mat[r][i] = '-'


if __name__ == '__main__' :
    N = 8

    mat = [['-' for x in range(N)] for y in range(N)]

    Nqueen(mat, 0)
