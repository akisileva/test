with open('data2_cef_november.txt', 'r', encoding='utf-8') as file:
    text = file.read()

symbols_to_replace = ['"', '»', '«']

for symbol in symbols_to_replace:
    text = text.replace(symbol, "'")

with open('data2_cef_november.txt', 'w', encoding='utf-8') as file:
    file.write(text)