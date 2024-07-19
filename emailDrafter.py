import docx
print(docx.__version__)


def write_my_email(path, replacements, output_path):

    #Load Document
    template = Document(path)

    for paragraph in template.paragraphs:
        for key, value in replacements.items():
            if key in pragraph.text:
                paragraph.text = paragraph.text.replace(key, value)

    template.save(output_path)
