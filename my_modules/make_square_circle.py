"""
This Module i made with the intention of make a square and a circle
inside the square image, i will generate this by passing the 
Side of Square, 
Radius of the Circle, border width of the circle

"""

import datetime

from pathlib import Path
from PIL import Image, ImageDraw


def now_time_india() -> int:
    """
    This will return current timestamp as a integer value
    """
    now_time = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    )
    now_time = now_time.timestamp()
    return int(now_time)


def make_square_image(
    side: int = 1024,
    color: str | int | tuple[int, int, int] = (255, 255, 255),
):

    im = Image.new("RGBA", (side, side), color)
    return im


def make_square_circle_image(
    side: int = 1024,
    bg_color: str | int | tuple[int, int, int] = (255, 255, 255),
    circle_radius: int = 500,
    circle_fill: str | int | tuple[int, int, int] = (0, 255, 0),
    circle_outline: str | int | tuple[int, int, int] = (0, 0, 255),
    outline_width: int = 10,
) -> Path | None:
    """
    i will call this funciton which will save the image
    and then it will return the iamge locaion and it will i
    use in others places
    """

    im = Image.new("RGBA", [side, side], bg_color)
    draw = ImageDraw.Draw(im)
    x1, x2 = im.size[0] // 2, im.size[1] // 2
    center_point = (x1, x2)

    # Main part to draw the circle
    draw.circle(
        center_point,
        circle_radius,
        circle_fill,
        circle_outline,
        outline_width,
    )
    im_name = f"{now_time_india()}_image.png"
    im_location = Path("static") / "image_generate" / im_name
    im_location.parent.mkdir(parents=True, exist_ok=True)

    try:
        im.save(im_location)
        return im_location
    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":

    red_im = make_square_circle_image()
    print(str(red_im))
