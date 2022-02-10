import webbrowser

from exif import Image
import matplotlib
import PIL

def run():
    print('run')

    #load image and put image data into variable
    img_path = './images/test3.jpg'
    with open(img_path, 'rb') as src:
        img = Image(src)
        print(src.name, img)
    image = PIL.Image.open(img_path)
    # image.show()

    #has or doenst have exif information
    with open(img_path, "rb") as src:
        img = Image(src)
        if img.has_exif:
            info = f" has the EXIF {img.exif_version}"
        else:
            info = "does not contain any EXIF information"
        print(f"Image {src.name}: {info}")

    image = PIL.Image.open(img_path)
    # image.show()

    #list all exif data
    print(sorted(img.list_all()))

    def decimal_coords(coords, ref):
        decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
        if ref == "S" or ref == "W":
            decimal_degrees = -decimal_degrees
        return decimal_degrees

    def image_coordinates(image_path):
        with open(img_path, 'rb') as src:
            img = Image(src)
        if img.has_exif:
            try:
                img.gps_longitude
                coords = (decimal_coords(img.gps_latitude,img.gps_latitude_ref),decimal_coords(img.gps_longitude,img.gps_longitude_ref))
            except AttributeError:
                print('No Coordinates')
        else:
            print('The Image has no EXIF information')
        print(f"Image {src.name}, OS Version:{img.get('software', 'Not Known')} ------")
        print(f"Was taken: {img.datetime_original}, and has coordinates:{coords}")

        return coords

    coords = image_coordinates(img_path)

    print(coords[0])
    print (coords[1])




    #print exif data
    print(img.datetime)


    print(img.gps_longitude_ref)

    webbrowser.open("https://www.google.com/maps/place/"+str(coords[0])+","+str(coords[1]))

if __name__ == '__main__':
    run()

