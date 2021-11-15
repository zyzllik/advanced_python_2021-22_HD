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
    test_metrics = Test_protein.metrics
    assert hasattr(Test_protein, 'metrics') == True

#def test_