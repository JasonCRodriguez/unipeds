# IPEDS Data Analysis

| Date | Achievements|
|------|-------------|
| 2016-02-28| | 


## data-handler:
- [x] read data set
- [x] clean data
- [x] merge and filter data sets
    - [x] include only academic year 2012, private for-profit, public, private non-profit

## univ-performance: 
- [ ]  perform univariate and multivariate analysis
    - [x] by-sector analysis
        - [x] summary: create simple summary table
        - [x] plot: create simple summary plot
        - [ ] lm: create a Generalized linear multivariate model to evaluate the sector differences
        
## unigeocode: geocoding with GeoNames API
    - [x] attach lat-long to data set
    - [x] merge lat-long data set with distance education
    - [x] output a pandas dataframe
     
## BubbleMap
    - [ ] read a dataframe and write a geojson
    - [x] read geojson
    - [x] plot bubbles
        - [x] uni location
        - [ ] undergrad enrollment size
        - [ ] color based on retention rate or something
        - [ ] sliding bar to limit bubbles by retention rate/size
