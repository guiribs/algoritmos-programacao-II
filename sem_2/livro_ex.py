#Ex. 8.1

class Point:
    'classe que representa pontos no plano'
    def setx(self, coordx):
        'define coordenada x do ponto como coordx'
        self.x = coordx
    
    def sety(self, coordy):
        'define coordenada y do ponto como coordy'
        self.y = coordy
    
    def get(self):
        'retorna tupla com coordenadas x e y do ponto'
        return (self.x, self.y)

    def move(self, dx, dy):
        'muda as coordenadas x e y por dx e dy'
        self.x += dx
        self.y += dy
        
    def getx(self):
        'retorna somente a coordenada x'
        return (self.x)
    
p = Point()
p.setx(4)
p.sety(7)

print(p.get())
print(p.getx())

#Ex. 8.9

class Queue2(list):
    """Uma classe de fila, subclasse de list."""

    def isEmpty(self):
        """Retorna True se a fila estiver vazia, False caso contrário."""
        return len(self) == 0

    def dequeue(self):
        """Remove e retorna o item na frente da fila."""
        return self.pop(0)

    def enqueue(self, item):
        """Insere o item no final da fila."""
        self.append(item)
