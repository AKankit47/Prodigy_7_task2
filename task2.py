from PIL import Image
import numpy as np
import os

def generate_random_mask(shape, key):
    np.random.seed(key)  # Seed the random generator with the key
    return np.random.randint(0, 256, size=shape, dtype=np.uint8)

def encrypt_image(input_path, output_path, key):
    
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist.")
        return

    try:
        # Open the image
        img = Image.open(input_path)
        img_array = np.array(img, dtype=np.uint8)

        print(f"Encrypting image of size {img_array.shape}...")
        # Generate a random mask
        mask = generate_random_mask(img_array.shape, key)

        # Apply the mask for encryption
        encrypted_array = np.bitwise_xor(img_array, mask)

        # Save the encrypted image
        encrypted_img = Image.fromarray(encrypted_array, mode=img.mode)
        encrypted_img.save(output_path)
        print(f"Encrypted image saved to {output_path}")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")


def decrypt_image(input_path, output_path, key):

    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist.")
        return

    try:
        # Open the encrypted image
        img = Image.open(input_path)
        img_array = np.array(img, dtype=np.uint8)

        print(f"Decrypting image of size {img_array.shape}...")
        # Generate the same random mask
        mask = generate_random_mask(img_array.shape, key)

        # Reverse the mask application for decryption
        decrypted_array = np.bitwise_xor(img_array, mask)

        # Save the decrypted image
        decrypted_img = Image.fromarray(decrypted_array, mode=img.mode)
        decrypted_img.save(output_path)
        print(f"Decrypted image saved to {output_path}")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")


if __name__ == "__main__":
    print("Image Encryption Tool")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        input_path = input("Enter the path to the image to encrypt: ").strip()
        output_path = input("Enter the path to save the encrypted image: ").strip()
        key = int(input("Enter the encryption key (integer): "))
        encrypt_image(input_path, output_path, key)

    elif choice == "2":
        input_path = input("Enter the path to the encrypted image: ").strip()
        output_path = input("Enter the path to save the decrypted image: ").strip()
        key = int(input("Enter the decryption key (must match encryption key): "))
        decrypt_image(input_path, output_path, key)

    else:
        print("Invalid choice. Please enter 1 or 2.")
