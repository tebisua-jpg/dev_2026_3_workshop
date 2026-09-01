class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """
        if n <=0:
            return 0
        elif n==1:
            return 1
        else: 
            return self.fibonacci(n-1)+ self.fibonacci(n-2)
        pass
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        sec_fib=[0,1]
        for i in range(2,n):
            sec_fib.append(sec_fib[-1]+ sec_fib[-2])
        
        return sec_fib[:n]
        pass
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        if n <2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i==0:
                return False
        return True
        pass
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
        primos=[]
        for j in range(2,n+1):
            if self.es_primo(j):
                primos.append(j)
        return primos
        pass
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        if n<2:
            return False
        suma_divisores=sum(i for i in range(1,n) if n%i==0)
        return suma_divisores==n
        pass
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        triangulo = [[1]]
        for _ in range(1, filas):
            fila_anterior = triangulo[-1]
            nueva_fila = [1] + [fila_anterior[i] + fila_anterior[i + 1] for i in range(len(fila_anterior) - 1)] + [1]
            triangulo.append(nueva_fila)
        return triangulo
        pass
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        if n==0 or n==1:
            return 1
        else: 
            return n *self.factorial(n-1)
        pass
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        import math
        return math.gcd(a,b)
        pass
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        return abs(a*b)// self.mcd(a,b) if a and b else 0
        pass
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        return sum(int(dig1)for dig1 in str(abs(n)))
        pass
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        if n < 0:
         return False

        num_str = str(n)
        suma = sum(int(digito) ** len(num_str) for digito in num_str)

        return suma == n
        
        
        pass
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        if not matriz or not all(len(fila) == len(matriz) for fila in matriz):
            return False

        n = len(matriz)
        suma_magica = sum(matriz[0])

        for i in range(n):
            if sum(matriz[i]) != suma_magica or sum(matriz[j][i] for j in range(n)) != suma_magica:
                return False

        if sum(matriz[i][i] for i in range(n)) != suma_magica or sum(matriz[i][n - i - 1] for i in range(n)) != suma_magica:
            return False

        return True
        pass