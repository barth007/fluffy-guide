import smtplib
import email
from json import dumps

from encryption import encryption


# Function to send an encrypted email with a text message
def send_encrypted_email(sender_email, receiver_email, app_password, subject, email_message, text_message):
    # Encrypt the email message and text message using the corona graph encryption
    full_message = f"{email_message}\n\n{text_message}"
    beta_gamma_values = encryption(full_message)

    # Create the email content
    msg = email.message.EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    # msg.set_content("Encrypted Email - See attachment for the encrypted message")

    # Attach the encrypted message as a file
    msg.add_attachment(dumps(beta_gamma_values).encode(), subtype='plain', filename='encrypted_message.txt', maintype='plain')

    # Connect to the email server and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

    print("Email sent successfully!")
    smtp.close()

# # Function to receive and decrypt an email
# def receive_and_decrypt_email(receiver_email, app_password):
#     # Log in to the email server and select the inbox
#     with imaplib.IMAP4_SSL('imap.gmail.com') as mail:
#         mail.login(receiver_email, app_password)
#         mail.select('inbox')

#         # # Search for emails from the sender
#         # result, data = mail.search(None, f'(FROM "{sender_email}")')

#         # # Get the latest email
#         # latest_email_id = data[0].split()[-1] # worlking so far
#         # result, msg_data = mail.fetch(latest_email_id.decode('utf-8'), "(RFC822)")
        
#         # # Parse the email content
#         # raw_email = msg_data[0][1]
#         # msg = email.message_from_bytes(raw_email)
#         # print("MSG: ", msg)
#         # encrypted_message_bytes = msg.get_payload(0)
#         # print("First: ", encrypted_message_bytes)
#         # encrypted_message_bytes = encrypted_message_bytes.get_payload()

#         # # encrypted_message_bytes = encrypted_message_bytes.decode('utf-8')

#         # print("Encrypted msg bytes (after): ", encrypted_message_bytes); 
        
#         # Search for emails based on the search criteria
#         result, data = mail.search(None, f'(FROM "{sender_email}")')

#         # Get the email IDs
#         email_ids = data[0].split()

#         for email_id in email_ids:
#             # Fetch the email data
#             result, msg_data = mail.fetch(email_id, "(RFC822)")

#             # Parse the email content
#             raw_email = msg_data[0][1]
#             msg = email.message_from_bytes(raw_email)

#             # Loop through the email parts
#             for part in msg.walk():
#                 if part.get_content_maintype() == 'multipart':
#                     continue
#                 if part.get('Content-Disposition') is None:
#                     continue

#                 # Extract the attachment
#                 filename = part.get_filename()
#                 if filename:
#                     # Save the attachment to a specific folder
#                     with open(os.path.join('.', filename), 'wb') as f:
#                         f.write(part.get_payload(decode=True))
        
#         temp_file = open("encrypted_message.txt", "r")
#         encrypted_message_bytes = ast.literal_eval(temp_file.read())
#         temp_file.close()
#         os.remove(filename)

#         # Create the cycle graph C_n 
#         cycle_graph = nx.cycle_graph(encrypted_message_bytes["beta_values"])

#         # Create a new graph for the corona graph C_n⨀K_1
#         corona_graph = nx.Graph()

#         # Add nodes and edges from the cycle graph C_n
#         corona_graph.add_nodes_from(cycle_graph)
#         corona_graph.add_edges_from(cycle_graph.edges())

#         # Add additional vertices for the K_1 component
#         k1_vertices = [i for i in range(len(encrypted_message_bytes["gamma_values"]))]
#         for i in range(len(k1_vertices)):
#             corona_graph.add_node(i, value=encrypted_message_bytes["gamma_values"][i])

        
#         # connecting pendant vertices with the inner vertices
#         for ver, k_ver in zip(encrypted_message_bytes["beta_values"], k1_vertices):
#             corona_graph.add_edge(ver, k_ver) 

#         # Decrypt the encrypted message using corona graph decryption
#         decrypted_msg = decryption(corona_graph)
#         print(decrypted_msg)

#         mail.close()

if __name__ == "__main__":
    sender_email = ""  # Replace with your sender email address
    receiver_email = ""  # Replace with your receiver email address

    # Call generate() only once to generate keys
    #generate()

    subject = input("Enter the email subject: ")
    email_message = input("Enter the email message: ")

    # You can leave text_message empty if you don't want to include it
    text_message = input("Enter the text message (optional): ")

    # Enter the app passwords for sender and receiver email accounts
    sender_app_password = ""  # Replace with the sender's app password
    receiver_app_password = ""  # Replace with the receiver's app password

    send_encrypted_email(sender_email, receiver_email, sender_app_password, subject, email_message, text_message)
    # receive_and_decrypt_email(receiver_email, receiver_app_password)

