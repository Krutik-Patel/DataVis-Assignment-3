## Prior Visualizations and Inferences
(Refer to Assignment - 1 Report [here](https://drive.google.com/file/d/1Y_7gA8rXsIsCU-aiNzAtsxRIDqNl4-Ee/view?usp=sharing))
This section summarizes my task for CS732-Assignment-1 (Task-2), where I aimed to give an overview of Attacks in Health Care in Countries in Conflict for the years 2020, 2021, and 2022. It serves as an appendix for Assignment-3, and may initially be skipped by the reader.
### Visualization Methodology - A1
- I started by visualizing the count of reported incidents in various countries around the world as a choropleth map for a particular year, say 2021.
- Using the world map overview, I identified countries/regions with high number of reported incidents, and then provided a zoomed in view of each (in this case, Myanmar, OPT, DRC, and CAR). These choices were strengthened by a bar chart which essentially depicted the same data.
- I then visualized the trend in number of reported incidents over different months for the entire world and for each of the identified regions, linking peaks across them.
- The categories (state actor, opposition group, etc) of perpetrators and various perpetrator groups were visualized first as bar charts and then as pie charts. A stacked bar chart was also used to visualize the distribution of perpetrators across different categories in select countries.
- Finally, I visualized weapon types (explosives, firearms, etc) used in reported incidents in different countries as a pie chart and a stacked bar chart. 
### Inferences - A1
- From the cartographic maps in Fig. 7. and Fig. 8., we identify that in 2021, the regions that reported the most number of attacks on healthcare are Myanmar, Dominican Republic of Congo, Central African Region, and Occupied Palestinian Territory. These beliefs are further confirmed by the bar chart in Fig. 9.
- The line charts in Fig. 10. and Fig. 11. together provide an overview of how the 4 aforementioned regions affect the trend of number of attacks in 2021 (for the entire world) when seen monthly. In Fig. 10., the chart first peaks in March, which can be attributed to the rise in attacks in Myanmar in the same month (March), and then peaks again in May, which can be attributed primarily to the large number of attacks reported in Occupied Palestinian Territory in May. This is evident on comparing Fig. 10. and Fig. 11.
- Figures 12, 14, 15, and 16 in particular indicate that there is a void in information. A large portion of data, especially in regions like Central Africa and Occupied Palestinian Territory, can be attributed to their regime’s/government’s continuing oppressive and discriminatory system of governing the region. Such regimes often hinder or block the flow of information needed to build dataset such as the one provided.
- The rise of attacks on healthcare in Myanmar in March of 2021 (as seen in Fig. 11., top left) can be attributed to the 2021 Myanmar coup d’etat´, which began in February of 2021.
- The rise of attacks on healthcare in Occupied Palestinian Territory in May of 2021 (as seen in Fig. 11., bottom left) can be attributed to the Escalation of attacks in Gaza Strip, West Bank, and East Jerusalem. These led to damage of hospitals, primary health clinics, and other public health infrastructure.
- From the available information, we infer that Firearms and Explosives were the primary categories of weapons used in attacks on healthcare in 2021, and Myanmar was the biggest contributor in terms of reported incidents involving attacks on healthcare (Fig. 17, 18.). This is different than what was observed in the data stories for 2022 and 2020 (attached with the submission), for which the major contributors were war-torn countries like Ukraine, Syria, and Afghanistan.
- From collectively looking at the data stories of 2020, 2021, and 2022, we also observe that the Central African Region (DRC, CAR, Ethiopia, Sudan) have always been in a state of conflict during this period.
## New Ideas To Build On
- While identifying a country where the number of reported incidents is high serves as a good starting point, it is naive to say that the entire country is enduring conflict. We aim to further narrow down the area of conflict and draw significantly improved inferences.
- While we have been able to visualize what different categories of perpetrators are present in different countries (and in what ratio) through stacked bar charts and pie charts, it would be useful to identify specific locations within a country and visualize the perpetrator type for each incident.
These two points serve as feedback from the visualizations generated for Assignment-1, and should thus be incorporated in the workflow.
## Dataset
The UCPD GED dataset serves as a good complementing dataset to the previously explored SHCC dataset as it has data on conflicts (in general) while the SHCC dataset focusses solely on attacks on healthcare.

One of the major challenges faced during A1 (using the SHCC dataset) was the lack of data (and thus, a dominating presence of null values was encountered). This is rectified by using the GED dataset, which provides us with rich, disaggregated data.
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
| 1 | 724 | Orange | South |
| 2 | 730 | Red | North |
| 3 | 650 | Cyan/Light Green | North-East |
Table 1

![[Ukraine-2022.png]]
Figure 1

We observe (in Figure 1 and Table 1) a discernably high count for cluster 0. Upon visualizing the reported incidents on a geographical map and marking the clusters using color, we observe that cluster 0 represents the incidents along the eastern border of Ukraine, that is, the Russia-Ukraine border. These are indicated in blue color.

This observation leads to the inference that during the war between Russia and Ukraine, a dominating fraction of the attacks were along the shared border between the two countries.

We also observe that there is a dense "group" of incidents (in red color, cluster 2) around what is roughly the middle of cluster 2 (in northern Ukraine).

We infer that this "group" appears to be located around Kiev, Ukraine's capital, which was an important target during the war.
#### Afghanistan - 2020
The results of the clustering were as follows:

| Cluster Number | Count | Color | Indicates |
| --- | --- | --- | --- |
| 0 | 816 | Blue | North |
| 1 | 981 | Orange | South |
| 2 | 678 | Red | West |
| 3 | 842 | Cyan/Light Green | East |
Table 2

![[Afghanistan-2020.png]]
Figure 2

We observe (in Figure 2 and Table 2) that all clusters roughly report the same number of incidents (about 650-950). Upon visualizing the reported incidents on a geographical map and marking the clusters using color, this observation is reaffirmed as we observe all 4 clusters to be spread uniformly across the country.

This observation leads to the inference that due to the prolonged conflict (starting as far back as 1996) in Afghanistan and the time that rebels, militants, and terror groups have had, the damage and destruction has spread throughout the country (by the year 2020).

We also observe an empty patch located slightly to the right of central Afghanistan, indicating a lack of reported incidents from this region.

We infer that this "empty patch" is indicative of the geography of Afghanistan and is probably spanned over by mountain ranges, which do not make viable targets for attacks. This is further confirmed by Figure 3.

![[Pasted image 20231212164856.png]]
Figure 3: A geographical overview of Afghanistan: Image Courtesy - Wikipedia
#### Myanmar - 2021
Due to the "tall and narrow" geography of Myanmar, the clusters indicate Upper, Upper-Middle, Lower-Middle, and Lower segments instead of the expected North, South, East, and West.

| Cluster Number | Count | Color | Indicates |
| --- | --- | --- | --- |
| 0 | 128 | Blue | Lower-Middle |
| 1 | 464 | Orange | Upper-Middle |
| 2 | 113 | Red | Upper |
| 3 | 142 | Cyan/Light Green | Lower |
Table 3

![[Myanmar-2021.png]]
Figure 4

We observe (in Figure 4 and Table 3) that cluster 1 (indicated in orange) reports significantly higher number of incidents than other clusters. Upon visualizing the reported incidents on a geographical map and marking the clusters using color, this observation is reaffirmed as we observe a dominant presence of orange marks near Central and Western Myanmar.

This observation leads to the inference that during due to the prolonged conflict (starting as far back as 1996) in Afghanistan and the time that rebels, militants, and terror groups have had, the damage and destruction has spread throughout the country (by the year 2020).

We also observe that cluster 3 (indicated by cyan/light green) constituted the second-highest fraction of reported incidents, and is focused more near the southern part of the country.

The inference that we draw from this observation is as follows: *historically*, the southern part of Myanmar was occupied by minorities (mostly Muslims) who were rigorously discriminated against, which might have led to conflict in the area (using Figure 8 as a reference).

![[WhatsApp Image 2023-12-12 at 21.16.32_cf80371c.jpg]]
Figure 8: Shows the percent population of Muslims in different states of Myanmar: Image Courtesy - [State wise Muslim population distribution in Myanmar according to census | ResearchGate](https://www.researchgate.net/figure/State-wise-Muslim-population-distribution-in-Myanmar-according-to-2014-census-A_fig2_332253865)

Overall, the entire country appears to be covered by conflict, from which we infer that a nation-wide event must have occurred, triggering this scenario. We conclude that the Coup in Myanmar (2021) is a strong candidate for this situation (see reference: [2021 Myanmar Coup D’etat | Britannica](https://www.britannica.com/event/2021-Myanmar-coup-d-etat)).
#### Syria - 2020

| Cluster Number | Count | Color | Indicates |
| --- | --- | --- | --- |
| 0 | 136 | Blue | North |
| 1 | 266 | Orange | East, North-East |
| 2 | 155 | Red | South, South-West |
| 3 | 583 | Cyan/Light Green | West, North-West |
Table 4

![[Syria-2020.png]]
Figure 5

We observe (in Figure 5 and Table 4) that cluster 3 (indicated in cyan/light green) reports significantly higher number of incidents compared to other clusters. Upon visualizing the reported incidents on a geographical map and marking the clusters using color, this observation is reaffirmed as we observe a dominant presence of cyan/light green marks near the North-West border of the nation (the Turkey-Syria border). The obtained visualization is also in accordance with the actual war-torn regions in Syria (see Figure 6), as per the Washington Post.

This observation leads to the inference that cluster 3 spans an area which is primarily under the control of rebel groups and is surrounded by areas which are controlled by the Syrian government (see Figure 7). This situation was one of the primary causes of conflict near the North-West border of Syria, which was additionally burdened with the incursion of Kurdish forces from the North.

We also observe (in Figure 5) a prominent straight line in cluster 1 (indicated by orange, second highest by count) running from South-East to North-West direction, before entering cluster 0 (indicated by blue).

From this observation, we infer that this area was probably a volatile zone of conflict, which is further confirmed by Figure 6, which depicts the area in question as being war-torn, and Figure 7, which demarcates it as being under the control of the Islamic State in Iraq and the Levant (ISIL), a well-known insurgent group.

Finally, we notice that cluster 2 (indicated by red, third highest by count) is tightly grouped in the southern part of Syria.

We infer that this grouping is probably centered around Damascus and Daraya (see Figure 7), which are important cities in Syria, making them strategic targets for insurgent groups and rebels.

![[Pasted image 20231212172705.png]]
Figure 6: A bird's eye view of war-torn regions in Syria: Image Courtesy - Washington Post

![[Pasted image 20231212172804.png]]
Figure 7: Regions and their controlling authority: Image Courtesy - National Geographic Education Blog

\* We recognize that Figure 7 is dated 2016, but for our purposes, the regions being controlled by various organizations remained largely the same till 2020.
## Data Analytics Workflow
(Reference: [Visual Analytics: Definition, Process and Challenges, Kiem et al. (cnrs.fr)](https://hal-lirmm.ccsd.cnrs.fr/lirmm-00272779/document))

![[Pasted image 20231212223606.png]]
Figure 9: Kiem et al. visual analytics workflow: Image Courtesy - [Visual Analytics: Definition, Process and Challenges (cnrs.fr)](https://hal-lirmm.ccsd.cnrs.fr/lirmm-00272779/document)

We now provide a summary of 2 runs of the above workflow.
### First Run
#### Data
Minimal data processing was done, where certain cases of categorical variables were noted and subsequently merged categories related to unavailable data. Null values were appropriately imputed based on variables.
#### Visualization
- I started by visualizing the count of reported incidents in various countries around the world as a choropleth map for a particular year, say 2021.
- Using the world map overview, I identified countries/regions with high number of reported incidents, and then provided a zoomed in view of each (in this case, Myanmar, OPT, DRC, and CAR). These choices were strengthened by a bar chart which essentially depicted the same data.
- I then visualized the trend in number of reported incidents over different months for the entire world and for each of the identified regions, linking peaks across them.
- The categories (state actor, opposition group, etc) of perpetrators and various perpetrator groups were visualized first as bar charts and then as pie charts. A stacked bar chart was also used to visualize the distribution of perpetrators across different categories in select countries.
- Finally, I visualized weapon types (explosives, firearms, etc) used in reported incidents in different countries as a pie chart and a stacked bar chart. 
#### Models
No models were used when going through the workflow for the first time.
#### Knowledge
(Please note that the figure numbers in this subsection indicate the figure numbers as mentioned in the report for Assignment-1, available [here](https://drive.google.com/file/d/1Y_7gA8rXsIsCU-aiNzAtsxRIDqNl4-Ee/view?usp=sharing))
- From the cartographic maps in Fig. 7. and Fig. 8., we identify that in 2021, the regions that reported the most number of attacks on healthcare are Myanmar, Dominican Republic of Congo, Central African Region, and Occupied Palestinian Territory. These beliefs are further confirmed by the bar chart in Fig. 9.
- The line charts in Fig. 10. and Fig. 11. together provide an overview of how the 4 aforementioned regions affect the trend of number of attacks in 2021 (for the entire world) when seen monthly. In Fig. 10., the chart first peaks in March, which can be attributed to the rise in attacks in Myanmar in the same month (March), and then peaks again in May, which can be attributed primarily to the large number of attacks reported in Occupied Palestinian Territory in May. This is evident on comparing Fig. 10. and Fig. 11.
- Figures 12, 14, 15, and 16 in particular indicate that there is a void in information. A large portion of data, especially in regions like Central Africa and Occupied Palestinian Territory, can be attributed to their regime’s/government’s continuing oppressive and discriminatory system of governing the region. Such regimes often hinder or block the flow of information needed to build dataset such as the one provided.
- The rise of attacks on healthcare in Myanmar in March of 2021 (as seen in Fig. 11., top left) can be attributed to the 2021 Myanmar coup d’etat´, which began in February of 2021.
- The rise of attacks on healthcare in Occupied Palestinian Territory in May of 2021 (as seen in Fig. 11., bottom left) can be attributed to the Escalation of attacks in Gaza Strip, West Bank, and East Jerusalem. These led to damage of hospitals, primary health clinics, and other public health infrastructure.
- From the available information, we infer that Firearms and Explosives were the primary categories of weapons used in attacks on healthcare in 2021, and Myanmar was the biggest contributor in terms of reported incidents involving attacks on healthcare (Fig. 17, 18.). This is different than what was observed in the data stories for 2022 and 2020 (attached with the submission), for which the major contributors were war-torn countries like Ukraine, Syria, and Afghanistan.
- From collectively looking at the data stories of 2020, 2021, and 2022, we also observe that the Central African Region (DRC, CAR, Ethiopia, Sudan) have always been in a state of conflict during this period.
#### Feedback
These two points serve as feedback from the visualizations generated in the first run, and should thus be incorporated in the workflow for the second run.
- While identifying a country where the number of reported incidents is high serves as a good starting point, it is naive to say that the entire country is enduring conflict. We aim to further narrow down the area of conflict and draw significantly improved inferences.
- While we have been able to visualize what different categories of perpetrators are present in different countries (and in what ratio) through stacked bar charts and pie charts, it would be useful to identify specific locations within a country and visualize the perpetrator type for each incident.
### Second Run
#### Data
#### Models
#### Visualization
#### Knowledge
#### Feedback

## Authors
- Vidhish Trivedi - IMT2021055
