# Extract Title

def extract_title(markdown):
    if markdown is None or markdown == "":
        raise ValueError("Markdown text cannot be empty.")
    
    lines = markdown.split("\n")

    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    
    raise ValueError("No H1 header found in markdown")