def ip_address(address):
    new_address = ""
    split_address = address.split(".")
    seprator = "[.]"
    new_address = seprator.join(split_address)
    return new_address


if __name__ == "__main__":
    ipaddress = ip_address("192.168.1.1")
    print(ipaddress)
