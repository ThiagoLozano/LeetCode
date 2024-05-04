class Solution(object):
    def isValid(self, s):
        '''
            - Valida se as chaves são abertas e fechadas de forma correta.
            
            [Input]:
                s: Uma string

            [Output]:
                Retorna True se as chaves estiverem corretas ou False caso elas nã estejam.
        '''
        
        # Separa as chaves de fechamento e abertura.
        chaves = {')': '(', '}': '{', ']': '['}
        pilha  = []
        
        # Passa por cada caracter e valida se para cada chave aberta existe uma fechada corretamente.
        '''
            Ex:
                string = "()"
                pilha  = []
                
                caracter = '('   -> É uma chave de abertura, adicione na pilha  ->  pilha = ['(']
                caracter = ')'   -> É uma chave de fechamento, valida se é uma chave valida e está na pilha -> pilha = []
        '''
        for character in s:
            if character in chaves:
                elemento_topo = pilha.pop() if pilha else '#' # Retorna o último elemento da pilha caso não seja vazia.
                
                if chaves[character] != elemento_topo:
                    return False
            else:
                pilha.append(character)

        return not pilha
