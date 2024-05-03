class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
            - Valida se o número inteiro pode ser considerado um palíndromo.
            
            [Input]:
                x: Um número inteiro.

            [Output]:
                Um booleno TRUE para casos que sejam palíndromos ou FALSE caso não sejam.
        """

        return True if str(x) == str(x)[::-1] else False
