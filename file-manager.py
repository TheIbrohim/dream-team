def file_reader(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = file.readlines(file)
                for i in reader:
                    print(f"Berilgan misollar javoblari:{i}")
        except FileNotFoundError:
            print(f"Xatolik: Fayl topilmadi — {filename}")\

def write_file(filepath, text):
    with open(filepath, 'a', encoding='utf-8') as file:
        file.write(text + '\n')