# web_diction_dictionary_scraper

This is a project that provides a nifty and basic way to scrape webpages to extract web html content. 
It will simply parse the raw html using python's urllib and use regular expression to [find and replace] all the html tags with a space.
The parsed html content is then grouped into a set and word count occurrences are stored in a dictionary with the help of python's inbuilt module Counter that is contained in the package - collections.

Multiple web pages can be scraped and the content words in the Counter dictionaries can be compared using union, intersection and subsets.

# importance
This project is important as it provides a high level view of the most commonly used words as a result of comparing multiple web pages. Furthermore, it makes it easy to identify the occurrence and count of non-english words among scraped web content from either a single domain url or from multiple domain urls.

#Quick Start
locate the main function [if __name__ == '__main__':]
and in the indentation replace the urls strings with the website pages that you want to be scraped and have their content compared and contrasted.

# Help and Feedback
For any help I can be reached on email at cheseremtitus4@gmail.com

#Project Contributions
All are welcome to contribute to this project
