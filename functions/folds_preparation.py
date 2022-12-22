from collections import Counter
from settings.settings import Settings
from functions.folding_enum import FoldingEnum
from functions.folding_methods import FoldingMethods

class FoldsPreparation:

    def __init__(self, settings_path=''):
        self.settings_path = settings_path

    def choose_folding_method_from_settings(self):
        folding_method: FoldingEnum = Settings.folding_method
        folds = []
        match FoldingEnum[folding_method]:
            case FoldingEnum.KFOLD:
                FoldingMethods.skfold_method(self, 10, Settings.seeds, run)
            case FoldingEnum.SKFOLD:
                FoldingMethods.skfold_method(self, 10, Settings.seeds, run)




    def evaluate_loop(self, X, y, runs=10):
        # counter_y = Counter(y)
        # results = dict(acc=[], rec=[], prec=[], fscore=[], cnf=[],
        #                n=X.shape[0],
        #                n_pos=counter_y[1], n_neg=counter_y[0])

        for run in range(runs):
            skfold = FoldingMethods.skfold_method(self, 10, Settings.seeds, run)
            print(skfold)
            # seeds - nie moga przepasc (muszą byc zapisane gdzies)
            # czy reużywam raz wygenerowanych seedów, czy też za kazdym razem na nowo generowac
            # skfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seeds[run])
            # kfold = KFold(n_splits=10, shuffle=True, random_state=seeds[run])
            # print(f'Run {run + 1} / {runs}')
            # cv_preds = []
            # cv_trues = []
            # print('- Fold: ', end=" ")
            # fold = 1
            # for train_index, val_index in skfold.split(X, y):
            #     print(f'{fold}', end=' ')
            #     y_pred = evaluate_model_func(X.iloc[train_index], y.iloc[train_index], X.iloc[val_index])
            #
            #     cv_preds += y_pred.tolist()
            #     cv_trues += y.iloc[val_index].tolist()
            #     fold += 1
            # print("")
            # results['acc'].append(accuracy_score(cv_trues, cv_preds))
            # results['rec'].append(recall_score(cv_trues, cv_preds))
            # results['prec'].append(precision_score(cv_trues, cv_preds))
            # results['fscore'].append(f1_score(cv_trues, cv_preds))
            # results['cnf'].append(confusion_matrix(cv_trues, cv_preds))

        # return results
