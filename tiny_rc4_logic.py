# tiny_rc4_logic.py
# Phiên bản RC4 rút gọn dùng mảng 0–15 (mod 16) để minh họa

def ksa_tiny(key):
    """Key Scheduling Algorithm - khởi tạo và trộn S-box"""
    N = 16 
    S = list(range(N))
    j = 0
    for i in range(N):
        j = (j + S[i] + key[i % len(key)]) % N
        S[i], S[j] = S[j], S[i]
    return S

def prga_tiny(S, n_bytes):
    """Pseudo-Random Generation Algorithm - sinh keystream"""
    N = 16
    i = j = 0
    keystream = []
    for _ in range(n_bytes):
        i = (i + 1) % N
        j = (j + S[i]) % N
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % N]
        keystream.append(K)
    return keystream

def encrypt_tiny_rc4(plaintext_new, key):
    """Mã hóa: plaintext XOR keystream"""
    S = ksa_tiny(key)
    keystream = prga_tiny(S, len(plaintext_new))
    cipher = [((p ^ k) %16) for p, k in zip(plaintext_new, keystream)]
    return cipher, keystream

def decrypt_tiny_rc4(ciphertext, key):
    """Giải mã: XOR ngược lại với cùng keystream"""
    S = ksa_tiny(key)
    keystream = prga_tiny(S, len(ciphertext))
    plain = [((c ^ k)%16) for c, k in zip(ciphertext, keystream)]
    return plain
 

