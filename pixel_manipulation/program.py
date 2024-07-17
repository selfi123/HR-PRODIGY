from PIL import Image,ImageEnhance
import easygui
import random

def shuffle_pixels(img, key):
    width,height=img.size
    pixels=list(img.getdata())
    
    random.seed(key)
    shuffled_positions=list(range(len(pixels)))
    random.shuffle(shuffled_positions)
    
    shuffled_img=Image.new('RGB',(width,height))
    for i,j in enumerate(shuffled_positions):
        shuffled_img.putpixel((j%width,j//width),pixels[i])
    
    return shuffled_img

def unshuffle_pixels(img,key):
    width,height=img.size
    pixels=list(img.getdata())
    
    random.seed(key)
    shuffled_positions=list(range(len(pixels)))
    random.shuffle(shuffled_positions)
    
    unshuffled_img=Image.new('RGB',(width,height))
    for i,j in enumerate(shuffled_positions):
        unshuffled_img.putpixel((i%width,i//width),pixels[j])
    
    return unshuffled_img

def adjust_saturation(image, factor):
   
    enhancer = ImageEnhance.Color(image)
    adjusted_image = enhancer.enhance(factor)
    return adjusted_image

print("Upload your Image.....")
file_path=easygui.fileopenbox()
if file_path:
    try:
    
        img=Image.open(file_path)
        print(img.size)
        if img.mode!='RGB':
            img=img.convert('RGB')
        print("Uploading Completed...")
        print("\n1. ENCRYPT THE IMAGE\n2. DECRYPT THE IMAGE\n")
        try:
            option=int(input("Choose from above: "))
            if option==1:
                key=int(input("Enter the encryption key: "))
                shuffled_img=shuffle_pixels(img, key)
                shuffled_img.show()
                shuffled_img.save("encrypted_image.jpg")
                print("Image encrypted and saved as 'encrypted_image.jpg'.")
            elif option == 2:
                key=int(input("Enter the decryption key: "))
                unshuffled_img=unshuffle_pixels(img, key)
                unshuffled_img.show()
                unshuffled_img.save("decrypted_image.jpg")
                print("Image decrypted and saved as 'decrypted_image.jpg'.")
            else:
                print("Invalid option. Exiting.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the option and key.")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("No file selected.")
