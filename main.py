from pptx import Presentation

def main():
    prs = Presentation("/Users/pioppoido/Desktop/sample_bf.pptx")
    
    for i in range(1, int(len(prs.slides) / 2)):
        delete_slides(prs, i)

    prs.save("/Users/pioppoido/Desktop/sample_af.pptx")

def delete_slides(presentation, index):
        xml_slides = presentation.slides._sldIdLst
        slides = list(xml_slides)
        xml_slides.remove(slides[index])

if __name__ == "__main__":
    main()