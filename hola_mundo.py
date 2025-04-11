#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def saludar(nombre):
    """
    Función simple que devuelve un saludo personalizado
    
    Args:
        nombre (str): Nombre de la persona a saludar
        
    Returns:
        str: Mensaje de saludo
    """
    return f"¡Hola {nombre}! Bienvenido a tu repositorio de prueba."

def calcular_suma(a, b):
    """
    Función que suma dos números
    
    Args:
        a (int/float): Primer número
        b (int/float): Segundo número
        
    Returns:
        int/float: Resultado de la suma
    """
    return a + b

if __name__ == "__main__":
    # Ejemplo de uso de las funciones
    print(saludar("Usuario"))
    
    # Ejemplo de suma
    num1 = 5
    num2 = 7
    resultado = calcular_suma(num1, num2)
    print(f"La suma de {num1} y {num2} es: {resultado}")
    
    # Solicitar datos al usuario
    nombre_usuario = input("Por favor, introduce tu nombre: ")
    print(saludar(nombre_usuario))
    
    try:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))
        print(f"La suma de {numero1} y {numero2} es: {calcular_suma(numero1, numero2)}")
    except ValueError:
        print("Error: Debes introducir números válidos.")