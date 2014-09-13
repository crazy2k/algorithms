def rotate_90(img):
    new_img = [range(len(img)) for x in range(len(img))]
    for i in range(len(img)):
        for j in range(len(img)):
            ir = len(img) - 1 - j
            jr = i
            new_img[ir][jr] = img[i][j]
