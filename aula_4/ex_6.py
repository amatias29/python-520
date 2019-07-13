
import os
import sys
import subprocess

current_module = os.path.abspath(os.path.curdir)
sys.path.append(current_module)

'''
for f in os.listdir(current_module):
	print(f)
'''

res = subprocess.run([ 'ls' ])
