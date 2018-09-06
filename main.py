import ChannelHandler as ch

im = [100, 200, 30, 40,
123, 145, 6, 90,
0, 255, 14, 60,
100, 200, 30, 40]

h = ch.ChannelHandler(4, 4)
h.low_brightness(im, 200)
h.filter_by_median(im)
h.filter_by_harmonic_mean(im)
h.get_histogram(im)
h.get_negative(im)

