from scholarly import scholarly, ProxyGenerator
# get a free account on ScraperAPI
pg = ProxyGenerator()
success = pg.ScraperAPI('YOUR_SCRAPER_API_KEY')
scholarly.use_proxy(pg)
# Retrieve the author's data, fill-in, and print
# Get an iterator for the author results
search_query = scholarly.search_author('YOUR_NAME')
# Retrieve the first result from the iterator, make sure this is you
first_author_result = next(search_query)

# Retrieve all the details for the author
author = scholarly.fill(first_author_result)
# check if this is you by uncommenting the next line
# scholarly.pprint(author)

who_cited_me = []
for pub in author['publications']:
    pub_filled = scholarly.fill(pub)
    who_cited_me += [pub['bib']['author'] for pub in scholarly.citedby(pub_filled)]
    
# use a dictionary to count the occurrences of each name in the list. 
# Then, you can sort the dictionary based on the count values to get a ranked list of names.    
from collections import Counter

# Count occurrences of each name using Counter
name_count = Counter(who_cited_me)

# Sort the names based on their counts in descending order
sorted_names = sorted(name_count.items(), key=lambda x: x[1], reverse=True)

# Display the ranked list of names and their counts
print("Rank\tName\t\tCount")
print("--------------------------")
for rank, (name, count) in enumerate(sorted_names, start=1):
    print(f"{rank}\t{name}\t\t{count}")