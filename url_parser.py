def extract_domain_extension(url):
    ind = url.index(".") # last dot
    return url[ind:]

def extract_website_name(url):
    start = url.index("//") + 2
    end = url.index(".")
    return url[start:end]

url = "https://exampleURL1.com"

print("Extension:", extract_domain_extension(url))
print("Website name:", extract_website_name(url))
