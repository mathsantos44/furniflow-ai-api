from joblib import load

from src.settings import get_settings

_settings = get_settings()


class TrainedModelService:
    def __init__(self, model_path: str = _settings.trained_model_path):
        self.model = load(model_path)

    def predict(self, data: str) -> str:
        return self.model.predict([data])[0]


if __name__ == '__main__':
    model_service = TrainedModelService()
    prediction = model_service.predict('TV')
    print(prediction)
