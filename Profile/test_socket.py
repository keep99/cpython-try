# -*- coding: utf-8 -*-
import socket
import profile

def main():
    for i in range(100):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7788端口
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(("", 7788))
        server_socket.listen(128)
 
if __name__ == "__main__":
    profile.run('main()')
    