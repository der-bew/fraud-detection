# fraud_detection/hooks.py
from kedro.framework.hooks import hook_impl
from kedro.pipeline import Pipeline
from fraud_detection.pipelines.data_processing import pipeline as de_pipeline

class ProjectHooks:
    @hook_impl
    def register_pipelines(self) -> dict:
        data_processing_pipeline = de_pipeline.create_pipeline()
        return {
            "de": data_processing_pipeline,
            "__default__": data_processing_pipeline,
        }
