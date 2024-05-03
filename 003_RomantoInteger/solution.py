class Solution:
    def romanToInt(self, s: str) -> int:
        """
            - Coleta a String de número Romano e converte para um valor inteiro.
            
            [Input]:
                s: Texto representativo do número romano.
            
            [Output]:
                Número romano convertido.
        """
        
        # Cria a base para a conversão dos números Romanos.
        base_num_roman = {'I':1,'V':5,'X':10,'L':50, 'C':100,'D':500,'M':1000}
        total = 0
        sucessor_value = 0

        for num in reversed(s):
            # Valida se o texto faz parte dos números Romanos.
            try:
                value = base_num_roman[num]
            except KeyError:
                return None
            
            # Realiza a soma ou subtração do valor conforme a sua posição ao número sucessor.
            if value >= sucessor_value:
                total += value
            else:
                total -= value
            
            sucessor_value = value
        
        return total
