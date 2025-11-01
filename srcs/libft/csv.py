import numpy as np
import csv

def load_csv(filename):

  dataset = list()

  with open(filename) as csvfile:

    reader = csv.reader(csvfile)

    try:

      for _ in reader:

        row = list()

        for value in _:

          try:

            value = float(value)

          except:

            if not value:

              value = np.nan

          row.append(value)

        dataset.append(row)

    except csv.Error as e:

      print(f'file {filename}, line {reader.line_num}: {e}')

  return np.array(dataset, dtype=object)