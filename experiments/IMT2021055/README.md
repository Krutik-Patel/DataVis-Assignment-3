# Experiments - IMT2021055

## Dataset
The UCPD GED dataset serves as a good complementing dataset to the previously explored SHCC dataset as it has data on conflicts (in general) while the SHCC dataset focusses solely on attacks on healthcare.

One of the major challenges faced during A1 (using the SHCC dataset) was the lack of data (and thus, the dominating presence of null values). This is rectified by using the GED dataset, which provides us with rich, disaggregated data.
## Data Preprocessing
### Preprocessing Using Tableau Prep
The original UCPD GED dataset was loaded into Tableau Prep and the columns which did not appear to be important (such as different ids) were dropped. Null Values, if any, were appropriately imputed. The entire UCPD GED dataset was filtered on the range 2018-2022 over the `year` column to match the time period available in the SHCC dataset (used in A1). The resultant dataset was exported as a new excel file.
### Data Reorganization And Grouping Using Pandas
The relevant columns in the new excel were: `\['year', 'type_of_violence', 'side_a', 'side_b', 'number_of_sources', 'source_article', 'source_office', 'source_date', 'where_coordinates', 'latitude', 'longitude', 'country', 'region', 'date_start', 'date_end', 'deaths_a', 'deaths_b', 'deaths_civilians', 'deaths_unknown', 'best', 'high', 'low'\]`
#### Grouping
The data was grouped over the following columns separately to identify interesting cases for further exploration. Statistical measures such as standard deviation, mean, minimum, maximum, and sum were used (for numerical columns: `\['deaths_a', 'deaths_b', 'deaths_unknown', 'best'\]`) to facilitate these decisions.

- **Country:** The data was aggregated and grouped by `country`, producing to summary statistics for each country across the years 2018-2022.
- **Year:** The data was aggregated and grouped by `year`, producing to summary statistics for each year across all countries available in the dataset.
- **Region:** The data was aggregated and grouped by `region`, producing to summary statistics for each region across the years 2018-2022. Here, the continents are naively considered as regions.
#### Data Reorganization
The following hierarchies were explored in the dataset after reorganization to identify interesting cases for further exploration. Once again, statistical measures such as standard deviation, mean, minimum, maximum, and sum were used (for numerical columns: `\['deaths_a', 'deaths_b', 'deaths_unknown', 'best'\]`) to facilitate these decisions. The decision to reorganize the data into hierarchies was largely influenced by the groupings performed earlier.

- **Region-Year Hierarchy:** The data was reorganized such that at the topmost level, we have regions, and below them (for each region) we have different years. The data corresponding to each year within a particular region describes the summary statistics for that region in that year.
- **Country-Year Hierarchy:** The data was reorganized such that at the topmost level, we have countries, and below them (for each country) we have different years. The data corresponding to each year within a particular country describes the summary statistics for that country in that year.
- **Region-Country-Year Hierarchy:** The data was reorganized such that at the topmost level, we have regions, and below them (for each region) we have different countries which lie within that region. Finally, below each country, we have different years. The data corresponding to each year within a particular country (lying in a particular region) describes the summary statistics for that country in that region, in that year.
## Machine Learning Techniques
## Clustering on GED Data
### Aim
- To identify natural clusters of incidents based on the location (`latitude` and `longitude`) within a region or country for further exploration in order to draw useful inferences.
### Method
- KMeans implementation of scikit-learn was used to perform clustering.
- Empirically chose number of clusters as 4 (expecting each of the clusters to represent one of North, South, East, and West).
### Observation And Inferences
#### Ukraine - 2022
The results of the clustering were as follows:

| Cluster Number | Count | Color | Indicates |
| --- | --- | --- | --- |
| 0 | 2719 | Blue | East |
| 1 | 724 | Orange | North |
| 2 | 730 | Red | South |
| 3 | 650 | Cyan/Light Green | North-East |
[Table 1]

![[Ukraine-2022.png]]
[Figure 1]

