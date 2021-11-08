def triangle_pascal(n):
    if n == 0:
        return [0,0,0,0]

    pascal = [[1,0,0,0]]

    for i in range(1,n):
        line = [1]
        for j in range(len(pascal)):
            if j+1 < len(pascal):
                line.append(pascal[i-1][j] + pascal[i-1][j+1])
        line.append(1)
        while len(line)<4 : line.append(0) #this is not necessary but it adds the 0 to the first 4 lines.
        pascal.append(line)

    return pascal
