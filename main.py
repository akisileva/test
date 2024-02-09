import pandas as pd
import csv
import re
import json

def process_dialogue(dialogue): #чтоб начиналось с human: и кончалось bot:
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

def replace_multiple_bot_words(processed_dialogues): #несколько bot: подряд
    paragraphs = processed_dialogues.split('\n')
    updated_paragraphs = []
    for paragraph in paragraphs:
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
        updated_paragraphs.append(updated_paragraph)

    return '\n'.join(updated_paragraphs)


    
    

def create_jsonl_file(dialogs, output_jsonl_file):
    jsonl_data = []
    for i in range(0, len(dialogs), 2):
        human_input = dialogs[i][1].strip()
        bot_output = dialogs[i + 1][1].strip() if i + 1 < len(dialogs) else ''
        jsonl_data.append({"input": human_input, "output": bot_output})

    with open(output_jsonl_file, 'w', encoding='utf-8') as jsonl_file:
        for item in jsonl_data:
            json.dump(item, jsonl_file, ensure_ascii=False)
            jsonl_file.write('\n')

def main(input_csv):
    col_names = ['msisdn', 'start_time', 'duration', 'bot_duration', 'reg_num', 'fio', 'endpoint_mark',
                 'status_mark', 'verification_mark', 'objection_mark', 'zapis_of_comment', 'call_transcript',
                 'call_record', 'output_log', 'robot_detected', 'status', 'virified', 'recall_count', 'sum',
                 'client_id', 'smart_dialogs_uid', 'new_call_record', 'api_count', 'api_result', 'call_uid',
                 'request_from_handler', 'curl_api_count', 'manager', 'virtual_group', 'time_zone', 'flag',
                 'flag_reserv', 'script', 'uuid', 'sex', 'call_start_time', 'asr_duration', 'secretary',
                 'SD req', 'need_check_birthdate', 'attempt', 'type_call', 'voice_name', 'ringing_duration',
                 'ringing_d']

    df = pd.read_csv(input_csv, names=col_names, skiprows=2, delimiter=';', decimal=',')
    df.columns = df.columns.str.strip()
#удаляем из csv ненужные строки
    df = df[(df.endpoint_mark != 'Автоответчик') & (df.endpoint_mark != 'Недозвон')]
    df = df[(df.status_mark != 'Автоответчик') & (df.status_mark != 'Недозвон')]

#чтоб начиналось с human: и кончалось bot:
    processed_dialogues = []
    
    for dialogue in df['call_transcript']:
        print(dialogue)
        processed_dialogues.append(process_dialogue(dialogue))
        
#несколько bot: подряд
    replaced_text = replace_multiple_bot_words('\n'.join(processed_dialogues))
    
    symbols_to_replace = ['"', '»', '«']
    for symbol in symbols_to_replace:
            replaced_text = replaced_text.replace(symbol, "'")
# cоздание jsonl 
    dialog_pattern = re.compile(r'(human|bot): (.+?)(?=(?:human|bot):|$)')
    dialogs = dialog_pattern.findall(replaced_text)
    output_jsonl_file = 'output_dialogs.jsonl'
    create_jsonl_file(dialogs, output_jsonl_file)

if __name__ == "__main__":
    input_csv = 'D://fromtech//cef_december//CEF_TheRest_2.0_december.csv' 
    main(input_csv)