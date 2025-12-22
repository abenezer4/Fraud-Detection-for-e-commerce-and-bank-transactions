import pandas as pd
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataLoader:
    def __init__(self, data_dir='../data/raw'):
        """
        Initialize with the directory where raw data is stored.
        Default is set for running from the 'notebooks' folder.
        """
        self.data_dir = data_dir

    def load_csv(self, filename):
        """Helper to load a CSV and handle basic errors."""
        path = os.path.join(self.data_dir, filename)
        try:
            logging.info(f"Loading data from {path}...")
            df = pd.read_csv(path)
            logging.info(f"Successfully loaded {filename} with shape {df.shape}")
            return df
        except FileNotFoundError:
            logging.error(f"File not found: {path}. Check your directory path.")
            return None

   

