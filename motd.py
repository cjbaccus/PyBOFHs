#!/usr/bin/env python

import random

with open("BOFH.txt", "r") as f:
	content = f.readlines()

content = [x.strip() for x in content]

print(random.choice(content))

