"""Create an inspiring meme."""

from PIL import Image, ImageDraw, ImageFont
import os
import uuid


class MemeEngine:
    """Takes image path and quote and makes a inspiring meme."""

    def __init__(self, output_dirName):
        """Create output director for the meme."""
        self.output_dirName = output_dirName
        # Create target Directory if don't exist
        if not os.path.exists(output_dirName):
            os.mkdir(output_dirName)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a Meme  With an inspiring Quote.

        Arguments:
            img_path {str} -- the file location for the input image.
            text {str} -- the desired quote for the output meme.
            author {str} -- author of the quote.
            width {int} -- The pixel width value. Default=500.
        Returns:
            str -- the file path to the output image.
        """
        path = self.output_dirName + '/' + str(uuid.uuid1()) + '.png'
        print(img_path, text, author)
        try:
            with Image.open(img_path) as im:
                (img_width, img_height) = im.width, im.height
                height = int(width * (img_height / img_width))
                resized_image = im.resize((width, height))
                # make a blank image for the text, initialized to transparent text color
                resized_image = resized_image.convert('RGBA')
                txt = Image.new('RGBA', resized_image.size, (255, 255, 255, 0))
                # get a font
                fnt = ImageFont.truetype('fonts/LilitaOne-Regular.ttf', 20)
                d = ImageDraw.Draw(txt)
                # draw text, full opacity
                d.text((20, 20), text + ' - ' + author, font=fnt, fill=(0, 0, 0, 255))
                out = Image.alpha_composite(resized_image, txt)
                # out.show()
                out.save(path)
        except IOError:
            pass
        return path
