import subprocess
import constants

PIPELINE_NAME = constants.PIPELINE_NAME

# Create a TFX pipeline in local environment.
result = subprocess.run([
	"tfx", "pipeline", "create", 
	f"--engine=local",
	f"--pipeline_path={PIPELINE_NAME}/local_runner.py",
	], capture_output=True
)
print(result)