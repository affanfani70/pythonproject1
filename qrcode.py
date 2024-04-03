import qrcode


class MyQRCode:
    def __init__(self, size: int, padding: int) -> None:
        self.qr = qrcode.QRCode(version=1, box_size=size, border=padding)

    def create_qrcode(self, filename: str, fg_color: str, bg_color: str) -> None:
        user_input = input("Enter text: ")
        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make(fill_color=fg_color, back_color=bg_color)
            qr_image.save(filename)

            print(f"Successfully created {filename}")
        except Exception as e:
            print("Something went wrong")


def main() -> None:
    my_qr = MyQRCode(30, 90)
    my_qr.create_qrcode("sample.png", "red", "blue")


if __name__ == "__main__":
    main()
