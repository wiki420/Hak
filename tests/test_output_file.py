import os
import pytest
from click.testing import CliRunner
from ciphey.ciphey import main

def test_output_to_file():
    runner = CliRunner()
    test_output_path = "test_output.txt"
    
    # Run Ciphey with a sample text and specify the output file path
    result = runner.invoke(main, ["-t", "aGVsbG8gd29ybGQ=", "-q", "-o", test_output_path])
    
    # Check if the file was created and contains output
    assert os.path.exists(test_output_path), "Output file was not created"
    with open(test_output_path, "r") as f:
        content = f.read()
    assert "hello world" in content, "Decrypted output was not saved correctly"
    
    # Clean up the test output file
    os.remove(test_output_path)

def test_output_to_console():
    runner = CliRunner()
    result = runner.invoke(main, ["-t", "aGVsbG8gd29ybGQ="])
    
    # Check that the console output contains the decrypted text
    assert "hello world" in result.output, "Decrypted output was not printed to console"

