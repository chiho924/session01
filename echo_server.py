import socket
import sys


def server(log_buffer=sys.stderr):
    # Set an address for our server with the IP address of 127.0.0.1 and port number 10000.
    address = ('127.0.0.1', 10000)
    # TODO: Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'

    # Create a socket on the server side that uses IPv4 as the Internet layer protocol and TCP as the transport
    # layer protocol.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

    # TODO: You may find that if you repeatedly run the server script it fails,
    #       claiming that the port is already used.  You can set an option on
    #       your socket that will fix this problem. We DID NOT talk about this
    #       in class. Find the correct option by reading the very end of the
    #       socket library documentation:
    #       http://docs.python.org/3/library/socket.html#example

    # Tell the kernel to reuse a local socket in TIME_WAIT state without waiting for its natural timeout to expire.
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Log that we are building a server.
    print("making a server on {0}:{1}".format(*address), file=log_buffer)

    # TODO: bind your new sock 'sock' to the address above and begin to listen
    #       for incoming connections

    # Bind the server socket with the loopback address and the port number.
    sock.bind(address)
    # Listen for attempted connection with the maximum number of connection requests that the socket will queue
    # to be 1.
    sock.listen(1)

    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            # Print the debugging message on the screen (i.e., waiting for a connection).
            print('waiting for a connection', file=log_buffer)

            # TODO: make a new socket when a client connects, call it 'conn',
            #       at the same time you should be able to get the address of
            #       the client so we can report it below.  Replace the
            #       following line with your code. It is only here to prevent
            #       syntax errors

            # Receive an incoming connection request from a client.
            conn, addr = sock.accept()

            try:
                # Print the debugging message on the screen (i.e., the client's socket address information).
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)

                # the inner loop will receive messages sent by the client in
                # buffers.  When a complete message has been received, the
                # loop will exit
                while True:
                    # TODO: receive 16 bytes of data from the client. Store
                    #       the data you receive as 'data'.  Replace the
                    #       following line with your code.  It's only here as
                    #       a placeholder to prevent an error in string
                    #       formatting

                    # Receive at most 16 bytes of data from the client.
                    data = conn.recv(16)

                    # Print the data received on the screen for debugging purposes.
                    print('received "{0}"'.format(data.decode('utf8')))
                    # TODO: Send the data you received back to the client, log
                    # the fact using the print statement here.  It will help in
                    # debugging problems.

                    # Echo the data back to the client.
                    conn.send(data)

                    # Print the data sent on the screen for debugging purposes.
                    print('sent "{0}"'.format(data.decode('utf8')))
                    # TODO: Check here to see if the message you've received is
                    # complete.  If it is, break out of this inner loop.

                    # Check to see whether or not the entire message has been sent.  If so, this means that the
                    # length of data is less than 16, and the loop would be ended.
                    if len(data) < 16:
                        break  # No more data

            finally:
                # TODO: When the inner loop exits, this 'finally' clause will
                #       be hit. Use that opportunity to close the socket you
                #       created above when a client connected.

                # Print the debugging message on the screen (i.e., client connection is closed).
                print(
                    'echo complete, client connection closed', file=log_buffer
                )

                # Close the client's scoket.
                conn.close()

    except KeyboardInterrupt:
        # TODO: Use the python KeyboardInterrupt exception as a signal to
        #       close the server socket and exit from the server function.
        #       Replace the call to `pass` below, which is only there to
        #       prevent syntax problems

        # Close the server's socket.
        sock.close()
        # Print the debugging message on the screen (i.e., quitting echo server).
        print('quitting echo server', file=log_buffer)


if __name__ == '__main__':
    server()
    sys.exit(0)
