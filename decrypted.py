
import os
import string
from cryptography.fernet import Fernet, InvalidToken
import base64
import hashlib

try:
    my_key = "MyOwnSecretPassword123"
    key = base64.urlsafe_b64encode(
        hashlib.sha256(my_key.encode("utf-8")).digest()
    )
    fk = Fernet(key)

    for drive in string.ascii_uppercase:
        path = f"{drive}:\\"

        if not os.path.exists(path):
            continue

        print(f"\nScanning drive: {path}")

        for root, dirs, files in os.walk(path, topdown=True):
            dirs.sort()
            files.sort()

            print(f"\nScanning folder: {root}")

            for filename in files:
                # Skip only encrypted.exe and decrypted.exe
                if filename.lower() in ("encrypted.exe", "decrypted.exe"):
                    continue

                filepath = os.path.join(root, filename)

                print("\n" + "=" * 80)
                print("FILE:", filepath)
                print("=" * 80)

                try:
                    with open(filepath, "rb") as f:
                        content = f.read()

                    try:
                        decrypted_content = fk.decrypt(content)
                    except InvalidToken:
                        print(f"[SKIPPED] Invalid token or incorrect key: {filepath}")
                        continue

                    with open(filepath, "wb") as file:
                        file.write(decrypted_content)

                except OSError as e:
                    print(f"[FILE ERROR] {filepath}: {e}")

except OSError as e:
    print(f"[DRIVE SCAN ERROR] {e}")

print("\nFinished checking all drive letters.")
