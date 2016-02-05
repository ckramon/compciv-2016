# Show Me Where Project

A **project showing me where things** are.

### Denver Crimes Associated with Marijuana


# About the dataset

On the Denver Open Data site, they have a dataset showing all the crimes in the last year that, on review, had some connection to Marijuana (which has only been legal in the state for about two years. It does not list crimes related to the posession, sale or cultivation of marijuana, but other crimes that were later found to have been the result of Marijuana use.)


## Basic facts about the dataset

- The source of the data: [City of Denver, Open Data Catalog, Denver Police Department](http://data.denvergov.org/)
- The data's landing page: [Open Data Catalog](http://data.denvergov.org/dataset/city-and-county-of-denver-crime-marijuana)
- Direct link to the data: [http://data.denvergov.org/dataset/city-and-county-of-denver-crime-marijuana](http://data.denvergov.org/dataset/city-and-county-of-denver-crime-marijuana)
- The data format: CSV
- Number of rows: 998

## Description of data fields


#### INCIDENT_ID 

The Denver PD's way of keeping track of incident reports.


#### FIRST_OCCURENCE_DATE 

The date and time of the incident beginning.


#### LAST_OCCURENCE_DATE

The date and time of the incident ending.


#### REPORTDATE

When the incident was reported.


#### INCIDENT_ADDRESS  

Where in Denver the incident occurred.


#### GEO_X

Unclear, some kind of geocode.


#### GEO_Y

Unclear, some kind of geocode.


#### DISTRICT_ID

What district the crime occurred in.


#### PRECINCT_ID

What precinct the crime occurred in.


#### OFFENSE_CODE

What kind of crime it was.


#### OFFENSE_TYPE_ID

What type of offense it was.


#### OFFENSE_CATEGORY_ID

What category of offense it was.


#### MJ_RELATION_TYPE

How the incident related to Marijuana.


#### NEIGHBORHOOD_ID

What neighborhood in Denver it was.


## Anticipated data wrangling

I'm really interested to see what the most common Marijuana-associated crimes are 
(crimes under the influence of Marijuana), and how that has changed in the past decade since the drug has become legal. 
