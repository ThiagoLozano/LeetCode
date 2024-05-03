class Solution(object):
    def longestCommonPrefix(self, strs:list) -> str:
        """
            - Localiza o LCP(Longest Common Prefix) de uma lista de Strings.

            [Input]:
                strs: Lista de strings.

            [Output]:
                Caracteres que se repetem entre as strings da lista.
        """

        # Valida se contêm algum elemento vazio na lista.
        if "" in strs:
            return ""
        
        len_first_element = len(strs[0]) # Identifica a quantidade de iterações necessárias.
        
        # Valida se há retorno True em todas as iterações, se sim, ele para no primeiro prefixo comum localizado.
        '''
            lista -> ["flower","flow","flight"]

            EX: flower -> lista[True, False, False]
                flowe  -> lista[True, False, False]
                flow   -> lista[True, False, False]
                flo    -> lista[True, True, False]
                fl     -> lista[True, True, True]
        '''
        for index in range(len_first_element, 0, -1):
            prefix = strs[0][:index]
            status_prefix  = [True if elemento.startswith(prefix) else False for elemento in strs]

            if all(status_prefix):
                break
        
        return "" if False in status_prefix else prefix
