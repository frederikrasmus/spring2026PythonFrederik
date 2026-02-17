import requests

#1
url = input('Please enter an url: ')
html = requests.get(url)

#with open('index.html', 'w') as f:
#    f.write(html.text)

# look for <link> tags in html
x = html.text.index('link')
# slice the string in 2 from the url
slice = html.text[x+11:]
#print(slice)
# find the end of the url
y = slice.index('"')
#print(y)
# slice the string in 2
sliced = slice[:y]
print(sliced)

# download css file
css = requests.get(sliced)
with open('style.css', 'w') as c:
    c.write(css.text)

# Change url to new stylesheet.
#html_css = html.text.split('<link href="')

# look for " sign in end of line
 

# look for img tags
