class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        """
        Convierte temperatura de Celsius a Fahrenheit.
        
        Args:
            celsius (float): Temperatura en grados Celsius
            
        Returns:
            float: Temperatura en grados Fahrenheit
            
        Fórmula: F = (C × 9/5) + 32
        
        Ejemplo:
            celsius_a_fahrenheit(0) -> 32.0
            celsius_a_fahrenheit(100) -> 212.0
        """
        return (celsius * 9 / 5) + 32
        pass
    
    def fahrenheit_a_celsius(self, fahrenheit):
        """
        Convierte temperatura de Fahrenheit a Celsius.
        
        Args:
            fahrenheit (float): Temperatura en grados Fahrenheit
            
        Returns:
            float: Temperatura en grados Celsius
            
        Fórmula: C = (F - 32) × 5/9
        
        Ejemplo:
            fahrenheit_a_celsius(32) -> 0.0
            fahrenheit_a_celsius(212) -> 100.0
        """
        return (fahrenheit - 32) * 5 / 9
        pass
    
    def metros_a_pies(self, metros):
        """
        Convierte distancia de metros a pies.
        
        Args:
            metros (float): Distancia en metros
            
        Returns:
            float: Distancia en pies
            
        Factor: 1 metro = 3.28084 pies
        
        Ejemplo:
            metros_a_pies(1) -> 3.28084
        """
        return metros * 3.28084
        pass
    
    def pies_a_metros(self, pies):
        """
        Convierte distancia de pies a metros.
        
        Args:
            pies (float): Distancia en pies
            
        Returns:
            float: Distancia en metros
            
        Factor: 1 pie = 0.3048 metros
        
        Ejemplo:
            pies_a_metros(3.28084) -> 1.0
        """
        return pies * 0.3048
        pass
    
    def decimal_a_binario(self, decimal):
        """
        Convierte un número decimal a su representación binaria.
        
        Args:
            decimal (int): Número decimal (positivo)
            
        Returns:
            str: Representación binaria como string
            
        Ejemplo:
            decimal_a_binario(10) -> "1010"
            decimal_a_binario(255) -> "11111111"
        """
        if decimal < 0:
            raise ValueError("El número debe ser positivo")

        return bin(decimal)[2:]
        pass
    
    def binario_a_decimal(self, binario):
        """
        Convierte un número binario a decimal.
        
        Args:
            binario (str): Representación binaria como string
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            binario_a_decimal("1010") -> 10
            binario_a_decimal("11111111") -> 255
        """
        if not binario:
            raise ValueError("El número binario no puede estar vacío")

        if any(digito not in "01" for digito in binario):
            raise ValueError("El número contiene caracteres que no son binarios")

        return int(binario, 2)
        pass
    
    def decimal_a_romano(self, numero):
        """
        Convierte un número decimal a numeración romana.
        
        Args:
            numero (int): Número decimal entre 1 y 3999
            
        Returns:
            str: Número romano
            
        Ejemplo:
            decimal_a_romano(9) -> "IX"
            decimal_a_romano(1994) -> "MCMXCIV"
        """
        if numero < 1 or numero > 3999:
            raise ValueError("El número debe estar entre 1 y 3999")

        valores = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        romano = ""

        for valor, simbolo in valores:
            while numero >= valor:
                romano += simbolo
                numero -= valor

        return romano
        pass
    
    def romano_a_decimal(self, romano):
        """
        Convierte un número romano a decimal.
        
        Args:
            romano (str): Número romano válido
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            romano_a_decimal("IX") -> 9
            romano_a_decimal("MCMXCIV") -> 1994
        """
        if not romano:
            raise ValueError("El número romano no puede estar vacío")

        valores = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        romano = romano.upper()
        total = 0

        for i in range(len(romano)):
            if romano[i] not in valores:
                raise ValueError("Número romano inválido")

            if i + 1 < len(romano) and valores[romano[i]] < valores[romano[i + 1]]:
                total -= valores[romano[i]]
            else:
                total += valores[romano[i]]

        return total
        pass
    
    def texto_a_morse(self, texto):
        """
        Convierte texto a código Morse.
        
        Args:
            texto (str): Texto a convertir (letras y números)
            
        Returns:
            str: Código Morse separado por espacios
            
        Ejemplo:
            texto_a_morse("SOS") -> "... --- ..."
            texto_a_morse("HELLO") -> ".... . .-.. .-.. ---"
        """
        morse = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "0": "-----",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----."
        }

        resultado = []

        for caracter in texto.upper():
            if caracter == " ":
                resultado.append("/")
            elif caracter in morse:
                resultado.append(morse[caracter])
            else:
                raise ValueError(
                    f"Caracter no soportado: {caracter}"
                )

        return " ".join(resultado)

        pass
    
    def morse_a_texto(self, morse):
        """
        Convierte código Morse a texto.
        
        Args:
            morse (str): Código Morse separado por espacios
            
        Returns:
            str: Texto decodificado
            
        Ejemplo:
            morse_a_texto("... --- ...") -> "SOS"
            morse_a_texto(".... . .-.. .-.. ---") -> "HELLO"
        """
        codigo_morse = {
            ".-": "A",
            "-...": "B",
            "-.-.": "C",
            "-..": "D",
            ".": "E",
            "..-.": "F",
            "--.": "G",
            "....": "H",
            "..": "I",
            ".---": "J",
            "-.-": "K",
            ".-..": "L",
            "--": "M",
            "-.": "N",
            "---": "O",
            ".--.": "P",
            "--.-": "Q",
            ".-.": "R",
            "...": "S",
            "-": "T",
            "..-": "U",
            "...-": "V",
            ".--": "W",
            "-..-": "X",
            "-.--": "Y",
            "--..": "Z",
            "-----": "0",
            ".----": "1",
            "..---": "2",
            "...--": "3",
            "....-": "4",
            ".....": "5",
            "-....": "6",
            "--...": "7",
            "---..": "8",
            "----.": "9"
        }

        resultado = []

        for codigo in morse.split():
            if codigo == "/":
                resultado.append(" ")
            elif codigo in codigo_morse:
                resultado.append(codigo_morse[codigo])
            else:
                raise ValueError(
                    f"Código Morse inválido: {codigo}"
                )

        return "".join(resultado)
        pass