import seaborn as sn
import pandas as pd
import csv
from collections import Counter
import matplotlib.pyplot as plt

def aa_propensity(input_file_path, output_file_path = 'output.csv'):
    aminoacid_counter = Counter()

    with open(input_file_path, 'r') as uniprot_file:
        for line in uniprot_file:
            if line[0] != '>':
                line = line.strip()
                aminoacid_counter += Counter(line)

    with open(output_file_path, 'w', newline = '') as output_file:
        output_writer = csv.writer(output_file)
        output_writer.writerow(['aa', 'counter'])
        for key, value in sorted(aminoacid_counter.items()):
            output_writer.writerow([key, str(value)])
    return aminoacid_counter

def plot_aa_distribution_to_pdf(aap_output, output_file='barplot.pdf'):
    col_names = ['Count']
    aap_output_df = pd.DataFrame.from_dict(aap_output, orient='index', columns=col_names)
    aap_output_df = aap_output_df.rename_axis('Aminoacid').reset_index()
    ax = sn.barplot(x = 'Aminoacid', y = 'Count', data = aap_output_df)
    ax.set_title("Aminoacid propensity")
    plt.savefig(output_file)

input_file = input()
aas = aa_propensity(input_file)
plot_aa_distribution_to_pdf(aas)