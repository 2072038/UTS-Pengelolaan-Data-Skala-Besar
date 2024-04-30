def perkalian_matriks(matriks1, matriks2):
    hasil = [[0 for x in range(len(matriks2[0]))] for y in range(len(matriks1))]

    # perkalian matriks
    for i in range(len(matriks1)):
        for j in range(len(matriks2[0])):
            for k in range(len(matriks2)):
                hasil[i][j] += matriks1[i][k] * matriks2[k][j]
    return hasil

def main():
    # nilai matriks
    A = [[0, 1, 1/2, 0],
        [1/3, 0, 0, 1/2],
        [1/3, 0, 0, 1/2],
        [1/3, 0, 1/2, 0]]

    v = [[1/4],
        [1/4],
        [1/4],
        [1/4]]
        
    print("A:")
    for baris in A:
        print(baris)

    print("\nv:")
    for baris in v:
        print(baris)

    iterasi_pertama = perkalian_matriks(A, v)
    print("\nPerhitungan iterasi pertama:")
    for baris in iterasi_pertama:
        print(baris)

    iterasi_kedua = perkalian_matriks(A, iterasi_pertama)
    print("\nPerhitungan iterasi kedua:")
    for baris in iterasi_kedua:
        print(baris)

if __name__ == '__main__':
    main()
