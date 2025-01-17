from hindi_tokenizer import HindiTokenizer

def main():
    try:
        print("Starting Hindi BPE Tokenizer...")
        tokenizer = HindiTokenizer('hindi_text (1)')
        
    except FileNotFoundError:
        print("File not found. Please ensure the file exists in the current directory.")

if __name__ == "__main__":
    main() 