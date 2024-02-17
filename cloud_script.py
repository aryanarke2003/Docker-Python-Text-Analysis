import os
import socket
from collections import Counter

# Function to read text files and count words
def count_words(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        text = file.read()
        words = text.split()
        return len(words)

# Function to find top words in IF.txt
def top_words(file_path, n=3):
    with open(file_path, 'r', encoding='latin-1') as file:
        text = file.read()
        words = text.split()
        word_counts = Counter(words)
        return word_counts.most_common(n)

# Main function
def main():
    data_dir = '/home/data'
    output_file_path = '/home/output/result.txt'

    # Initialize variables
    total_word_count = 0
    file_info = []
    top_words_list = []

    # Filter text files and count words
    for file_name in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file_name)
        if file_name.endswith('.txt'):  # Process only text files
            word_count = count_words(file_path)
            total_word_count += word_count
            file_info.append((file_name, word_count))
            if file_name == 'IF.txt':  # Process top words for IF.txt
                top_words_list = top_words(file_path)

    # Get IP address
    ip_address = socket.gethostbyname(socket.gethostname())

    # Write output to text file
    with open(output_file_path, 'w') as output_file:
        output_file.write('File Name\tWord Count\n')
        for file_name, word_count in file_info:
            output_file.write(f'{file_name}\t{word_count}\n')
        output_file.write(f'Total word count: {total_word_count}\n')
        output_file.write(f'Top 3 words in IF.txt:\n')
        for word, count in top_words_list:
            output_file.write(f'{word}: {count}\n')
        output_file.write(f'IP Address: {ip_address}\n')

    # Print output to console
    with open(output_file_path, 'r') as result_file:
        print(result_file.read())

if __name__ == "__main__":
    main()
