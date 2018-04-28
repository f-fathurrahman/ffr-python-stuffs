from pptx import Presentation

prs = Presentation()

# Create title slide
title_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(title_slide_layout)

title = slide.shapes.title
subtitle = slide.placeholders[1]

title.text = "A Presentation Made via Python"
subtitle.text = "Fadjar Fathurrahman"

# layout
slide = prs.slides.add_slide( prs.slide_layouts[1] )

shapes = slide.shapes
title_shape = shapes.title
body_shape = shapes.placeholders[1]

title_shape.text = "Test adding a bullet slide"
tf = body_shape.text_frame
tf.text = "First item"

prs.save("01_hello.pptx")
