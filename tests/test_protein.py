import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent.resolve()), 
)

from exercises.day5 import protein

def test_protein_sequence():
    Test_protein = protein.Protein('Test', 'NKLGB')
    assert Test_protein.sequence == 'NKLGB'

def test_metrics_exists():
    Test_protein = protein.Protein('Test', 'NKLGB')
    assert hasattr(Test_protein, 'metrics') == True

def test_x_values():
    Test_protein = protein.Protein('Test', 'NKLGB')
    x_vals = Test_protein.get_x_values_plot()
    assert x_vals == [i for i in range(len(Test_protein.sequence))]
