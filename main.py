from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional
import tkinter as tk
from tkinter import scrolledtext


# ------------------------------
# Definiciones básicas
# ------------------------------
class TokenType(Enum):
    KEYWORD = auto()
    IDENTIFIER = auto()
    NUMBER = auto()
    OPERATOR = auto()
    SEMICOLON = auto()


@dataclass
class Token:
    tipo: TokenType
    lexema: str
    literal: Optional[str]
    linea: int
    columna: int


# ------------------------------
# Etapas del compilador
# ------------------------------
def analisis_lexico(codigo: str) -> List[Token]:
    tokens: List[Token] = []
    palabras_clave = {"let", "if", "else", "while"}
    operadores = {"+", "-", "*", "/", "="}
    linea, col = 1, 1

    for palabra in codigo.replace(";", " ; ").split():
        if palabra in palabras_clave:
            tokens.append(Token(TokenType.KEYWORD, palabra, None, linea, col))
        elif palabra.isidentifier():
            tokens.append(Token(TokenType.IDENTIFIER, palabra, None, linea, col))
        elif palabra.isdigit():
            tokens.append(Token(TokenType.NUMBER, palabra, int(palabra), linea, col))
        elif palabra in operadores:
            tokens.append(Token(TokenType.OPERATOR, palabra, None, linea, col))
        elif palabra == ";":
            tokens.append(Token(TokenType.SEMICOLON, palabra, None, linea, col))
        col += len(palabra) + 1
    return tokens


def analisis_sintactico(tokens: List[Token]) -> str:
    return "Árbol de sintaxis abstracta generado (AST simulado)."


def analisis_semantico(tokens: List[Token]) -> str:
    ids = [t.lexema for t in tokens if t.tipo == TokenType.IDENTIFIER]
    if not ids:
        return "Error semántico: no se encontraron variables."
    return "Análisis semántico exitoso."


def generar_codigo_intermedio(tokens: List[Token]) -> str:
    return "Código intermedio: [LOAD, ADD, MULT, STORE]"


def optimizar_codigo() -> str:
    return "Optimización aplicada: eliminación de instrucciones redundantes."


def generar_codigo_objetivo() -> str:
    return "Código objetivo generado para x86."


def linker() -> str:
    return "Linker: se unieron módulos y librerías en un ejecutable."


# ------------------------------
# Interfaz gráfica Tkinter
# ------------------------------
def compilar():
    codigo = entrada.get("1.0", tk.END).strip()
    salida.delete("1.0", tk.END)

    # Etapas
    tokens = analisis_lexico(codigo)
    salida.insert(tk.END, "=== Análisis Léxico ===\n")
    for t in tokens:
        salida.insert(tk.END, f"{t.tipo.name}: '{t.lexema}' literal={t.literal}\n")

    salida.insert(tk.END, "\n=== Análisis Sintáctico ===\n")
    salida.insert(tk.END, analisis_sintactico(tokens) + "\n")

    salida.insert(tk.END, "\n=== Análisis Semántico ===\n")
    salida.insert(tk.END, analisis_semantico(tokens) + "\n")

    salida.insert(tk.END, "\n=== Generación de Código Intermedio ===\n")
    salida.insert(tk.END, generar_codigo_intermedio(tokens) + "\n")

    salida.insert(tk.END, "\n=== Optimización ===\n")
    salida.insert(tk.END, optimizar_codigo() + "\n")

    salida.insert(tk.END, "\n=== Código Objetivo ===\n")
    salida.insert(tk.END, generar_codigo_objetivo() + "\n")

    salida.insert(tk.END, "\n=== Linker ===\n")
    salida.insert(tk.END, linker() + "\n")


# Ventana principal
ventana = tk.Tk()
ventana.title("Mini Compilador - Demo")
ventana.geometry("600x600")

tk.Label(ventana, text="Código Fuente:").pack()
entrada = scrolledtext.ScrolledText(ventana, height=8, width=70)
entrada.pack()

btn = tk.Button(ventana, text="Compilar", command=compilar, bg="lightblue")
btn.pack(pady=10)

tk.Label(ventana, text="Salida del Compilador:").pack()
salida = scrolledtext.ScrolledText(ventana, height=20, width=70, bg="black", fg="white")
salida.pack()

ventana.mainloop()


#probando#