We observe (in Figure 1 and Table 1) a discernably high count for cluster 0. Upon visualizing the reported incidents on a geographical map and marking the clusters using color, we observe that cluster 0 represents the incidents along the eastern border of Ukraine, that is, the Russia-Ukraine border. These are indicated in blue color.

This observation leads to the inference that during the war between Russia and Ukraine, a dominating fraction of the attacks were along the shared border between the two countries.

We also observe that there is a dense "group" of incidents (in red color, cluster 2) around what is roughly the middle of cluster 2 (in northern Ukraine).

We infer that this "group" appears to be located around Kiev, Ukraine's capital, which was an important target during the war.
#### Afghanistan - 2020
The results of the clustering were as follows:

| Cluster Number | Count | Color | Indicates |
| --- | --- | --- | --- |
| 0 | 816 | Blue | North |
| 1 | 981 | Orange | West |
| 2 | 678 | Red | South |
| 3 | 842 | Cyan/Light Green | East |
[Table 2]

![[Afghanistan-2020.png]]
[Figure 2]

We observe (in Figure 2 and Table 2) that all clusters roughly report the same number of incidents (about 650-950). Upon visualizing the reported incidents on a geographical map and marking the clusters using color, this observation is reaffirmed as we observe all 4 clusters to be spread uniformly across the country.

This observation leads to the inference that during due to the prolonged conflict (starting as far back as 1996) in Afghanistan and the time that rebels, militants, and terror groups have had, the damage and destruction has spread throughout the country (by the year 2020).

We also observe an empty patch located slightly to the right of central Afghanistan, indicating a lack of reported incidents from this region.

We infer that this "empty patch" is indicative of the geography of Afghanistan and is probably spanned over by mountain ranges, which do not make viable targets for attacks. This is further confirmed by Figure 3.

![[Pasted image 20231212164856.png]]
[Figure 3: A geographical overview of Afghanistan: Image Courtesy - Wikipedia]
#### Myanmar - 2021

| Cluster Number | Count | Color | Indicates |
| --- | --- | --- | --- |
| 0 | 128 | Blue | North |
| 1 | 464 | Orange | West |
| 2 | 113 | Red | South |
| 3 | 142 | Cyan/Light Green | East |
[Table 3]

![[Myanmar-2021.png]]
[Figure 4]

We observe (in Figure 4 and Table 3) that cluster 1 (indicated in orange) reports significantly higher number of incidents than other clusters. Upon visualizing the reported incidents on a geographical map and marking the clusters using color, this observation is reaffirmed as we observe a dominant presence of orange marks near Central and Western Myanmar.

[This observation leads to the inference that during due to the prolonged conflict (starting as far back as 1996) in Afghanistan and the time that rebels, militants, and terror groups have had, the damage and destruction has spread throughout the country (by the year 2020).]
#### Syria - 2020

| Cluster Number | Count | Color | Indicates |
| --- | --- | --- | --- |
| 0 | 136 | Blue | North |
| 1 | 266 | Orange | West |
| 2 | 155 | Red | South |
| 3 | 583 | Cyan/Light Green | East |
[Table 4]

![[Syria-2020.png]]
[Figure 5]

We observe (in Figure 5 and Table 4) that cluster 3 (indicated in cyan/light green) reports significantly higher number of incidents compared to other clusters. Upon visualizing the reported incidents on a geographical map and marking the clusters using color, this observation is reaffirmed as we observe a dominant presence of cyan/light green marks near the North-West border of the nation (the Turkey-Syria border).

[This observation leads to the inference that during due to the prolonged conflict (starting as far back as 1996) in Afghanistan and the time that rebels, militants, and terror groups have had, the damage and destruction has spread throughout the country (by the year 2020).]

![[Pasted image 20231212172705.png]]
[Figure 6: A bird's eye view of war-torn regions in Syria: Image Courtesy - Washington Post]

![[Pasted image 20231212172804.png]]
[Figure 7: Regions and their controlling authority: Image Courtesy - National Geographic Education Blog]

