Automated Gender Analysis of Washington State Highway Stop Data


Introduction

This is an automated analysis of the gender makeup of traffic stops in Washington State in 2011, according to the Washington State Highway Patrol. Surficial findings indicate that men outnumber women in performing highway stops in Washington State by roughly 10 to 1, and that our gender detector was relatively accurate (it was only off by about 1 for the ratio of males to females we detected compared to the actual from the dataset). And we learned that females and males have roughly the same ratio of males stopped to females stopped: roughly 2.2 males stopped to every 1 female stopped regardless of officer gender.


Methodology

The methodology of the gender detection is similar to that of the babynames-gender-detector homework.

We removed fields of interest from the raw dataset and put them into a new one called classified-data.csv. Our gender detection proved accurate compared to the gender field in the original dataset. 


Past research and articles

Perhaps more interesting is highway stops as they relate to race: it has been proven time and time again that racial profiling exists during highway patrols. This gives me an idea of how to work with this data (which happens to include gender but that probably isn't the most interesting aspect of it) when it comes to race. Washington has a statewide law requiring that race is collected during highway stops, but analysis is done at a local level, and most localities have not analyzed race data since about 2007. 


Methodology and Caveats

Gender isn't necessarily super informative when it comes to highway stops. There are vastly more male officers than female officers, but because there is so little data to draw on for female officers, the analysis that can be done is limited. Additionally, when we looked at race, there were a lot of null fields, implying that officers didn't know the race of those they stopped. The race listed in this dataset is that of perceived race (what the officer thought the race of the person they stopped was) but doesn't include the actual race, so there could be some bias present, though perceived race is what is most important to representation of profiling. 
