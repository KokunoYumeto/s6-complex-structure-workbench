from pathlib import Path
import fitz

OUT = Path('/workspace/scratch/9fcd229a9ed4/base/S6_PUBLISH_c3_foundations_sources')
doc = fitz.open(OUT / 'S6_SERIES_PUBLISH_Inoue1974_volume.pdf')
for printed in (274, 275, 277, 279):
    page = doc[printed + 6]
    path = OUT / f'S6_SERIES_PUBLISH_Inoue1974_p{printed}.png'
    page.get_pixmap(matrix=fitz.Matrix(1.6, 1.6)).save(path)
    print(path)
