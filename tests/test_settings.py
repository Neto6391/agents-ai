import pytest
from pydantic import ValidationError
from config.settings import Settings

def test_defaults_load():
    s = Settings(_env_file=None)
    assert s.onnx_model_path == "./models/gemma.onnx"
    assert s.intent_confidence_threshold == 0.3

def test_invalid_type(tmp_path):
    env = tmp_path / ".env"
    env.write_text("INTENT_CONFIDENCE_THRESHOLD=not_a_number\n")
    with pytest.raises(ValidationError):
        Settings(_env_file=str(env))
