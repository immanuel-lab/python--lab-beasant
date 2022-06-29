import socket
def serever_program():
    host=socket.gethostname()
    port=5000
    server_socket=socket.sockets()
    server_socket.bind((host,port))
    server_socket.listen(2)
    comm,address=server_socket.accept()
    while True:
        data=conn.recv(1024).decode()
        if not data:
            break
        print(data)
        data=input()
        conn.send(data.encode())
        conn.close()
if __name__=="main":
 server_program()
    
                   
        
