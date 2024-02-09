def replace_multiple_bot_words(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        paragraphs = file.read().split('\n')
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for idx, paragraph in enumerate(paragraphs, start=1):
            words = paragraph.split()
            found_human = False
            bot_count = 0

            i = 0
            while i < len(words):
                current_word = words[i].lower()

                if current_word == 'human:':
                    found_human = True
                    bot_count = 0
                elif current_word == 'bot:' and found_human:
                    if bot_count > 0:
                        words[i] = ''
                    else:
                        bot_count += 1
                i += 1

            updated_paragraph = ' '.join(words)
            output_file.write(updated_paragraph)

input_file_path = 'D://fromtech//data1_cef_november.txt'
output_file_path = 'D://fromtech//data2_cef_november.txt'
replace_multiple_bot_words(input_file_path, output_file_path)
