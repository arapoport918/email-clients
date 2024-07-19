from docx import Document


def write_my_email(path, replacements, output_path):

    #Load Document
    template = Document(path)

    for paragraph in template.paragraphs:
        for key, value in replacements.items():
            if key in paragraph.text:
                paragraph.text = paragraph.text.replace(key, value)

    template.save(output_path)

path = "15DayTEMPLATE.docx"
replacements = {
    "CLIENT_NAME": "Allegra",
    "BRAND": "Some Brand Name"
    }
output_path = "yayThisWorkedBetter.docx"

write_my_email(path, replacements, output_path)
