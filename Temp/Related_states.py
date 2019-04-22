import libpysal as ps
import numpy as np
import pandas as pd

from giddy.markov import FullRank_Markov
import scipy.stats as ss

income_table = pd.read_csv(ps.examples.get_path("usjoin.csv"))

pci = income_table[list(map(str,range(1929,2010)))].values

ranks = FullRank_Markov(pci).ranks

final_data = pd.DataFrame()

for i in list(range(ranks.shape[0])):
    state = income_table['Name'][i]
    for j in list(range(0, ranks.shape[1] - 1)):
        print('{} processed out of {}'.format(i, len(list(range(0, ranks.shape[0] - 1)))), end = "\r")
        aux_dict = {'state' : state, 'rank_origin' : ranks[i,j], 'rank_destiny' : ranks[i,j+1]}
        aux = pd.DataFrame(data = aux_dict, index=[0])
        final_data = pd.concat([final_data.reset_index(drop = True), aux], axis = 0, sort = False)
        
final_data.to_csv("final_data.csv", index=False)

#final_data.head()

# Richest states
final_data.loc[(final_data.rank_origin == 1.0) & (final_data.rank_destiny == 1.0)].state.unique()
