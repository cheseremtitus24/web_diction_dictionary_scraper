import re

# step 4: Convert our procedures into a function.

def grab_webpage(url="http://localhost:80/index.html"):
	from urllib.request import urlopen
	#url = "http://localhost:80/index.html"
	page = urlopen(url)
	#Read html request object to a variable 
	html_bytes = page.read()
	# decode the bytes as a string
	html_txt = html_bytes.decode('utf-8')
	return html_txt
	

def parse_html(html):
	query_string_to_replace = html
	print("________________________")
	print("original String before Substituting htm tags with a space is \n")
	print("_________________________")
	print(query_string_to_replace)
	pattern = re.compile(r"<\s*[^<>]+\s*>")
	matches = pattern.				finditer(query_string_to_replace)

	print("__________________________")
	print("Matched tags to be removed  are the following: ")
	print("____________________________")
	for match in matches:
		#print(match.span())# get only the tuple span
		print(match.group(0))
	trimmed_tags_html = pattern.sub(r' ',query_string_to_replace)
	return trimmed_tags_html

def count_sorted_words(html_content=""):
	from collections import Counter
	words = html_content.split()
	unique_word_count = Counter(words)
	
	print("___________________________")
	print("Counter Dictionary Content ")
	print("___________________________")
	print(unique_word_count," \n")
	print("___________________________")
	print("Key[word]   Value[Occurrences] ")
	print("___________________________")
	
	for key, value in unique_word_count.items() :
		print (key, value)
	return unique_word_count
	
def perform_set_union_func(counter_dict0, counter_dict1):
		#unpack counter objects to a set
		unpacked_elem0 = counter_dict0.elements()
		unpacked_elem1 = counter_dict1.elements()	
		return  set(unpacked_elem0).union(set(unpacked_elem1)) 

def perform_set_intersection_func(counter_dict0, counter_dict1):
		#unpack counter objects to a set
		unpacked_elem0 = counter_dict0.elements()
		unpacked_elem1 = counter_dict1.elements()	
		return  set(unpacked_elem0).intersection(set(unpacked_elem1)) 
		
def perform_set_difference_func(counter_dict0, counter_dict1):
		#unpack counter objects to a set
		unpacked_elem0 = counter_dict0.elements()
		unpacked_elem1 = counter_dict1.elements()	
		return  set(unpacked_elem0).difference(set(unpacked_elem1)) 
		
if __name__ == '__main__':
	urls = ("http://127.0.0.1:80/index.html","http://127.0.0.1:80/about.html")
	word_counter_obj_list = list()
	for url in urls:
		result = grab_webpage(url)
		html_content = parse_html(result)
		#print("___________________________")
		#print("Trimmed HTML Content after substituting html tags")
		#print("___________________________")
		print(html_content)
		counter_dict = count_sorted_words(html_content)
		#print(counter_dict)
		word_counter_obj_list.append(counter_dict)
		
	#Sets (unions,subsets,supersets,intersection)
	#list_length =  len(word_dicts)
	
#	html_content_union_iterator = map(perform_set_union_func,word_counter_obj_list)
	
	html_content_union = perform_set_union_func( word_counter_obj_list[0] , word_counter_obj_list[1])
	
	# list(html_content_union_iterator)
	print("\n___________________________")
	print(f"   {len(html_content_union)} unions")
	print("\n___________________________")
	print(html_content_union)
	
	html_content_intersection = perform_set_intersection_func( word_counter_obj_list[0] , word_counter_obj_list[1])
	
	print("\n___________________________")
	print(f"   {len(html_content_intersection)} intersections")
	print("\n___________________________")
	print(html_content_intersection)
	
	html_content_difference = perform_set_difference_func( word_counter_obj_list[1] , word_counter_obj_list[0])
	
	print("\n___________________________")
	print(f"   {len(html_content_difference)} differences")
	print("\n___________________________")
	print(html_content_difference)
	
	
	
	
