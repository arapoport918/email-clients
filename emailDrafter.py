from docx import Document


def write_my_email(path, replacements, output_path):

    #Load Document
    template = Document(path)

    for paragraph in template.paragraphs:
        for key, value in replacements.items():
            if key in paragraph.text:
                paragraph.text = paragraph.text.replace(key, value)

    template.save(output_path)

path15 = "15DayTEMPLATE.docx"
replacements15 = {
    "CLIENT_NAME": "Allegra",
    "BRAND": "Some Brand Name"
    }
output_path15 = "yayThisWorkedBetter.docx"

path60 = "60DayTEMPLATE.docx"
replacements60 = {
    "ADNAME": "Allegra",
    "CLIENT": "Brand for Testing",
    "DATE": "July 19th, 2024"
    }
output_path60 = "yayThisWorkedfor60.docx"

path100 = "100DayTEMPLATE.docx"
replacements100 = {
    "CLIENT_NAME": "Allegra's Famous Brand",
    "CLIENT_CONTACT_NAMES": "Bryce, Trea, Nick, Alec",
    "PROGRAM_TYPE": "affiliate"
    }
output_path100 = "yayThisWorkedfor100.docx"

write_my_email(path15, replacements15, output_path15)
write_my_email(path60, replacements60, output_path60)
write_my_email(path100, replacements100, output_path100)
