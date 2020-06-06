# Image_Manipulation

## For watermarking with image and text (text is optional)  :

  Open a `python` terminal then use below commands
  
  ` from Main import watermark `  <br/>
  ` watermark(input_image_path, output_image_path, watermark_image_path,position_logo,text,color,text_size,                       text_position) `
   
  ex- <br/>
   
  `watermark('gcs-banner.png',                      # Base Image    <br/>
             'watermarked_image_output.jpg',       # Output Image     <br/>
             'invide.png',                         # Watermark Image    <br/>
             'tr',                                 # Watermark Image Position   <br/>  
             text='Invide',                        # Warermark Text (optional)    <br/> 
             color ='white',                       # Watermark Text Color (optional)    <br/>
             text_size=55,                         # Warermark Text Size (optional)    <br/> 
             text_position='b'                     # Watermark Text Position with respect to Watermark Image (optional)     <br/>
             )  `

## For watermarking with text only  :

  Open a `python` terminal then below commands
  
    ` from Main import watermark `
  
    ` watermark_with_text(input_image_path,output_image_path,text,text_position,color',text_size) `
  
  ex-
  
    ` watermark_with_text('gcs-banner.png',               # Base Image
    
                       'watermarked_text_output.png',   # Output Image
                       
                       'Invide',                        # Warermark Text
                       
                        'bc',                           # Watermark Text Position
                        
                       text_size=200,                   # Warermark Text Size (optional)
                       
                        color='white') `
                       
## Positioning parameter for watermark function :

  For Watermark Image                                      For Watermark Text 
  
  ` tl - Top Left Corner                                   b - Below Watermark Image
  
    tc - Top Center                                        r - On Right Of Watermark Image
    
    tr - Top Right
    
    cl - Center Left
    
    c  - Center 
    
    cr - Center Right
    
    bl - Bottom Left
    
    bc - Bottom Center
    
    br - Bottom Right `
    
 
## Positioning parameter for watermark_with_text function :

    ` tl - Top Left Corner      
    
    tc - Top Center
    
    tr - Top Right
    
    cl - Center Left
    
    c  - Center
    
    cr - Center Right
    
    bl - Bottom Left
    
    bc - Bottom Center
    
    br - Bottom Right `

   


