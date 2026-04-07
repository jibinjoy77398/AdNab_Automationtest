import json
import os

class ConfigReader:
    """Utility class to read configuration from config.json."""

    @staticmethod
    def get_config():
        """
        Reads the config.json file and returns its content as a dictionary.
        """
        # Get the path to the config.json at the project root
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        config_path = os.path.join(project_root, 'config.json')
        
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found at {config_path}")
            
        with open(config_path, 'r') as config_file:
            return json.load(config_file)
