import wikipedia

result = wikipedia.page("Python (programming language)")
print("Title:", result.title)
print("Summary:", result.summary)
print("URL:", result.url)