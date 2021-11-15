import numpy as np
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from collections import deque
import matplotlib.pyplot as plt
from pathlib import Path

class Protein:
    #directory = Path.resolve()
    #path_csv = directory / 'amino_acid_properties.csv'
    #aa_properties = pd.read_csv(path_csv)
    
    def __init__(self, name, sequence):
        self.sequence = sequence
        self.name = name
    
    @property
    def metrics(self):
        aa_properties = pd.read_csv(Path(__file__).parent.parent.parent/'data/amino_acid_properties.csv')
        aa_properties = aa_properties.rename(columns ={'hydropathy index (Kyte-Doolittle method)': 'hydropathy'})
        aa_properties = aa_properties[['1-letter code', 'pI','hydropathy']]
        aa_properties = aa_properties.set_index('1-letter code')
        self._metrics = aa_properties.to_dict('dict')
        return self._metrics
    
    def get_x_values_plot(self):
        return list(np.arange(len(sequence_l)))

    def get_y_values_plot(self, metric, window_size):
        sequence_l = list(self.sequence)
        metric_values = []
        values_to_plot = []
        
        for aa in list(sequence_l):
            metric_values.append(self.metrics[metric][aa])

        sliding_window = deque([], maxlen=window_size)

        for value in metric_values:
            sliding_window.append(value)
            values_to_plot.append(np.mean(sliding_window))
            return values_to_plot

    def plot(self, metric ="hydropathy", window_size = 1):
            
        x_values = self.get_x_values_plot()
        y_values = self.get_y_values_plot(metric, window_size)

        data = [
            go.Bar(
                x=x_values,
                y=y_values,
            )
        ]

        fig = go.Figure(data=data)
        fig.update_layout(title=self.name, template = 'plotly_white')
        
        return fig
