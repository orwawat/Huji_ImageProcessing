from sol1 import *

# EQUALIZE TEST:
# res = histogram_equalize(read_image("tests/external/jerusalem.jpg", 1))
# plt.imshow(res[0], cmap=plt.cm.gray)
# plt.show()
# plt.plot(res[1])
# plt.plot(res[2],'r')
# plt.show()
#



# # QUANTIZE TEST:
# res1 = quantize(read_image("tests/external/monkey.jpg", 2), 20, 10)
# res2 = quantize(read_image("tests/external/monkey.jpg", 1), 4, 5)
# #
# Y = (rgb2yiq(res1[0])[:,:,0])
# hist_orig, bin_edges = np.histogram(Y, MAX_PIX_VAL + 1)
# c = np.count_nonzero(hist_orig)
# print(c)
# f = plt.figure()
# f.add_subplot(2, 3, 1)
# plt.imshow(read_image("tests/external/monkey.jpg", 2), cmap=plt.cm.gray)
# f.add_subplot(2, 3, 2)
# plt.imshow(res1[0], cmap=plt.cm.gray)
# f.add_subplot(2, 3, 3)
# plt.plot(res1[1])
# f.add_subplot(2, 3, 4)
# plt.imshow(read_image("tests/external/monkey.jpg", 1), cmap=plt.cm.gray)
# f.add_subplot(2, 3, 5)
# plt.imshow(res2[0], cmap=plt.cm.gray)
# f.add_subplot(2, 3, 6)
# plt.plot(res2[1])
# plt.show()
# #



# QUANTIZE_RGB TEST:
res = quantize_rgb(read_image("tests/external/jerusalem.jpg", 2), 4, 5)
f = plt.figure()
a = f.add_subplot(1, 2, 1)
a.set_title('ORIGINAL')
plt.imshow(read_image("tests/external/jerusalem.jpg", 2))
b = f.add_subplot(1, 2, 2)
b.set_title('quantize_rgb with 4 quants')
plt.imshow(res[0])
plt.show()
plt.plot(res[1])
plt.show()