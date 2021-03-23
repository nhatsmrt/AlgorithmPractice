class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Time and Space Complexity: O(N log N)
        coeff1 = list(reversed(list(map(complex, iter(num1)))))
        coeff2 = list(reversed(list(map(complex, iter(num2)))))
        prod_deg = len(coeff1) + len(coeff2) - 2

        padded_len = 2 ** math.ceil(math.log2(prod_deg + 1))

        coeff1 += [complex(0)] * (padded_len - len(coeff1))
        coeff2 += [complex(0)] * (padded_len - len(coeff2))

        fft1 = self.fft(coeff1)
        fft2 = self.fft(coeff2)



        fft_prod = [val1 * val2 for val1, val2 in zip(fft1, fft2)]
        coeff_prod = [round(coeff.real) for coeff in self.ifft(fft_prod)]

        ret = 0
        power = 1

        carry = 0
        for i in range(len(coeff_prod)):
            coeff_prod[i] += carry
            carry = coeff_prod[i] // 10
            coeff_prod[i] = str(coeff_prod[i] % 10)

        while carry > 0:
            coeff_prod.append(str(carry % 10))
            carry //= 10

        ret = "".join(reversed(coeff_prod)).lstrip("0")
        if len(ret) == 0:
            return "0"

        return ret


    def fft(self, coeff):
        return self.transform(coeff)

    def ifft(self, vals):
        return ([coeff / len(vals) for coeff in self.transform(vals, True)])


    def transform(self, arr, inversed: bool=False):
        n = len(arr)

        if n == 1:
            return arr

        even = [arr[i] for i in range(0, len(arr), 2)]
        odd = [arr[i] for i in range(1, len(arr), 2)]

        if inversed:
            angle = -2 * math.pi / len(arr)
        else:
            angle = 2 * math.pi / len(arr)
        root = complex(cos(angle), sin(angle))

        y_even = self.transform(even, inversed)
        y_odd = self.transform(odd, inversed)
        cur_factor = 1

        ret = [0] * n
        for i in range(n // 2):
            ret[i] = y_even[i] + cur_factor * y_odd[i]
            ret[i + n // 2] = y_even[i] - cur_factor * y_odd[i]
            cur_factor *= root

        return ret
