import os
import pytest
from click.testing import CliRunner
from ciphey.ciphey import main

def test_output_to_file():
    runner = CliRunner()
    test_output_path = "test_output.txt"
    result = runner.invoke(main, ["-t", "aGVsbG8gd29ybGQ=", "-q", "-o", test_output_path])
    assert os.path.exists(test_output_path), "Output file was not created"
    with open(test_output_path, "r") as f:
        content = f.read()
    assert "hello world" in content, "Decrypted output was not saved correctly"
    os.remove(test_output_path)

def test_output_to_console():
    runner = CliRunner()
    result = runner.invoke(main, ["-t", "aGVsbG8gd29ybGQ="])
    assert "hello world" in result.output, "Decrypted output was not printed to console"

