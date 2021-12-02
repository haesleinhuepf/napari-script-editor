

def write_text_file(filename, text):
    with open(filename, 'w') as f:
        f.write(text)

def read_text_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    return "".join(lines)
