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


og_file_path: Path = Path("rockyou.txt")
enc_file_path = Path(__file__).resolve().parent / "encrypted_rockyou.txt"
photo_path: Path = Path(__file__).resolve().parent / "image.jpg"
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
def download_image(image_url: str) -> None:
    print(
        f"Downloading image from {image_url} "
        f"in thread {threading.current_thread().name}"
    )
    response = requests.get(image_url)
    with open(photo_path, "wb") as f:
        f.write(response.content)


def processes():
    processes: list[Process | Thread] = [
        Process(target=encrypt_file, args=(og_file_path, enc_file_path)),
        Thread(target=download_image, args=(photo_url,)),
    ]
    for process in processes:
        process.start()
    for process in processes:
        process.join()


def main():
    try:
        encryption_counter = time.perf_counter()

        # encrypt_process = Process(
        #     target=encrypt_file, args=(og_file_path, enc_file_path))
        # encrypt_process.start()
        # encrypt_process.join()
        encrypt_file(og_file_path, enc_file_path)

        download_counter = time.perf_counter()

        # download_thread = Thread(target=download_image, args=(photo_url,))
        # download_thread.start()
        # download_thread.join()

        download_image(photo_url)
        total = time.perf_counter() - encryption_counter

        print(
            f"Time taken for encryption task: {encryption_counter},"
            f"I/O-bound task: {download_counter}, Total: {total} seconds"
        )
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    total_start = time.perf_counter()

    start = time.perf_counter()
    processes()
    end = time.perf_counter()
    print(f"total process time was {end- start}\n")

    main()

    print(f"\nTotal time was {time.perf_counter() - total_start}")
