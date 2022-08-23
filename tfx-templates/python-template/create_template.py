import os
import shlex
import subprocess
import tfx
import pprint
pp = pprint.PrettyPrinter(indent=4)

import constants

def HR():
	print("-"*40)

# Step 1: Basic setup
print(f"TFX: {tfx.__version__}")
HR()

PIPELINE_NAME = constants.PIPELINE_NAME

# Step 2: Copy predefined template to project directory
print(f"PIPELINE_NAME: {PIPELINE_NAME}")
HR()

# Create project dir under current working directory
PROJECT_DIR = constants.PROJECT_DIR

print(f"PROJECT_DIR: {PROJECT_DIR}")
HR()

os.makedirs(PROJECT_DIR, exist_ok=True)


cmd_copy = f"""
tfx template copy 
--pipeline-name={PIPELINE_NAME}
--destination-path={PROJECT_DIR}
--model=penguin"""

print("Command to copy template:")
print(cmd_copy)
HR()

# Copy template files.
result = subprocess.run(shlex.split(cmd_copy), capture_output=False)

print("Result of copying the template:")
pp.pprint(result)