def generate_phrases(list1, list2):
    phrases = []
    for phrase in list1:
        for phrase2 in list2:
            phrases.append(f"{phrase} {phrase2}")
    return phrases


def generate_phrases2(list1, list2, list3):
    phrases = []
    for phrase in list1:
        for phrase2 in list2:
            for phrase3 in list3:
                phrases.append(f"{phrase} {phrase2} {phrase3}")
    return phrases


def load_from_file(filename):
    citys = []
    with open(filename, encoding='utf-8') as fh:
        for line in fh:
            clean_line = line.replace("\n", "")
            citys.append(f'{clean_line}')
    return citys


def write_list_to_file(input_list, filename):
    with open(filename, 'w', encoding='utf-8') as fh:
        for phrase in input_list:
            fh.write(f"{phrase}\n")


def load_and_generate():
    full_list = []
    frazy = load_from_file("Input/frazy.txt")
    brandy = load_from_file("Input/brandy.txt")
    for fraza in frazy:
        for brand in brandy:
            full_list.append(f'{brand} {fraza}')
            full_list.append(f'{fraza} {brand}')

        write_list_to_file(full_list, f"Output/monitoring.txt")


def load_and_generate2():
    full_list = []
    urls = load_from_file("urle.txt")
    for url in urls:
        full_list.append(f'{url}')
        for i in range(10):
            full_list.append(f'{url}/{i}')

    write_list_to_file(full_list, "lista_lista.txt")


# load_and_generate()
