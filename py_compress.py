import zlib
import bz2
import gzip
import time


def get_printable_size(byte_size):
    """
    A bit is the smallest unit, it's either 0 or 1
    1 byte = 1 octet = 8 bits
    1 kB = 1 kilobyte = 1000 bytes = 10^3 bytes
    1 KiB = 1 kibibyte = 1024 bytes = 2^10 bytes
    1 KB = 1 kibibyte OR kilobyte ~= 1024 bytes ~= 2^10 bytes (it usually means 1024 bytes but sometimes it's 1000... ask the sysadmin ;) )
    1 kb = 1 kilobits = 1000 bits (this notation should not be used, as it is very confusing)
    1 ko = 1 kilooctet = 1000 octets = 1000 bytes = 1 kB
    Also Kb seems to be a mix of KB and kb, again it depends on context.
    In linux, a byte (B) is composed by a sequence of bits (b). One byte has 256 possible values.
    More info : http://www.linfo.org/byte.html
    """
    BASE_SIZE = 1024.00
    MEASURE = ["B", "KB", "MB", "GB", "TB", "PB"]

    def _fix_size(size, size_index):
        if not size:
            return "0"
        elif size_index == 0:
            return str(size)
        else:
            return "{:.3f}".format(size)

    current_size = byte_size
    size_index = 0

    while current_size >= BASE_SIZE and len(MEASURE) != size_index:
        current_size = current_size / BASE_SIZE
        size_index = size_index + 1

    size = _fix_size(current_size, size_index)
    measure = MEASURE[size_index]
    return size + measure


with open("ETHBTC1h_test_data.txt") as f:
    _str = f.read()

_str = bytes(_str, "utf-8")
for i_mode in range(1, 4):
    if i_mode == 1:
        _mode = zlib
        print("\nzlib")
    elif i_mode == 2:
        _mode = bz2
        print("\nbz2")
    else:
        _mode = gzip
        print("\ngzip")
    print("Level\tCompressTime\tDecompressTime\tSize\tCompressedSize\tCompressionRate")
    for level in range(1, 10):

        d_compress_time = 0.0
        d_decompress_time = 0.0
        s_output = ""
        f_original_size = 0.0
        f_compressed_size = 0.0
        f_compression_rate = 0.0

        for is_decompress in range(2):
            if is_decompress:
                _compressed_str = _mode.compress(_str, level)

            t = time.time()
            if is_decompress:
                _str = _mode.decompress(_compressed_str)
                d_decompress_time = "%6.02fms" % (1000 * (time.time() - t))
            else:
                _compressed_str = _mode.compress(_str, level)
                d_compress_time = "%6.02fms" % (1000 * (time.time() - t))

            if not is_decompress:
                f_original_size = get_printable_size(len(_str))
                f_compressed_size = get_printable_size(len(_compressed_str))
                f_compression_rate = "%.03f%%" % (float(len(_str)) / len(_compressed_str))

        print(str(level) + "\t" + d_compress_time + "\t" + d_decompress_time + "\t" + \
              f_original_size + "\t" + f_compressed_size + "\t" + f_compression_rate)
