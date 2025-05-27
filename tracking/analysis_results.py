import _init_paths
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [8, 8]

from lib.test.analysis.plot_results import plot_results, print_results, print_per_sequence_results
from lib.test.evaluation import get_dataset, trackerlist

trackers = []
dataset_name = 'mot'
"""hiptrack"""
trackers.extend(trackerlist(name='hiptrack', parameter_name='hiptrack', dataset_name=dataset_name,
                            run_ids=None, display_name='HIPTrack'))

dataset = get_dataset(dataset_name)
# dataset = get_dataset('otb', 'nfs', 'uav', 'tc128ce')
#plot_results(trackers, dataset, 'otb', merge_results=True, plot_types=('success', 'prec','norm_prec'),
#             skip_missing_seq=False, force_evaluation=True, plot_bin_gap=0.05)
print_results(trackers, dataset, dataset_name, merge_results=True, plot_types=('success', 'norm_prec', 'prec'))
# print_results(trackers, dataset, 'UNO', merge_results=True, plot_types=('success', 'prec'))
#29
# mot           | AUC        | OP50       | OP75       | Precision    | Norm Precision    |
# HIPTrack      | 69.75      | 82.18      | 59.37      | 49.85        | 81.11             |
#22
# mot           | AUC        | OP50       | OP75       | Precision    | Norm Precision    |
# HIPTrack      | 69.51      | 82.02      | 59.01      | 49.86        | 80.73             |

# 29 -0.3
# mot           | AUC        | OP50       | OP75       | Precision    | Norm Precision    |
# HIPTrack      | 69.63      | 82.77      | 59.15      | 50.37        | 81.42             |


# 0.5-26
# mot           | AUC        | OP50       | OP75       | Precision    | Norm Precision    |
# HIPTrack      | 69.69      | 82.20      | 59.13      | 49.70        | 80.74             |
# 0.3-26
# mot           | AUC        | OP50       | OP75       | Precision    | Norm Precision    |
# HIPTrack      | 69.87      | 82.49      | 59.48      | 50.28        | 80.98             |
# 0.7-26
# mot           | AUC        | OP50       | OP75       | Precision    | Norm Precision    |
# HIPTrack      | 69.73      | 82.24      | 59.53      | 49.93        | 80.84             |
# 0.2-26
# mot           | AUC        | OP50       | OP75       | Precision    | Norm Precision    |
# HIPTrack      | 69.81      | 82.24      | 59.56      | 49.99        | 80.83             |
# 0.6-26
# mot           | AUC        | OP50       | OP75       | Precision    | Norm Precision    |
# HIPTrack      | 69.40      | 81.98      | 58.83      | 49.97        | 80.86             |
# 0.1-26
# mot           | AUC        | OP50       | OP75       | Precision    | Norm Precision    |
# HIPTrack      | 69.81      | 82.32      | 59.50      | 49.95        | 81.12             |
# 1-26
# mot           | AUC        | OP50       | OP75       | Precision    | Norm Precision    |
# HIPTrack      | 67.28      | 81.32      | 54.61      | 44.45        | 80.07             |
