from PIL import Image, ImageDraw, ImageFont

class MemeEngine():

    def make_meme(self, img_path, text, author, width) -> str:
        """Create a Meme  With an inspiring Quote

        Arguments:
            img_path {str} -- the file location for the input image.
            text {str} -- the desired quote for the output meme.
            author {str} -- author of the quote.
            width {int} -- The pixel width value. Default=500.
        Returns:
            str -- the file path to the output image.
        """
        try:
            with Image.open(img_path) as im:
                (img_width, img_height) = im.width, im.height
                height = int (500 *(img_height/img_width))
                resized_image = im.resize((width, height))
                # make a blank image for the text, initialized to transparent text color
                resized_image = resized_image.convert('RGBA')
                txt = Image.new('RGBA', resized_image.size, (255, 255, 255, 0))
                # get a font
                fnt = ImageFont.truetype('fonts/LilitaOne-Regular.ttf', 30)
                d = ImageDraw.Draw(txt)
                # draw text, full opacity
                d.text((10, 10), text+author, font=fnt, fill=(255, 255, 255, 128))
                out = Image.alpha_composite(resized_image, txt)
                out.show()
                out.save('tmp/meme.png')
        except IOError:
            pass