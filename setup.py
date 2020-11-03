from setuptools import setup


setup(
    name="papermill-mlflow-handler",
    description="MLFlow handler for papermill.",
    version="1.0.0",
    license=["MIT"],
    packages=["papermill_mlflow_handler"],
    python_requires=">=3.6",
    install_requires=[
        "papermill",
        "mlflow",
        "google-cloud-storage"
    ],
    entry_points={"papermill.io": ["mlflow://=papermill_mlflow_handler:MLFlowHandler"]},
)