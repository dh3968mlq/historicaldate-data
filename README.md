# historicaldate-data

![Example timeline image](https://picoteal.com/wp-content/uploads/2023/05/basic_timeline_example.png)

This is a repo for openly sharing datasets of historical events and lives in a simple CSV format. All data held here is, to the best of my knowledge, open public domain information with no copyright limitations.

It is intended for use with *historicaldate*, a Python package for handling events and lives with possibly uncertain dates and displaying timelines of them. For example dates may be specified as a year, or with a 'circa' indication or as a range of possible dates. See the ReadMe at https://github.com/dh3968mlq/historicaldate for details.

There are some example timelines at https://historicaldate.com/

It is at present a personal repo, with inevitable limitations on the amount of data held. Contributions would be most welcome, within the data guidelines below, either via pull requests or emails to david@historicaldate.com. I would be very happy for this repo to become an openly shared resource with wider contributions.

### Data guidelines

(Actually, more what you'd call 'actual rules' than guidelines)

   * It's an English language database
   * Dates and files must be in *historicaldate* format
   * Information must be in the public domain and free of copyright
   * Every row must contain a link in the *url* column to an entry English Wikipedia that at least mentions the relevant event or person.

### Limitations

At present *historicaldate* uses Python dates, and so is limited to AD (CE) dates. It cannot as yet deal with dates BC (BCE).


