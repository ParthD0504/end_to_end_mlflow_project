import joblib
import numpy as np
import pandas as pd
from pathlib import Path


class PredictionPipeline:
    def __init__(self, model_path: Path | None = None):
        base_dir = Path(__file__).resolve().parents[3]
        self.model_path = model_path or base_dir / "artifacts" / "model_trainer" / "model.joblib"

        if not self.model_path.exists():
            raise FileNotFoundError(f"Model artifact not found at {self.model_path}")

        self.model = joblib.load(self.model_path)

    def predict(self, data: np.ndarray):
        return self.model.predict(data)

    
