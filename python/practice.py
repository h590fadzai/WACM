from urllib.request import urlopen

# Link to website api
link = 'https://wttr.in/Perth?A'

# Gets url and opens it
wget = urlopen(link)

# Reads whats on website in clear text
webtext = wget.read()

# Print it to the screen
print(webtext.decode('utf-8'))
