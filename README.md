# CIP26_FinalPJ
Code in Place 2026 final project - A document sanitizer 

This is my final project for _Code in Place 2026_.

It is a python programme for running a "find and replace" operation over a text file so that potentially sensitive or confidential information in the document (think legal contracts or commercial documents) can be replaced by generic <placeholders>.

The key:value pairs used to redact a particular document are saved to disk as a JSON file so that at a later date, another "find and replace" operation can be ran to revert the <placeholders> to their original non-redacted form.

This can be useful if you wish to translate the document to another language, or perhaps summarize it using a LLM. If you instruct the LLM to leave the <placeholders> untranslated (eg. "Leave the word strings placed in angle brackets <> untranslated").
