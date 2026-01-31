"""
Fibonacci-Poesie-Modul
Datum: 2026-01-31
Author: Norman Fober
Angelehnt an den FB Post von Brian Bilston
Dieses Modul wird über fibo_poem(text: str) aufgerufen, welches den übergebenen Text in Zeilen
aufteilt, wobei die Anzahl der Wörter in jeder Zeile den Fibonacci-Zahlen folgt.
Falls am Ende nicht genügend Wörter übrig sind, werden die Zeilen mit '.' aufgefüllt
"""

from typing import List

# Hauptfunktion, welche den Text in Fibonacci-Poesie umwandelt
# Basierend auf der Liste der Fibonacci-Zahlen wird der Text in Zeilen aufgeteilt
def fibo_poem(text: str) -> str:
    """Teilt `text` in Zeilen, wobei die Wortanzahlen den Fibonacci-Größen folgen.
    Die letzte Gruppe wird mit '_' aufgefüllt, falls zu wenige Wörter übrig sind."""
    words = text.split()
    if not words:
        return ""
    groups = fib_it(len(words))
    lines = []
    idx = 0
    for g in groups:
        segment = words[idx: idx + g]
        if len(segment) < g:
            segment = segment + ["."] * (g - len(segment))
        lines.append(" ".join(segment))
        idx += g
        if idx >= len(words):
            break
    return "\n".join(lines)

# Hilfsfunktion zur Generierung der Fibonacci-Zahlen
def fib_it(n: int) -> List[int]:
    """Gibt eine Liste von Fibonacci-Größen zurück, so dass ihre kumulierte Summe >= n."""
    if n <= 0:
        return []
    if n == 1:
        return [1]
    seq = [1, 1]
    cum = 2
    while cum < n:
        nxt = seq[-1] + seq[-2]
        seq.append(nxt)
        cum += nxt
    return seq

