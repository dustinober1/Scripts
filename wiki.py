import wikipedia

wikipedia.set_lang("en")
page = wikipedia.page("George Washington")

with open("george_washington.txt", "w", encoding="utf-8") as f:
    f.write(page.content)
