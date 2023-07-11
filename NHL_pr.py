import csv
from typing import List

import matplotlib.pyplot as plt
import numpy as np
import pytest


def id_to_fruit(fruit_id: int, fruits: List[str]) -> str:
    if fruit_id < len(fruits):
        return fruits[fruit_id]
    raise RuntimeError(f"Fruit with id {fruit_id} does not exist")


def test_id_to_fruit():
    assert id_to_fruit(1, ["apple", "orange", "melon", "kiwi", "strawberry"]) == "orange"
    assert id_to_fruit(3, ["apple", "orange", "melon", "kiwi", "strawberry"]) == "kiwi"
    assert id_to_fruit(4, ["apple", "orange", "melon", "kiwi", "strawberry"]) == "strawberry"
    with pytest.raises(RuntimeError) as excinfo:
        id_to_fruit(5, ["apple", "orange", "melon", "kiwi", "strawberry"])


def swap(coords: np.ndarray):
    coords[:, 0], coords[:, 1], coords[:, 2], coords[:, 3] = \
        coords[:, 1].copy(), coords[:, 0].copy(), coords[:, 3].copy(), coords[:, 2].copy()
    return coords


def test_swap():
    coords = np.array([[10, 5, 15, 6, 0],
                       [11, 3, 13, 6, 0],
                       [5, 3, 13, 6, 1],
                       [4, 4, 13, 6, 1],
                       [6, 5, 13, 16, 1]])
    swapped_coords = swap(coords)
    assert swapped_coords.all() == coords.all()


def test_draw_precision_recall_plot():
    csv_file_path = 'data_file.csv'

    results = []
    with open(csv_file_path) as result_csv:
        csv_reader = csv.reader(result_csv, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            results.append([float(val) for val in row])  # Convert string values to floats
        results = np.stack(results)

    # plot precision-recall curve
    plt.plot(results[:, 1], results[:, 0])
    plt.ylim([-0.05, 1.05])
    plt.xlim([-0.05, 1.05])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.show()


def test_plot_data():
    csv_file_path = 'data_file.csv'
    results = []
    with open(csv_file_path) as result_csv:
        csv_reader = csv.reader(result_csv, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            results.append(row)
        results = np.stack(results)

    # plot precision-recall curve
    plt.plot(results[:, 1], results[:, 0])
    plt.ylim([-0.05, 1.05])
    plt.xlim([-0.05, 1.05])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.show()
