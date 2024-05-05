# Operações em uma Árvore Binária de Busca
# Para que seja útil, a interface de programação de nossa árvore binária de busca deve fornecer algumas operações básicas, como: busca por chave, inserção de um elemento na árvore, remoção de um elemento e travessia

class BSTNode(object):
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    
    """def add(self, node):
        if node.value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.add(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.add(node)"""
                
    def add(self, key):
        """Adiciona elemento à subárvore
        """
        side = 'left' if key < self.key else 'right'
        node = getattr(self, side)
        if node is None:
            setattr(self, side, BSTNode(key))
        else:
            node.add(key)
            
    def remove(self, key):
        if key < self.key:
            self.left = self.left.remove(key)
        elif key > self.key:
            self.right = self.right.remove(key)
        else:
            # encontramos o elemento, então vamos removê-lo!
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            #ao invés de remover o nó, copiamos os valores do nó substituto
            tmp = self.right._min()
            self.key, self.value = tmp.key, tmp.value
            self.right._remove_min()
        return self
 
    def _min(self):
        """Retorna o menor elemento da subárvore que tem self como raiz.
        """
        if self.left is None:
            return self
        else:
            return self.left._min()
 
    def _remove_min(self):
        """Remove o menor elemento da subárvore que tem self como raiz.
        """
        if self.left is None:  # encontrou o min, daí pode rearranjar
            return self.right
        self.left = self.left._removeMin()
        return self
    
    """def get(self, key):
                if key < self.key:
                    return self.left.get(key) if self.left else None
                elif key > self.key:
                    return self.right.get(key) if self.right else None
                else:
                    return self"""
    
    def get(self, key):
        """Retorna uma referência ao nó de chave key"""
        if self.key == key:
            return self
        node = self.left if key < self.key else self.right
        if node is not None:
            return node.get(key)
            
    """As três principais estratégias de travessia de uma árvore são:

    pré-ordem
    ordem simétrica
    pós-ordem"""

    def traverse(self, visit, order='pre'):
        """Percorre a árvore na ordem fornecida como parâmetro (pre, pos ou in)
        visitando os nós com a função visit() recebida como parâmetro.
        """
        if order == 'pre':
            visit(self)
        if self.left is not None:
            self.left.traverse(visit, order)
        if order == 'in':
            visit(self)
        if self.right is not None:
            self.right.traverse(visit, order)
        if order == 'post':
            visit(self)
        
"""root = BSTNode(42)
root.left = BSTNode(10)
root.right = BSTNode(90)
root.left.left = BSTNode(2)"""

tree = BSTNode(8)
tree.left = BSTNode(5)
tree.right = BSTNode(4)
found = tree.get(4)
if found:
    print(found)
    
tree2 = BSTNode(0)
for i in range(1, 10):
    tree2.add(i)

# Perceba que o parâmetro visit representa uma função que será aplicada a cada elemento da árvore. Se quiséssemos imprimir a árvore em ordem simétrica, bastaria fazermos:
tree.traverse(print, 'in')

# travessia em profundidade x travessia em largura

"""Alternativas de Implementação
A estrutura de dados Árvore Binária de Busca pode também ser representada através de um simples array. A árvore do lado esquerdo da figura abaixo poderia ser representada pelo array ilustrado no lado direito da mesma figura. Observe que a raiz é representada na posição 0 do array. Para acessar o filho à esquerda de qualquer elemento, basta acessar a posição 2*i+1 do array, sendo i a posição do elemento em questão. Para acessar o filho à direita de um elemento, basta acessar a posição 2*i+2. Já o nó pai de um elemento i é encontrado na posição calculada através da divisão inteira (i-1)/2. Na figura acima, representamos os filhos à esquerda com uma seta verde e os filhos à direita com uma seta azul. A desvantagem dessa abordagem está no espaço necessário para representar árvores binárias incompletas, como a árvore da figura abaixo, em que é necessário representar os nós não existentes também. No exemplo abaixo, uma árvore de 5 elementos precisou de um array de tamanho 7 para representá-la."""
