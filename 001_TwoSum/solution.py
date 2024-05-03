class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
            - Localiza dois números da lista onde o resulta de sua soma seja o valor de Target.

            [Input]:
                nums: Uma lista de números inteiros. 
                target: O valor da soma a ser localizado.
            
            [Output]:
                Uma lista contendo os índices de dois números, onde a soma entre eles resulta no valor Target ou
                None caso nenhum índice seja localizado. 
        """
        
        # Armazena os números da lista e seus índices correspondentes.
        dict_index = {}
        
        # Passa por cada valor da lista e identifica se o resto da subtração foi localizado no dicionário. 
        for index, num in enumerate(nums):
            remainder = target - num

            if remainder in dict_index:
                return [dict_index[remainder], index]
            
            dict_index[num] = index
