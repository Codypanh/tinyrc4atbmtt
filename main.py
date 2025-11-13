# tiny_rc4_display.py
from tiny_rc4_logic  import encrypt_tiny_rc4, decrypt_tiny_rc4

def to_hex(data):
    """Chuyển danh sách số thành chuỗi hex (viết hoa)"""
    return ''.join(format(x, 'X') for x in data)

def to_binary(data):
    """Chuyển danh sách số thành chuỗi nhị phân (mỗi số 4 bit, vì mod 16)"""
    return ''.join(format(x, '04b') for x in data)

def main():
    # Khóa ví dụ: 4 phần tử (giá trị từ 0–15)
    key_input = ' '.join(input("Nhập khóa (4 số từ 0-15): "))
    # Chuyển chuỗi nhập vào thành danh sách số nguyên (mod 16). Nếu nhập sai, dùng khóa mặc định.
    parts = key_input.strip().split()
    try:
        key = [int(x) % 16 for x in parts]
    except ValueError:
        print("Khóa không hợp lệ, dùng khóa mặc định [1, 2, 3, 4]")
        key = [1, 2, 3, 4]
    # Đảm bảo đủ 4 phần tử: cắt hoặc điền 0 nếu cần
    if len(key) < 4:
        key = (key + [0, 0, 0, 0])[:4]
    elif len(key) > 4:
        key = key[:4]

    # Dữ liệu bản rõ (plaintext): 8 phần tử
    plaintext = input("Nhập văn bản bạn cần mã hóa/ giải mã: ").upper()
    plaintext_new = [ord(c) for c in plaintext]
    print("Mã sau khi đã đổi sang bảng mã AScii: ", plaintext_new)

    print("=== TINY RC4 DEMO (mod 16) ===")
    print(f"Key: {key}")
    print(f"Plaintext: {plaintext_new}")
    n = input("Hãy lựa chọn bước thực hiện:\n1. Mã hóa: \n2. Giải mã: ")
    if n == '1':
        cipher, keystream = encrypt_tiny_rc4(plaintext_new, key)
        print(f"\n[+] Keystream: {keystream}")
        print(f"[+] Ciphertext: {cipher}")
        m = input("Bạn muốn chuyển đổi bản  mã hóa của bạn sang dạng hex hay binary? (gõ 'binary: 1' hoặc 'hex: 2'): ")
        if m == '1':
            bin_output = to_binary(cipher)
            print(f"[+] Binary output: {bin_output}")
        elif m == '2':
            hex_output = to_hex(cipher)
            print(f"[+] Hex output: {hex_output}")

    elif n == '2':
        decrypted = decrypt_tiny_rc4(plaintext_new, key)
        print(f"\n[+] Decrypted: {decrypted}")
        m = input("Bạn muốn chuyển đổi bản giải mã của bạn sang dạng hex hay binary? (gõ 'binary: 1' hoặc 'hex: 2'): ")
        if m == '1':
            bin_output = to_binary(decrypted)
            print(f"[+] Binary output: {bin_output}")
        elif m == '2':
            hex_output = to_hex(decrypted)
            print(f"[+] Hex output: {hex_output}")
if __name__ == "__main__":
    main()
