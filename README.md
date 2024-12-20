# Prodigy_7_task2

### **1. Overview**
The tool uses **pixel-level encryption** to obscure image data. It operates in two stages:
1. **Encryption**: A random mask (generated using a key) is XORed with each pixel, effectively scrambling the image.
2. **Decryption**: The same mask is XORed again with the encrypted pixels, reversing the scrambling and restoring the original image.

---

### **2. Core Concepts**
#### a) **Random Mask Generation**
- A random mask is a matrix of random values with the same shape as the image.
- The `np.random.seed(key)` ensures reproducibility. For the same `key`, the exact random values are regenerated every time.
- This random mask serves as the encryption/decryption key.

#### b) **XOR Operation**
- XOR (`^` or `np.bitwise_xor`) is a reversible binary operation.
- When XOR is applied twice with the same value, the original data is restored:
  ```
  Original ^ Mask = Encrypted
  Encrypted ^ Mask = Original
  ```

#### c) **Reversibility**
The encryption process is **perfectly reversible** because the same mask is used during encryption and decryption, and XOR is self-inverting.

---

### **3. Code Walkthrough**

#### **Step 1: Import Libraries**
```python
from PIL import Image
import numpy as np
import os
```
- `PIL.Image`: To open and save image files.
- `numpy`: For efficient pixel-wise operations.
- `os`: To check file existence.

---

#### **Step 2: Random Mask Generation**
```python
def generate_random_mask(shape, key):
    np.random.seed(key)  # Seed the random generator with the key
    return np.random.randint(0, 256, size=shape, dtype=np.uint8)
```
- **Purpose**: Generates a random matrix (mask) the same size as the image.
- **Inputs**:
  - `shape`: The image dimensions (e.g., `(height, width, channels)`).
  - `key`: Integer used to seed the random number generator.
- **Output**: A matrix of random values in the range `[0, 255]`.

---

#### **Step 3: Encryption**
```python
def encrypt_image(input_path, output_path, key):
    # Open the image
    img = Image.open(input_path)
    img_array = np.array(img, dtype=np.uint8)
    
    # Generate a random mask
    mask = generate_random_mask(img_array.shape, key)

    # Encrypt using XOR
    encrypted_array = np.bitwise_xor(img_array, mask)

    # Save the encrypted image
    encrypted_img = Image.fromarray(encrypted_array, mode=img.mode)
    encrypted_img.save(output_path)
```
1. **Load the Image**:
   - Converts the image into a `numpy` array of pixels (`uint8` type), where each pixel is a value in the range `[0, 255]`.

2. **Generate the Mask**:
   - `generate_random_mask(img_array.shape, key)` produces a matrix of random values based on the `key`.

3. **Apply XOR**:
   - `np.bitwise_xor(img_array, mask)` applies the XOR operation between the pixel values and the mask. This scrambles the pixel values.

4. **Save the Image**:
   - The scrambled `numpy` array is converted back to an image and saved.

---

#### **Step 4: Decryption**
```python
def decrypt_image(input_path, output_path, key):
    # Open the encrypted image
    img = Image.open(input_path)
    img_array = np.array(img, dtype=np.uint8)

    # Generate the same random mask
    mask = generate_random_mask(img_array.shape, key)

    # Decrypt using XOR
    decrypted_array = np.bitwise_xor(img_array, mask)

    # Save the decrypted image
    decrypted_img = Image.fromarray(decrypted_array, mode=img.mode)
    decrypted_img.save(output_path)
```
1. **Load the Encrypted Image**:
   - Reads the scrambled image and converts it into a `numpy` array.

2. **Regenerate the Mask**:
   - Using the same `key`, the identical mask is regenerated.

3. **Reverse XOR**:
   - Applying `np.bitwise_xor(img_array, mask)` with the same mask undoes the encryption, restoring the original image.

4. **Save the Image**:
   - The restored image is saved as a new file.

---

#### **Step 5: User Interaction**
```python
if __name__ == "__main__":
    print("Image Encryption Tool")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    choice = input("Enter your choice (1 or 2): ")
```
- Prompts the user to choose between encryption or decryption.
- Collects the input and output file paths and the key for encryption/decryption.

---

### **4. How It Works**
#### Example:
1. Original image pixel: `150`
2. Mask value: `78` (generated randomly using the key)
3. **Encryption**:
   ```
   Encrypted = 150 ^ 78 = 204
   ```
4. **Decryption**:
   ```
   Decrypted = 204 ^ 78 = 150 (original restored)
   ```

---

### **5. Key Features**
- **Security**:
  - The random mask ensures that even similar images produce different encrypted outputs.
  - Without the key, it’s practically impossible to reconstruct the mask or decrypt the image.
  
- **Reversibility**:
  - The XOR operation ensures no loss of data, and the decryption process perfectly restores the original image.

- **Customizability**:
  - The strength of encryption depends on the key. A larger key space increases security.

---

### **6. Potential Enhancements**
- **Stronger Key Management**: Use more complex keys, such as strings or cryptographic hashes.
- **Advanced Algorithms**: Incorporate more robust encryption techniques (e.g., AES for pixel encryption).
- **Multi-layer Encryption**: Combine XOR with other pixel transformations.

---
