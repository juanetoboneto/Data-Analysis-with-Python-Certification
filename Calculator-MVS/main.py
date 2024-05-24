import numpy as np


def calculate(list):

  # Condition of ValueError:
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

# Lists of Matrix files:
  file_1 = [list[0], list[1], list[2]]
  file_2 = [list[3], list[4], list[5]]
  file_3 = [list[6], list[7], list[8]]
# Lists of Matrix columns:
  column_1 = [list[0], list[3], list[6]]
  column_2 = [list[1], list[4], list[7]]
  column_3 = [list[2], list[5], list[8]]

# Create the dictionary:
  calculations = {
      'mean': [[np.mean(column_1),
                np.mean(column_2),
                np.mean(column_3)],
               [np.mean(file_1),
                np.mean(file_2),
                np.mean(file_3)],
               np.mean(list)],
      'variance': [[np.var(column_1),
                    np.var(column_2),
                    np.var(column_3)],
                   [np.var(file_1),
                    np.var(file_2),
                    np.var(file_3)],
                   np.var(list)],
      'standard deviation':
      [[np.std(column_1), np.std(column_2),
        np.std(column_3)], [np.std(file_1),
                            np.std(file_2),
                            np.std(file_3)],
       np.std(list)],
      'max': [[np.max(column_1),
               np.max(column_2),
               np.max(column_3)],
              [np.max(file_1), np.max(file_2),
               np.max(file_3)],
              np.max(list)],
      'min': [[np.min(column_1),
               np.min(column_2),
               np.min(column_3)],
              [np.min(file_1), np.min(file_2),
               np.min(file_3)],
              np.min(list)],
      'sum': [[np.sum(column_1),
               np.sum(column_2),
               np.sum(column_3)],
              [np.sum(file_1), np.sum(file_2),
               np.sum(file_3)],
              np.sum(list)]
  }

  return calculations

print(calculate([0,1,2,3,4,5,6,7,8]))