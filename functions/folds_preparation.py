from settings.settings import Settings
from functions.folding_enum import FoldingEnum
from functions.folding_methods import FoldingMethods
from caddo_file_parser.models.fold import Fold


def get_folding_method():
    folding_method = Settings.folding_method
    match FoldingEnum[folding_method]:
        case FoldingEnum.KFOLD:
            return FoldingMethods.kfold_method
        case FoldingEnum.SKFOLD:
            return FoldingMethods.skfold_method


class FoldsPreparation:
    def __init__(self, settings_path=''):
        self.settings_path = settings_path

    def get_folds_dataset(self, x, y):
        folds = []
        folding_method = get_folding_method()
        for run in range(Settings.runs):
            fold = folding_method(self, 10, Settings.seeds, run)
            for train_index, val_index in fold.split(x, y):
                fold_data: Fold = Fold(run, train_index.tolist(), val_index.tolist(), Settings.seeds[run])
            folds.append(fold_data)
        return folds
