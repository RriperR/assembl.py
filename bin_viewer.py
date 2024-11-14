with open("program.bin", "rb") as f:
    content = f.read()
    print(" ".join(f"{byte:02x}" for byte in content))
