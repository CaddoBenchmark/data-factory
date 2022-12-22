import pandas as pd
from functions.functions_loader import FunctionsLoader
from settings.settings_loader import SettingsLoader
from settings.settings import Settings
from functions.folds_preparation import FoldsPreparation

def open_dataset_file(path, sep):
    dataset = pd.read_csv(path, sep=sep)
    return dataset


def save_to_caddo(dataset):
    output_name = Settings.extraction_data_module
    compression_opts = dict(method='zip',
                            archive_name=output_name + '.csv')
    pd.DataFrame(dataset).to_csv(output_name + ".caddo",
                                 sep=Settings.output_separator,
                                 index=False,
                                 compression=compression_opts)


class DataFactory:
    def __init__(self):
        print("INIT")
        SettingsLoader('./settings.yaml').load()
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
        extracted_data = self.extraction_module.extract(dataset_df)
        save_to_caddo(extracted_data)

        FoldsPreparation.evaluate_loop(None, None, None)


if __name__ == '__main__':
    DataFactory()
