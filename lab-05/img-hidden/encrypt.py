import sys
from PIL import Image

def encode_image(image_path, message):
    # Open the image
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure image is in RGB mode
    width, height = img.size
    
    # Convert message to binary
    message += '\0'  # Add null terminator to mark end of message
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    
    # Check if image can hold the message
    if len(binary_message) > width * height * 3:
        raise ValueError("Message is too large for the image")
    
    data_index = 0
    # Create a new image to store the encoded data
    encoded_img = img.copy()
    
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))  # Get RGB values
            
            for color_channel in range(3):  # For R, G, B
                if data_index < len(binary_message):
                    # Replace LSB of pixel color with message bit
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1
            
            # Update pixel in the new image
            encoded_img.putpixel((col, row), tuple(pixel))
            
            # Stop if entire message is encoded
            if data_index >= len(binary_message):
                encoded_img.save('encoded_image.png')
                return
    
    # Save the encoded image if not already saved
    encoded_img.save('encoded_image.png')

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        return
    
    image_path = sys.argv[1]
    message = sys.argv[2]
    
    try:
        encode_image(image_path, message)
        print("Message encoded successfully. Saved as 'encoded_image.png'")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()