import sys

from settings.settings import Settings


class FunctionsLoader:
    def extract_features_keywords(self):
        module = self.load_module(Settings.extraction_data_module)
        print("Data Loader loaded!")
        return module

    def load_module(self, path_to_module):
        __import__(path_to_module)
        return sys.modules[path_to_module]
