import pandas as pd

from functions.functions_loader import FunctionsLoader
from settings.settings_loader import SettingsLoader
from settings.settings import Settings
from functions.folds_preparation import FoldsPreparation
from caddo_file_parser.caddo_file_parser import CaddoFileParser
from caddo_file_parser.models.caddo_file import CaddoFile


def open_dataset_file(path, sep):
    dataset = pd.read_csv(path, sep=sep)
    return dataset


class DataFactory:
    def __init__(self):
        print("INIT")
        SettingsLoader('./settings.yaml').load()
        self.folds_preparation = FoldsPreparation()
        self.extraction_module = None
        self.load_modules()
        self.run()

    def load_modules(self):
        print("LOADING DATA EXTRACTION FUNCTION:")
        functions_loader = FunctionsLoader()
        self.extraction_module = functions_loader.extract_features_keywords()
        print()

    def run(self):
        print("READ DATA FROM FILE")
        dataset_df = open_dataset_file(Settings.data_source_path, Settings.data_source_separator)

        print("EXTRACT DATA")
        pre_processed_data = self.extraction_module.extract(dataset_df)

        X = dataset_df[Settings.data_source_x_cols]
        y = dataset_df[Settings.data_source_y_cols]
        pre_processed_data['Y'] = dataset_df[Settings.data_source_y_cols]

        print("PREPARE FOLDS")
        folds = self.folds_preparation.get_folds_dataset(X, y)

        print("SAVE TO .CADDO FILE")
        caddoFile = CaddoFile(folds, pre_processed_data)
        caddoFileParser = CaddoFileParser()
        caddoFileParser.create_file(caddoFile, "results_from_parser")

        caddoFileParser.read_data("results_from_parser")


if __name__ == '__main__':
    DataFactory()
