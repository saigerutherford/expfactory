#!/usr/bin/env python

import random
import string

choices = string.ascii_letters + string.digits + string.punctuation
selected = [random.SystemRandom().choice(choices) for _ in range(50)]
generated_key = ''.join(selected)
generated_key = generated_key.replace('"','a').replace("'",'B') # remove quotes
print(generated_key)
