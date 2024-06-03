import socket
import os
from face_test import face_recognition

def receive_image(client_socket):
    received_data = b''
    end_flag = b'##end##'  # 结束标识符
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        received_data += data
        # 检查接收到的数据是否包含结束标识符
        if end_flag in received_data:
            # 截取图片数据部分，不包含结束标识符
            image_data, extra_data = received_data.split(end_flag, 1)
            received_data = image_data
            break
    return received_data


def save_image(image_data, filename):
    with open(filename, 'wb') as file:
        file.write(image_data)

def main():
    # 创建服务器端的Socket对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定IP地址和端口号
    host = '0.0.0.0'  # 将这里替换为你电脑的 IP 地址
    port = 8080
    server_socket.bind((host, port))

    # 监听连接请求
    server_socket.listen(1)
    print("等待客户端连接...")

    while True:
        # 等待客户端连接
        client_socket, address = server_socket.accept()
        print("客户端已连接！")

        # 接收图片名称
        filename = client_socket.recv(1024).decode()
        # 接收图片数据
        received_data = receive_image(client_socket)
        print("图片接收完成！")
        # 将接收到的数据保存为图片文件
        save_image(received_data, filename)

        # 进行人脸识别并获得sign
        sign = face_recognition(filename)
        
        if sign :
            res="True"
        else :
            res="False"
        # 发送sign给客户端
        client_socket.sendall(res.encode())

        # 关闭连接
        client_socket.close()
        

    # 关闭服务器Socket
    server_socket.close()

if __name__ == "__main__":
    main()
