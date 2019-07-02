from string import ascii_uppercase, ascii_lowercase, digits, punctuation
import random

def scramble(max = 16, chars = ascii_uppercase + ascii_lowercase + digits + punctuation):
	return ''.join(random.SystemRandom().choice(chars) for _ in range(max))
print(scramble())
