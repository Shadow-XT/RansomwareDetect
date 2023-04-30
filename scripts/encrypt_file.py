from Crypto.Cipher import AES


def encrypt_file(input_file, output_file, key):
    # 创建AES对象
    aes = AES.new(key.encode("utf-8"), AES.MODE_EAX)

    # 打开原始文件和加密后文件
    with open(input_file, 'rb') as in_file, open(output_file, 'wb') as out_file:
        # 加密前需要写入nonce，以便解密时使用
        out_file.write(aes.nonce)

        # 循环读取原始文件中的数据进行加密
        data = in_file.read(1024)
        while len(data) > 0:
            out_data = aes.encrypt(data)
            out_file.write(out_data)
            data = in_file.read(1024)
