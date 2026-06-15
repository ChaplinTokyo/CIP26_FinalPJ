"""
IDEA:  Make an anonymiser for a contract text file
so uploading it to a LLM for translating, summarizing,
etc. will not put you at risk of leaking confidential
or personal information.
IDEA2:  Use a question and answer format to make
a change from:to dictionary of terms such as
[licensor_companyname],[licensor_address],[licensor_rep_name],
[licensee_companyname], [licensee_address], [licensee_rep_name],
[property_title], [author_name], [author_name2], [author_name],
[optionfee_amt], [purchase_or_licensefee_amt], which
should be saved to a file so the anonymisation can
be reverted locally later on after translation or
summarization by LLM chatbot.
---
MILESTONE 1: start with a text file anonymizer, rather than an MS-Word one
(MILESTONE 2: Add function to repopulate the processed file with redacted strings returned to placeholders)
"""

import json
import os
print(f"Working directory: {os.getcwd()}")

def main():
    # prompt file name from user and read it in and print to terminal so user can identify parts to anonymize
    print("")
    print("")
    print("**********************************")
    print("*       DOCUMENT SANITIZER       *")
    print("**********************************")
    print("")
    print("")
    print("- Find and remove sensitive information from plain text and markdown files (example: contracts).")
    print("- Just to be on the safe side, why not anonymize documents before you feed them to LLMs?")
    print("")
    print("")
    print("")
    file_name = input("Enter name of the file to open (or hit return to open 'sample_literaryoption_contract.md'): ") or "sample_literaryoption_contract.md"
    open_file_and_print(file_name)
    word_pairs = input_anonymization_pairs()
    print(word_pairs)

    # replace words in line using key and value in word_pairs
    with open(file_name, "r") as in_file, open("redacted_result.md", "w") as out_file:
        print(f"About to open: '{file_name}' | Length: {len(file_name)} | Repr: {repr(file_name)}") # test command to see whether files are being opened correctly
        for line in in_file:
            for o_word, n_word in word_pairs.items():
                line = line.replace(o_word, n_word)
            out_file.write(line)
            print(line, end='') # end='' prevents double newlines since line already has '\n'
    print("<<<<<<<<<<<<<<<<<< end of sanitized document >>>>>>>>>>>>>>>>>>")
    print(f"(Output file size: {os.path.getsize('redacted_result.md')} bytes)")      # check whether anything was written to file
    print("")
    print("")
    print("- Sanitized file has been written to disk as 'redacted_result.md'")
    print("- Sanitization word pairs saved to disk as 'word_pairs.json'")  # let user know that the word pairs have been written to disk
    print("")
    print("END OF RUN")

# helper function to ask user to input key:value pairs for strings needing to be anonymized, with the placeholders to use
def input_anonymization_pairs():
    word_pairs = {}
# instruct user to maximize the terminal to be able to see the contract that needs to be redacted
    print("<<<<<<<<<<<<<<<<<<<<<< end of document >>>>>>>>>>>>>>>>>>>>>>")
    print("")
    print("")
    print("Your file has been printed to Terminal.")
    print("")
    print("Input your 'find and replace' word pairs below, by copying & pasting or typing them in. ")
    print("If document is long, you will find it much easier to open it up in a separate editor screen (copy & paste with 2 windows open!)")
    print("")
    while True:
        key = input("Type or paste strings you want to replace ('q' to finish): ")

        if key.lower() == 'q':
            break

        value = input(f"Enter the placeholder for '{key}': ")
        word_pairs[key] = value
        # save word pairs to json
        with open("word_pairs.json", "w") as f:
            json.dump(word_pairs, f)
    return word_pairs


# helper function to read in the requested file and print to terminal for user to identify what needs to be anonymized
def open_file_and_print(file_name):
    with open(file_name) as file:  # at the end of the with block, the file is automatically closed
        for line in file:
            line = line.strip() # this gets rid of the new line '\n' that gets attached to each line end
            print(line)
        print()

if __name__ == "__main__":
    main()
