# python3

def parallel_processing(n, m, data):
    output = []

    for i in range(n):
        output.append((i,0))
    
    for i in range(n, m):
        sec = output[i-n][1] + int(data[i-n])
        output.append((i - (i//n)* n, sec))

    return output

def main():
    first_line = input().split()
    n = int(first_line[0])
    m = first_line[1]
    m = int(m.strip())

    sec_line = input().split()
    data = []
    data = sec_line

    result = parallel_processing(n,m,data)
    
    for i, j in result:
        print(i, j)


if __name__ == "__main__":
    main()
