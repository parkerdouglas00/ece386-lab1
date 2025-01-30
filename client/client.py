"""
TODO: Insert what this program does here.
"""

import sys
from requests import post


def get_img_prediction(
    server_ip: str, server_port: int, api_path: str, image_path: str
) -> str:
    """Send image to server for prediction."""
    # TODO: Replace with code to send image to server
    url = f"http://{server_ip}:{server_port}{api_path}"
    files = {"image": open(image_path, "rb")}
    response = post(url, files=files)
    return response.text


def main(server_ip: str, server_port: int) -> None:
    """Repeatedly prompt the user for a path to an image
    and send it to the server for prediction.
    Then display the result to the user.
    """
    # TODO: Replace with prompt to user and call to get_img_prediction
    filepath = input("Image path: ")
    num = get_img_prediction(server_ip, server_port, "/predict", filepath)
    print(num)


if __name__ == "__main__":
    # Ensure user passes required arguments
    if len(sys.argv) != 3:
        print("Usage: python client.py <server IP address> <server port>")
        sys.exit(1)

    main(sys.argv[1], int(sys.argv[2]))
