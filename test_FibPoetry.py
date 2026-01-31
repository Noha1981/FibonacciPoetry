import FibPoetry as fib

def test_empty():
    assert fib.fibo_poem("") == ""

def test_two_words():
    assert fib.fibo_poem("Zwei Wörter") == "Zwei\nWörter"

def test_four_words():
    assert fib.fibo_poem("Dies ist ein Test") == "Dies\nist\nein Test"

def test_eleven_words():
    input_text = "Dies ist ein weiterer Test mit ganz genau elf Wörtern im Satz."
    expected_output = "Dies\nit\nein weiterer\nTest mit ganz\ngenau elf Wörtern im Satz."
    assert fib.fibo_poem(input_text) == expected_output
