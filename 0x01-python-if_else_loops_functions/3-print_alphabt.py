#!/usr/bin/python3

print("".join(chr(97 + i) for i in range(26) if chr(97 + i) not in ('q', 'e')), end="")
