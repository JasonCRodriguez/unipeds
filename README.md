# ipeds-analysis
2015-05-10
-	University data (IPEDS)
o	Completion rates by university characteristics
?	Age
?	Expenditures (support, student services, etc)
?	Student demographic information
•	Look at in-district population statistics
•	Proportion students on financial aid
o	Assistance per student
o	Next steps
?	Select variables (mostly done)
?	Read in data
•	Chunk the data using pandas iterator that supports chunking
Data = [generic dataFrame]
For chunk in iterator(data_set):
	Chunk = read_csv(data_set)
	Data = append(data, chunk[selected columns])
?	Create initial one-ways

2015-05-17
Accomplishments:
-	Read in data using chunk and usecols
-	Selected a column subset
-	Created some initial groupings based on year and state
Next steps:
-	Create additional groupings to check out the data
o	Group by year
?	Populations stats
?	Expenditures
-	Create a way to calculate the retention rate for our different groups
o	Retention rate is our target
?	Weighted average retention rate
-	Create plots of university characteristics and retention rate
2015-05-31
Accomplishments:
-	Made plots to look at retention rates
-	Sorted the data set by undergrad size
-	Discovered that the data set contains a range of universities
o	For example, sector
o	Some have high aid and low retention
?	Are all for-profit universities high aid, low retention?
-	We focused on a single year (2012)
Next Steps:
-	Decide on criteria to identify our universities of interest to deal with the university heterogeneity
-	Improve plots
o	Possibly create new variables based on numeric variables
?	Categorization
o	Try out heat-maps
2015-06-14
Accomplishments:
-	Identifying a group of universities for analysis
o	Most universities are have fewer than 4K total undergrads
?	count      2458.000000
?	mean       4426.139138
?	std       10562.250888
?	min           1.000000
?	25%         572.250000
?	50%        1527.500000
?	75%        4095.750000
?	max      253011.000000
?	* this is data from 2012 only and only four-year universities
o	Created a cumulative fall total undergrad distribution
?	The first 2000 smallest universities account for ~90% of the total number of students enrolled
o	# of FTE per 100 FT students is less than 3 for the online universities (at least the three largest)
Next steps:
-	Consider newer data set
o	Is there an equivalent data table?
-	Actually create our analysis data set using the filters described above (ie undergrad count between X and Y, FTE/ 100 FTS > 3, 4-year universities only)
-	Look at retention by different university characteristics
o	Look at linear correlations
o	Transform the variables
o	Create univariate tables and graphs
2015-06-21
Accomplishments:
-	Discovered a potential selection bias in the graduation and retention rates.  For-profit universities do not always report the data despite receiving federal funds
Next steps:
-	Look at retention and graduate rates by sector to look for evidence of a selection bias

