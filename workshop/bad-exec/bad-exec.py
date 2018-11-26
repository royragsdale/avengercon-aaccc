#!/usr/bin/env python3

import subprocess

command = input("Input a command to run: ")

if command.split()[0] == "cat":
	if "flag" in command:
		print("Silly hacker, flags are for kids!")
		exit(0)

print(subprocess.check_output(["bash", "-c", command]).decode("utf-8"))
