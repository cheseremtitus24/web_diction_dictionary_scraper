# Regular expressions using the finditer method that returns span

# performance tuning - make use of yield statement on the urlopen function

import re

# regex help from https://www.youtube.com/watch?v=K8L6KVGG-7o&t=622s

query_string_to_replace = "This is a sample string with an < tag style='color: red;width=100'> you are </tag>"

query_string_to_replace = '<!DOCTYPE html>\n<html>\n  <head>\n    <link href="css/styles.css" rel="stylesheet">\n  </head>\n  <body>\n\n    <h1>My Website</h1>\n\t<P> I am the stone that the builder refused\n\t  I am the visual the inspiration that made the ladies sing the blues. I am the ballot in your box,\n\t  The bullet in the gun. That inner glow that makes you call your brother son.\n\t  The story that has just begun. The promise of what\'s to come. And I will remail a soldier until the war is won.\n\t  \n\n    <img id=\'myimage\' src="img/android1.png">\n\n\t<script src="js/scripts.js"></script>\n  </body>\n</html>\n'

print("________________________")
print("original String is \n")
print("_________________________")
print(query_string_to_replace)



#todo:
	#1. first we need to replace to match all the opening tag html elements then replace them with a space.
	# Therefore, we'll need to eliminate possible mismatch such as < tag>, <   tag>. Notice the spaces which we'll have to account for.

# compile the pattern
#\w      - Word Character (a-z, A-Z, 0-9, _)
# .       - Any Character Except New Line
#+       - 1 or More

# The dot character will account for any misplaced spaces after the opening tag <. 
# the period matches any thing except a new line
#The \w will account for any tag element since they contain [a-z, A-Z] as they are case insensitive.
#the digits [0-9] are used in defining the width and height

#such as < b/> will be matched. the tags must have atleast one or more characters therefore we'll use a + in our regex.' 

pattern = re.compile(r'<(.\w+)>')# greedy method 

pattern = re.compile(r'<[^|~\?$<>]+>')# non-greedy method as it performs elimination
# tag starts with zero or more whitespaces so that < tag> and <tag> qualify

# a whitespace can be zero or more at beginning of tag as well as end of tag will qualify the following: <tag >, <tag>, < tag>, < tag >

 # the [^<>] grabs the content within our tag. And through elimination. There is no tag that has angle brackets as its attribute content. # regex sourced from https://techstacker.com/regex-find-every-html-tag-document/
  

pattern = re.compile(r"<\s*[^<>]+\s*>")

pattern = re.compile(r"(<\s*[^<>]+\s*>)")

# the above character set eliminates the given tag if it contains a pipe, tilde,a backslash, a question mark, a dollar sign or angle brackets that are nested within a html tag for example: <tag width="$2"> will be skipped as a valid tag as it contains the invalid tag dollar sign.

  
#replacing the tag elements is more robust than grabbing the text between the tags since tags are usually nested. i.e. <body> <div><p>hello</p></div></body>

matches = pattern.finditer(query_string_to_replace)

print("__________________________")
print("Matched tags are the following: ")
print("____________________________________")
for match in matches:
	#print(match.span())# get only the tuple span
	print(match.group(1))
#print(query_string_to_replace[35:37])
#[print(query_string_to_replace[50:52])

# step 2: we need to substitute all the tags with a space so that we'll remain with the web content. 

# substitute our matched pattern with a space.
trimmed_tags_var = pattern.sub(r' ',query_string_to_replace)

print("_________________________________")
print(" our trimmed original  string is:  ")
print("__________________________________")
print(trimmed_tags_var)
# step 3: we can iterate through the text using yield statements and ensure there are being saved to a set. A set contains only unique words.