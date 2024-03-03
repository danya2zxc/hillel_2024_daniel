import os
import threading
import time
from multiprocessing import Process
from pathlib import Path
from threading import Thread

import requests
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)


media_path_folder: Path = Path(__file__).resolve().parent / "media"
if not media_path_folder.exists():
    media_path_folder.mkdir()
og_file_path: Path = Path("rockyou.txt")
enc_file_path = media_path_folder / "encrypted_rockyou.txt"
photo_path: Path = media_path_folder / "image.jpg"
photo_url: str = "https://picsum.photos/1000/1000"


# CPU-bound task (heavy computation)
def encrypt_file(original_path: Path, encrypted_path: Path) -> None:
    print(f"Processing file from {original_path} in process {os.getpid()}")
    with open(original_path, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(encrypted_path, "wb") as enc_file:
        enc_file.write(encrypted)

    with open(encrypted_path, "rb") as file:
        encrypted = file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(encrypted_path, "wb") as dec_file:
        dec_file.write(decrypted)

    _ = [i for i in range(100_000_000)]


# I/O-bound task (downloading image from URL)
def download_image(image_url: str, target_path: Path) -> None:
    print(
        f"Downloading image from {image_url} "
        f"in thread {threading.current_thread().name}"
    )
    response = requests.get(image_url)
    with open(target_path, "wb") as f:
        f.write(response.content)


def main():
    try:
        encryption_start_time = time.perf_counter()

        encrypt_process = Process(
            target=encrypt_file, args=(og_file_path, enc_file_path)
        )
        encrypt_process.start()

        download_start_time = time.perf_counter()

        download_thread = Thread(
            target=download_image, args=(photo_url, photo_path)
        )
        download_thread.start()

        encrypt_process.join()
        encryption_time = time.perf_counter() - encryption_start_time

        download_thread.join()
        download_time = time.perf_counter() - download_start_time

        total = encryption_time + download_time

        print(
            f"Time taken for encryption task: {encryption_time},"
            f"I/O-bound task: {download_time}, Total: {total} seconds"
        )
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
