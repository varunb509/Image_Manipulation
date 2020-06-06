#!/usr/bin/env python
# coding: utf-8



from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def watermark(
              input_image_path,
              output_image_path,
              watermark_image_path,
              position_logo,
              text='',
              color ='black',
              text_size=40,
              text_position='r'
              ):
    
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width_base, height_base = base_image.size
    width_water, height_water = watermark.size
    
    
    transparent = Image.new('RGB', (width_base, height_base))
    
    transparent.paste(base_image, (0,0))
    bias_width=int(width_base*.05)
    bias_height=int(height_base*.05)
    if bias_height>50:
        bias_height=50
    if bias_width>50:
        bias_width=50
    
    mapper_logo_position={'tl':(bias_width,bias_height),
            'tc':(width_base//2-width_water//2,bias_height),
            'tr':(width_base-width_water-bias_width,bias_height),
            'cl':(bias_width,height_base//2-height_water),
            'cr':(width_base-width_water-bias_width,height_base//2-height_water),
            'c':(width_base//2-width_water//2,height_base//2-height_water),
            'bl':(bias_width,height_base-height_water-bias_height),
            'bc':(width_base//2-width_water//2,height_base-height_water-bias_height),
            'br':(width_base-width_water-bias_width,height_base-height_water-bias_height)}

    transparent.paste(watermark, mapper_logo_position[position_logo], mask=watermark)
    drawing = ImageDraw.Draw(transparent)
    
    font = ImageFont.truetype(r'Helvetica.ttf', text_size)
    textwidth, textheight = drawing.textsize(text, font)
    mapper_text_position={
        'r':(mapper_logo_position[position_logo][0]+width_water+bias_width//2,mapper_logo_position[position_logo][1]+height_water//2-textheight//2),
        'b':[mapper_logo_position[position_logo][0]+width_water//2-textwidth//2,mapper_logo_position[position_logo][1]+height_water+bias_width//2]
    }
    position_text=mapper_text_position[text_position]
    if(textwidth<width_water):
        mapper_text_position['b'][0]=mapper_logo_position[position_logo][0]+(width_water-textwidth)//2
    drawing.text(position_text, text, fill=color,font=font)   
    transparent.show()
    transparent.save(output_image_path)

def watermark_with_text(input_image_path,
                        output_image_path,
                        text,
                        text_position,
                        color='black',
                        text_size=40,
                        
                       ):
    base_image = Image.open(input_image_path) 
    width_base, height_base = base_image.size 
 
    drawing = ImageDraw.Draw(base_image)
    bias_width=int(width_base*.05)
    bias_height=int(height_base*.05)
    if bias_height>50:
        bias_height=50
    if bias_width>50:
        bias_width=50
    
    font = ImageFont.truetype('Helvetica.ttf', text_size)
    textwidth, textheight = drawing.textsize(text, font)
    mapper_position={'tl':(bias_width,bias_height),
            'tc':(width_base//2-textwidth//2,bias_height),
            'tr':(width_base-textwidth-bias_width,bias_height),
            'cl':(bias_width,height_base//2-textheight),
            'cr':(width_base-textwidth-bias_width,height_base//2-textheight),
            'c':(width_base//2-textwidth//2,height_base//2-textheight),
            'bl':(bias_width,height_base-textheight-bias_height),
            'bc':(width_base//2-textwidth//2,height_base-textheight-bias_height),
            'br':(width_base-textwidth-bias_width,height_base-textheight-bias_height)}
    
    
    drawing.text(mapper_position[text_position], text,fill=color, font=font) 
    base_image.show()
    base_image.save(output_image_path)

if __name__ == '__main__':
    watermark('gcs-banner.png',              # Base Image
              'watermarked_image_output.jpg',       # Output Image Name
              'invide.png',                 # Watermark Image
              'tr', 
              text='Invide',
              color ='white',
              text_size=55,
              text_position='b'
              )      

    watermark_with_text('gcs-banner.png',
                       'watermarked_text_output.png',
                       'Invide',
                        'bc',
                       text_size=200,color='white')



