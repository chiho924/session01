import socket
import sys


def client(msg, log_buffer=sys.stderr):

    # Create the server address with the IP address of 127.0.0.1 and port number 10000.
    server_address = ('127.0.0.1', 10000)
    # TODO: Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'

    # Create a socket on the client side that uses IPv4 as the Internet layer protocol and TCP as the
    # transport layer protocol.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

    # Display the server address on the screen for debugging purposes.
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)
    # TODO: connect your socket to the server here.

    # Connect to the server socket on this computer with the IP address of 127.0.0.1 with port number, 20000.
    sock.connect(server_address)

    # you can use this variable to accumulate the entire message received back
    # from the server
    received_message = ''

    # this try/finally block exists purely to allow us to close the socket
    # when we are finished with it
    try:
        # Display the message to be sent on the screen for debugging purposes.
        print('sending "{0}"'.format(msg), file=log_buffer)
        # TODO: send your message to the server here.

        # Send the entire message encoded in UTF8 to the server socket.
        sock.send(msg.encode('utf8'))

        # TODO: the server should be sending you back your message as a series
        #       of 16-byte chunks. Accumulate the chunks you get to build the
        #       entire reply from the server. Make sure that you have received
        #       the entire message and then you can break the loop.
        #
        #       Log each chunk you receive.  Use the print statement below to
        #       do it. This will help in debugging problems

        while True:
            # Receive at most 16 bytes of data from the client.
            chunk = sock.recv(16)

            # Display all the data received on the screen.
            print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)

            # Save the received data, chunk, to received_message in order to construct the entire message received.
            received_message += chunk.decode('utf8')

            # Check to see whether or not the length of chunck is less than 16 bytes.  If so, there are no more
            # data to be received, and the loop will be ended.
            if len(chunk) < 16:
                break  # No more data

    finally:
        # TODO: after you break out of the loop receiving echoed chunks from
        #       the server you will want to close your client socket.

        # Print the debugging message (i.e., closing socket)
        print('closing socket', file=log_buffer)

        # Close the client socket.
        sock.close()

        # TODO: when all is said and done, you should return the entire reply
        # you received from the server as the return value of this function.

        # Return the entire message received to the caller of this function.
        return received_message


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
