import os


def main():
    path = r"C:\Users\Muhammadsiddig\Pictures\recov"
    for file_path in os.listdir(path):
        if (
            not os.path.splitext(file_path)[-1]
            or os.path.splitext(file_path)[-1] == ".thumb"
        ):
            os.rename(
                os.path.join(path, file_path),
                os.path.join(path, "{}_.jpg".format(file_path)),
            )


if __name__ == "__main__":
    main()
