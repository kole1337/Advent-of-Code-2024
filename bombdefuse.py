class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        sum = 0
        xs = code.copy()
        n = len(code)

        if k < 0:
            k = k*-1
            for i in range(n):
                print(f'i:{i}')
                for j in range(k):
                    sum = sum + xs[(i - j + n - 1) % n]
                    # print(f'{(i - j + n - 1) % n}')
                code[i] = sum
                sum=0
            print(f'{k} is less than 0')
        elif k > 0:
            for i in range(n):
                # print(f'i:{i}')
                for j in range(k):
                    # print(j)
                    sum = sum + xs[(i + j+1) % n]
                    # print(f'{(i + j+1) % n}')
                # print(f'sum:{sum}')
                # print(f'list:{code[i]}')
                code[i] = sum
                sum = 0

            # print(f'{k} is greater than 0')
        elif k == 0:
            for i in range(len(code)):
                code[i] = 0

        return code


test = Solution()
print(test.decrypt([2,4,9,3], -2))
