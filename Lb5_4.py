import random
def generate_filename(file_tag='.txt', filename_size=7):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters += [letter.upper() for letter in letters]
    
    filename = ''
    for i in range(filename_size):
        filename += ''.join(random.choice(letters))
    filename += file_tag
    return filename
print(generate_filename())