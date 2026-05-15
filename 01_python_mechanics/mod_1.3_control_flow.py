ramdisk_files = [11.4, 45.6, 52.1, 4.2, 24.0]

# Iterate through each file size in the list
for size in ramdisk_files:
    # print(f"{file}MB")
    if size > 45.6:
        print(
            f"[CRITICAL] File size {size}MB exceeds buffer container! Purging immediately."
        )
    elif 10.0 <= size <= 45.6:
        print(f"[UPLOADING] file size {size}MB optimal. Transmitting payload.")
    else:
        print(
            f"[SKIP] File size {size}MB insufficient capture length. Fragment ignored."
        )
