# TFX Custom Components


* [Custom TFX Component: Pipeline creation](custom-tfx-component-pipeline.ipynb)
    - Create customized TFX component based on FileBasedExampleGen.
    - This component is used to directly import JPEG files.
    - Exported code in a .py file can be run with a Apache Beam Orchestrator.
    - Adapted from [Workshop - Developing TensorFlow Extended Components](https://colab.research.google.com/drive/1Z22WiON0NQwjJF-FCy_booVnRxx8-4Lh#scrollTo=fAlDXeya7f-a)


* [Custom TFX Component: Model deployment](custom-tfx-component-server.ipynb)
    - Workflow to deploy the model with a customized TFX component.
    - Uses TensorFlow Serving both via Docker and direct installation.