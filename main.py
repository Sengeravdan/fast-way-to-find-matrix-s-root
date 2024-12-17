class Matrix:
    def __init__(self, n, m, rows):
        self.n = n
        self.m = m
        self.rows = rows

    def __str__(self):
        return '\n'.join(' '.join(str(val) for val in row) for row in self.rows)

    def __mul__(self, other):
        if self.m != other.n:
            raise Exception("Matrix multiplication error: dimension mismatch.")
        result = [
            [
                sum(self.rows[i][k] * other.rows[k][j] for k in range(self.m))
                for j in range(other.m)
            ]
            for i in range(self.n)
        ]
        return Matrix(self.n, other.m, result)

    @staticmethod
    def identity(n):
        return Matrix(n, n, [[1 if i == j else 0 for j in range(n)] for i in range(n)])

    def power_binary(self, k):
        if self.n != self.m:
            raise Exception("Matrix must be square.")
        result = Matrix.identity(self.n)
        base = self
        while k > 0:
            if k % 2 == 1:
                result = result * base
            base = base * base
            k //= 2
        return result

    def power_naive(self, k):
        if self.n != self.m:
            raise Exception("Matrix must be square.")
        result = Matrix.identity(self.n)
        for _ in range(k):
            result = result * self
        return result


if __name__ == "__main__":
    N, M = map(int, input("행렬의 행과 열의 개수를 입력하세요 (공백 구분): ").split())
    if N != M:
        raise Exception("정사각행렬만 거듭제곱이 가능합니다.")

    K = int(input("거듭제곱할 지수를 입력하세요: "))
    A_data = []

    for i in range(N):
        row = list(map(int, input(f"{i+1}행 입력 (공백 구분): ").split()))
        if len(row) != M:
            raise Exception("행렬의 열 수가 올바르지 않습니다.")
        A_data.append(row)

    A = Matrix(N, M, A_data)

    A_pow_bin = A.power_binary(K)
    print(f"\nA^{K} (Binary Exponentiation):")
    print(A_pow_bin)

    A_pow_naive = A.power_naive(K)
    print(f"\nA^{K} (Naive Multiplication):")
    print(A_pow_naive)

    print("\nDifference:")
    diff = [[A_pow_bin.rows[i][j] - A_pow_naive.rows[i][j] for j in range(M)] for i in range(N)]
    for row in diff:
        print(' '.join(map(str, row)))