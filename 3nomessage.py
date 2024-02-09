def process_dialogue(dialogue):

    utterances = dialogue.split(';')
    human_index = next((i for i, utterance in enumerate(utterances) if utterance.strip().startswith('human')), None)
    if human_index is None:
        return dialogue.strip()

    if human_index != 0:
        utterances = utterances[human_index:]
    for i in range(len(utterances) - 1, -1, -1):
        if utterances[i].strip().startswith('bot'):
            utterances = utterances[:i + 1]
            break

    processed_dialogue = '; '.join(utterances)
    return processed_dialogue.strip()

with open('data_cef_november.txt', 'r', encoding='utf-8') as file:
    dialogues = file.readlines()

processed_dialogues = [process_dialogue(dialogue) for dialogue in dialogues]

with open('data1_cef_november.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(processed_dialogues))