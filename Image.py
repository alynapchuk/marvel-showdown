from PIL import Image
from images2gif import writeGif

images = [Image.open('%s.png' % i) for i in range(12)]
durations = ['1.5']*len(images)
writeGif('my.gif' ,images, durations=durations)