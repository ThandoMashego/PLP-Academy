with open("poem.txt", "r") as file : 
    content = file.read()
    print(content)

# Example:
with open("poem1.txt", "w") as file: 
    file.write("""my kitty is proud 
my kitty is loud 
He's fur is silky
He's cheeks are milky""")
    print(file)

