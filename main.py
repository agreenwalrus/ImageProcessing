from ImageHelper import ImageHelper
import matplotlib.pyplot as plt
import numpy as np


ih = ImageHelper("./source/bobaka.jpg")
#ih.show_histogram("Source image")
ih.save_image("new")
