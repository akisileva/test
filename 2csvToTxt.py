import pandas as pd
import csv

with open('data2_cef_november.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')  
    df = pd.DataFrame(reader)
text_list = df['call_transcript'].tolist()

with open('data_cef_november.txt', 'w', encoding='utf-8') as txt_file:
    for text in text_list:
        txt_file.write(str(text) + '\n')