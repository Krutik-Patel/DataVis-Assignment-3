# Data preprocessing

## Merging SHCC and UCDP datasets

**Aim:**

- The ucpd ged dataset serves as a good complementing dataset to our existing shcc dataset as it has data on conflicts in general while shcc has data on attacks on health workers alone.

**Method:**

- this task was non-trivial as the only common columns between the two were country in date
- further complicated because shcc has precise date but ucpd has date range
- We had to perform binning week-wise to join the tables
- some data-loss was incurred
- had to be one-to-many mapping from shcc to ucdp

# ML techniques

## Clustering on SHCC data

**Aim:**

- To identify natural clusters of incidents based on number of health workers killed, kidnapped, infrastructure damage etc.

**Method:**

- Used KMeans implementation of scikit-learn.
- Empirically chose number of clusters as 4

**Observations & inferences:**

- The result of clustering is very imbalanced with the following being the number of incidents in each cluster:
  - 1 - 5948
  - 0 - 322
  - 2 - 24
  - 3 - 10
- Looking at statistical features of each cluster we infer the following:
  - Cluster 0 seems to indicate countries with less but non-zero number of health workers injured
  - Cluster 3 seems to indicate countries with more number of health workers injured
  - Cluster 1 seems to be a generic cluster where majority of the incidents lie
  - Cluster 2 seems to represent incidents where a large number of health workers seem to have been kidnapped
- Looking at countries prominent in each cluster, we infer the following:
  - Incidents from OPT (Other Palestenian Territories), Syria, Libya and DRC (Congo) seem to be predominant in cluster 0. This means conflicts in these regions are likely to injure health workers in the region.
  - Since cluster 1 is generic and doesn't have any unique attributes, the number of incidents of countries in this cluster is somewhat representative of their number of incidents in the entire dataset
  - We observe that incidents from Myanmar, Pakistan, Iran, Syria and Sudan find their place in cluster 2 which is implies a large number of health workers arrests. This is indicative of the oppressiveness of regimes in these countries.
  - We observe that 9 out of the 10 incidents in cluster 3 are from Palestine. The large number of health care workers injures might indicate widespread attacks on civilians or attacking health infrastructure as a strategic objective.
