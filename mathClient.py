

import socket
#create client socket
socket = socket.socket(socket. AF_INET , socket. SOCK_DGRAM )
#initialize and empty list to hold the message (an array of strings)
message = []
#ask user for the operation they want to perform
operation = input (
"""
Net-Centric Math Server by CHIOMA  GOODNESS IGWILO
Please select your operation:
1 - Addition   3 - Subtraction     5 - Multiplication
2- Division    4 - Modulus
>_
"""
)
#add operation to message
message.append( str (operation))
#ask user for the two values on which the operation is performed
first_variable = input ( 'enter the first value: >_ ' )
second_variable = input ('enter the second value: >_ ' )
#add the values to the message
message.append( str (first_variable))
message.append( str (second_variable))
#format message into [operation,first_varible,second_variable]
message = ',' .join(message)
#send message to client-side
socket.sendto(message, ( 'localhost' , 8640)
#receive result from server
server_result, server_address = socket.recvfrom( 1024 *3 )
print ( 'server result: ' + server_result)
#close connection between client and server
socket.close() ;



