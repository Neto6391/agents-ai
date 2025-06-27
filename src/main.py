from config.settings import Settings
import logging

def main():
    settings = Settings()
    logging.basicConfig(level=logging.INFO)
    logging.info(f"App iniciando com modelo em {settings.onnx_model_path}")
    # TODO: FEATURES HERE TO BE IMPLEMENTED
    
if __name__ == "__main__":
    main()
