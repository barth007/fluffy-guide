# test_encryption.py

import pytest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
#import encryption
#import decryption
from encryption import encryption
from decryption import decryption


"""
Encryption Module Test Suite

Overview:
This is a collection of test cases designed to thoroughly test the functionalities
and properties of the encryption module. The encryption module includes functions
for encrypting and decrypting messages using a specified secret key.

Test Cases:
1. Encryption and Decryption Test:
   - Description: Tests the round-trip functionality of the encryption and decryption process.
   - Test Function: test_encryption_decryption
   - Test Input: Sample messages and secret keys
   - Expected Output: Ensure the encrypted message can be decrypted to retrieve the original message.

2. Encryption Test with Mocked Input:
   - Description: Tests the encryption process while mocking user input.
   - Test Function: test_encryption
   - Test Input: Mocked user input for encryption
   - Expected Output: Ensure the encryption process produces expected output and format.

3. Encryption Performance Test:
   - Description: Measures the performance of the encryption process for varying message lengths and secret keys.
   - Test Function: test_encryption_performance
   - Test Input: Different message lengths and secret keys
   - Expected Output: Execution time for the encryption process.

4. Encryption Security Test:
   - Description: Ensures the encrypted message is different from the original message for security.
   - Test Function: test_encryption_security
   - Test Input: Sample message
   - Expected Output: Encrypted message should not match the original message.

5. Encryption Memory Usage Test:
   - Description: Measures the memory usage of the encrypted message to ensure efficient memory utilization.
   - Test Function: test_encryption_memory_usage
   - Test Input: Sample message
   - Expected Output: Memory usage of the encrypted message is within a predefined threshold.

Usage:
1. Make sure the encryption and decryption functions are implemented and accessible from the module.
2. Incorporate this test suite into your testing framework.
3. Run the suite using the testing framework.
4. Examine the test results to ensure all tests pass and functionalities are working as intended.

Note:
This test suite provides comprehensive coverage of the encryption module's functions and aspects
such as security, performance, and memory usage.
"""


@pytest.mark.parametrize("message, secret_key", [
    ("Hello, World!", 3),
    ("This is a longer message.", 7),
])
def test_encryption_decryption(message, secret_key):
    """
    Test encryption and decryption process for consistency.

    This test encrypts a sample message and then decrypts it using the decryption function.
    It then checks whether the decrypted message matches the original message, ensuring the consistency of the encryption and decryption processes.

    Args:
        message (str): The original message to be encrypted and decrypted.
        secret_key (int): The secret key used for encryption.

    Raises:
        AssertionError: If the decrypted message does not match the original message,
                       indicating a potential inconsistency in the encryption or decryption process.
    """


    encrypted_data = encryption(message)
    decrypted_data = decryption(encrypted_data["beta_values"], encrypted_data["gamma_values"])
    assert decrypted_data == message


def test_encryption(monkeypatch):
    """
    Test encryption process with user input simulation.

    This test simulates the user input process by using monkeypatch to set a mock input.
    It then encrypts a sample message and verifies the presence of required keys in the encrypted data.

    Args:
        monkeypatch: A pytest fixture that helps simulate user inputs.

    Raises:
        AssertionError: If the required keys are not present in the encrypted data,
                       indicating a potential issue with the encryption process or data format.
    """


    mock_input = "123"
    monkeypatch.setattr("builtins.input", lambda _: mock_input)
    encrypted_data = encryption("Hello, World!")
    assert "beta_values" in encrypted_data
    assert "gamma_values" in encrypted_data


@pytest.mark.parametrize("message_length", [10, 50, 100])
@pytest.mark.parametrize("secret_key", [3, 7, 11])
def test_encryption_performance(benchmark, message_length, secret_key):
    """
    Measure the performance of the encryption function.

    This performance test measures the execution time of the encryption function by encrypting a message
    of a specified length using a given secret key. The `pytest-benchmark` plugin is used to benchmark
    the execution time and print the result.

    Args:
        benchmark: The benchmark fixture provided by `pytest-benchmark`.
        message_length (int): The length of the message to be encrypted.
        secret_key (int): The secret key to be used for encryption.
    """


    message = "A" * message_length
    result = benchmark(encryption, message)
    print("Execution time: {}".format(result))


@pytest.mark.parametrize("message", [
    "HELLO",
    "This is a secret message.",
])
def test_encryption_security(message):
    """
    Test the security of the encryption process.

    This test function encrypts a given message using the encryption function and checks
    whether the encrypted message is different from the original message. It also verifies
    the structure of the encrypted message and ensures that 'beta_values' and 'gamma_values'
    are present and not empty in the encrypted message dictionary.

    Args:
        message (str): The message to be encrypted.

    Raises:
        AssertionError: If the encrypted message is the same as the original message,
                       or if the encrypted message is not in the expected dictionary format,
                       or if 'beta_values' or 'gamma_values' are empty.
    """


    encrypted_message = encryption(message)
    assert encrypted_message != message, "Encrypted message should not be the same as the original message"
    assert isinstance(encrypted_message, dict), "Encrypted message should be a dictionary"
    assert "beta_values" in encrypted_message, "Encrypted message should contain 'beta_values'"
    assert "gamma_values" in encrypted_message, "Encrypted message should contain 'gamma_values'"
    assert encrypted_message["beta_values"], "beta_values should not be empty"
    assert encrypted_message["gamma_values"], "gamma_values should not be empty"


def test_encrypt_and_decrypt_security():
    """
    Test the security of the encryption and decryption process.

    This test function encrypts a given message using the encryption function and then decrypts
    it using the decryption function. It checks whether the encrypted message is different from
    the original message and whether the decrypted message matches the original message. This
    ensures that the encryption and decryption processes are consistent and secure.

    Args:
        None

    Raises:
        AssertionError: If the encrypted message is the same as the original message,
                       or if the decrypted message does not match the original message.
    """


    message = "HELLO"
    encrypted_message = encryption(message)
    assert encrypted_message != message, "Encrypted message should not be the same as the original message"
    decrypted_message = decryption(encrypted_message["beta_values"], encrypted_message["gamma_values"])
    assert decrypted_message == message, "Decrypted message should match the original message"


def test_encryption_memory_usage():
    """
    Test the memory usage of the encryption function.

    This test function measures the memory usage of the encrypted message generated
    by the encryption function. It then compares the memory usage to a defined threshold
    to ensure that it is within an acceptable range.

    Raises:
        AssertionError: If the memory usage of the encrypted message exceeds the threshold.
    """


    message = "HELLO"
    encrypted_message = encryption(message)
    memory_usage = sys.getsizeof(encrypted_message)
    max_memory_usage = 1024  # 1 KB
    assert memory_usage <= max_memory_usage,f"Memory usage exceeds\
    {max_memory_usage} bytes: {memory_usage} bytes"
