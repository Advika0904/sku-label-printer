import os
from pdf2image import convert_from_path
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

def pdf_to_image_pdf(input_folder="labels", output_folder="output"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".pdf"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            print(f"Processing: {input_path}")

            # Convert PDF pages to images
            images = convert_from_path(input_path, dpi=1000)

            # Create a new PDF writer
            c = None

            for img in images:
                img_width, img_height = img.size  # keep original page size
                if c is None:
                    c = canvas.Canvas(output_path, pagesize=(img_width, img_height))

                c.setPageSize((img_width, img_height))
                c.drawImage(ImageReader(img), 0, 0, width=img_width, height=img_height)
                c.showPage()

            if c:
                c.save()
                print(f"Saved: {output_path}")

if __name__ == "__main__":
    pdf_to_image_pdf("labels", "output")
