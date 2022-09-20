from PIL import Image, ImageDraw, ImageSequence, ImageFont
import io

print(r"""          $$\  $$$$$$\                          $$\                           $$\     
          \__|$$  __$$\          $$\            $$ |                          $$ |    
 $$$$$$\  $$\ $$ /  \__|         $$ |         $$$$$$\    $$$$$$\  $$\   $$\ $$$$$$\   
$$  __$$\ $$ |$$$$\           $$$$$$$$\       \_$$  _|  $$  __$$\ \$$\ $$  |\_$$  _|  
$$ /  $$ |$$ |$$  _|          \__$$  __|        $$ |    $$$$$$$$ | \$$$$  /   $$ |    
$$ |  $$ |$$ |$$ |               $$ |           $$ |$$\ $$   ____| $$  $$<    $$ |$$\ 
\$$$$$$$ |$$ |$$ |               \__|           \$$$$  |\$$$$$$$\ $$  /\$$\   \$$$$  |
 \____$$ |\__|\__|                               \____/  \_______|\__/  \__|   \____/ 
$$\   $$ |                                                                            
\$$$$$$  |                                                                            
 \______/                                                                             """)

usertxt = input("Enter Your Text! ")
sizeoftext = input("text size ")
userimg = input("image.gif ")

fnt = ImageFont.truetype("Anton-Regular.ttf", int(sizeoftext))

im = Image.open(userimg)

frames = []


for frame in ImageSequence.Iterator(im):
	frame = frame.convert('RGBA')
	d = ImageDraw.Draw(frame)
	d.text((10,150), usertxt, "#ffffff", font=fnt, stroke_width=2, stroke_fill="#000000")
	del d
	
	b = io.BytesIO()
	frame.save(b, format="GIF")
	frame = Image.open(b)
	
	frames.append(frame)

frames[0].save('out.gif', save_all=True, append_images=frames[1:])