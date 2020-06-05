#!/usr/bin/env python
# coding: utf-8



from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def watermark(
              input_image_path,
              output_image_path,
              watermark_image_path,
              text,
              position_logo,
              color = (3, 8, 12),
              text_size=40,
              text_position='r'
              ):
    
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width_base, height_base = base_image.size
    width_water, height_water = watermark.size
    
    
    transparent = Image.new('RGB', (width_base, height_base))
    
    transparent.paste(base_image, (0,0))
    bias_width=int(width_base*.04)
    bias_height=int(height_base*.04)
    if bias_height>40:
        bias_height=40
    if bias_width>40:
        bias_width=40
    
    mapper_logo_position={'tl':(bias_width,bias_height),
            'tc':(width_base//2-width_water//2,bias_height),
            'tr':(width_base-width_water-bias_width,bias_height),
            'c':(width_base//2-width_water//2,height_base//2-height_water),
            'bl':(bias_width,height_base-height_water-bias_height),
            'bc':(width_base//2-width_water//2,height_base-height_water-bias_height),
            'br':(width_base-width_water-bias_width,height_base-height_water-bias_height)}

    transparent.paste(watermark, mapper_logo_position[position_logo], mask=watermark)
    drawing = ImageDraw.Draw(transparent)
    
    font = ImageFont.truetype(r'Helvetica.ttf', text_size)
    textwidth, textheight = drawing.textsize(text, font)
    mapper_text_position={
        'r':(mapper_logo_position[position_logo][0]+width_water+bias_width//2,mapper_logo_position[position_logo][1]+textheight//4),
        'b':(mapper_logo_position[position_logo][0]-textwidth//2+bias_width//2,mapper_logo_position[position_logo][1]+height_water+bias_width//2)
    }
    position_text=mapper_text_position[text_position]
    drawing.text(position_text, text, fill=color,font=font)   # Currently using 'black' color for the text
    transparent.show()
    transparent.save(output_image_path)


if __name__ == '__main__':
   
    watermark('example.jpg',              # Base Image
              'example_output.jpg',       # Output Image Name
              'logo.png',                 # Watermark Image
              'Price Tag',                # Text To Use as Waterark
              'tc', 
              color = (3, 8, 12),
              text_size=40,
              text_position='r'
              )      




