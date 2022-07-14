from PIL import Image as image_handler
from PIL.Image import Image

class GeneratorHelper:
    def __init__(self) -> None:
        pass

    def open_image(self, path:str) -> Image:
        return image_handler.open(path).convert("RGBA")


    def bulk_open_images(self, paths_list:list[str]) -> list[Image]:
        return [self.open_image(f) for f in paths_list]

    
    def merge_layers(self, layers:list[Image]) -> 'Image|None':
        #make sure that all images sizes are the same
        if len(set(map(lambda l: l.size, layers))) != 1:
            print("Images sizes is not the same!")
            return
        
        #start combining
        img = layers[0]
        for i in range(1, len(layers)):
            img = image_handler.alpha_composite(img, layers[i])

        return img

    
    def create_sprite_sheet(self, frames:list[Image]) -> Image:
        #make sure that all images sizes are the same
        if len(set(map(lambda l: l.size, frames))) != 1:
            print("Images sizes is not the same!")
            return

        #create transparent image
        sprite_width = frames[0].width * len(frames)
        sprite_height = frames[0].height * 2
        sprite = image_handler.new("RGBA", (frames[0].width * len)) 




