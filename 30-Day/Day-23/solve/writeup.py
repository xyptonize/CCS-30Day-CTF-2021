from PIL import Image


def cropImg(img):
    images = []
    height, width = img.size
    # 1
    left = 0
    top = 0
    right = width / 2
    bottom = height / 2
    img1 = img.crop((left, top, right, bottom))
    # 2
    left = width / 2
    top = 0
    right = width
    bottom = height / 2
    img2 = img.crop((left, top, right, bottom))

    # 3
    left = 0
    top = height / 2
    right = width / 2
    bottom = height
    img3 = img.crop((left, top, right, bottom))
    # 4
    left = width / 2
    top = height / 2
    right = width
    bottom = height
    img4 = img.crop((left, top, right, bottom))
    images.append(img1)
    images.append(img2)
    images.append(img3)
    images.append(img4)
    return images


if __name__ == "__main__":
    index = 1
    with Image.open("images/ctf.jpg") as img:
        img4 = cropImg(img)
        for i in range(len(img4)):

            img16 = cropImg(img4[i])

            for k in range(len(img16)):
                img64 = cropImg(img16[k])
                for j in range(len(img64)):
                    # img.save("images/{}".format(index))
                    img64[j].save("images/{}.jpg".format(index))

                    index += 1
