# TFX Templates

Create a TFX pipeline via CLI + tfx template

## Step 1: Create templates

Edit `contants.py`

Run `python create_template.py`

## Step 2: Run pipeline

Edit `run_pipeline.py`

Run `python run_pipeline.py`

---

We also have the option of running the orchestrator directly via Python, as in

`python ./projectname/local_runner.py`

However, we may lose some functionality here, such as registering the pipeline, output options, etc.