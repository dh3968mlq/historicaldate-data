# historicaldate-data

![Example timeline image](https://timeflows.uk/wp-content/uploads/2024/01/basic_timeline_example.png)

A repo of datasets of historical events and lives in a simple CSV format, with links to Wikipedia. 

This data is largely based on content from [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Copyrights), and so carries the following license terms:
*   [CC BY-SA 4.0: Creative Commons Attribution-ShareAlike 4.0 International License](https://en.wikipedia.org/wiki/Wikipedia:Text_of_the_Creative_Commons_Attribution-ShareAlike_4.0_International_License)
*   [GNU Free Documentation License](https://en.wikipedia.org/wiki/Wikipedia:Text_of_the_GNU_Free_Documentation_License)

It is intended for use with [historicaldate](hhttps://historicaldate.readthedocs.io/en/) and [hdtimelines](https://hdtimelines.readthedocs.io/en/), Python packages for handling events and lives with possibly uncertain dates and displaying timelines of them. For example dates may be specified as a year, or with a 'circa' indication or as a range of possible dates. 

See https://timeflows.uk/front-page/timelines-explorer/ for timelines produced from this data

### Data guidelines

   * It's an English language database
   * Files are in the format used by [hdtimelines](https://hdtimelines.readthedocs.io/en/)
   * Dates are in [historicaldate](hhttps://historicaldate.readthedocs.io/en/) format
   * Almost all rows contain a link in the *url* column to a relevant entry in English Wikipedia
