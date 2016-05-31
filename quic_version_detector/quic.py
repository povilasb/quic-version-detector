"""QUIC protocol related facilities."""


class Packet:
    """QUIC packet class.

    Used to send queries to server.
    """

    def __init__(self, public_flags, connection_id, version):
        self.public_flags = public_flags
        self.connection_id = connection_id
        self.version = version

    def to_buff(self):
        """
        Returns:
            str: QUIC packet encoded to ascii string.
        """
        packet = self.public_flags + self.connection_id + self.version + '\x01'
        return packet.encode('ascii')


class VersionNegotationPacket:
    """Used to hold data for recieved version negotation packets."""

    def __init__(self, public_flags, connection_id, supported_versions):
        self.public_flags = public_flags
        self.connection_id = connection_id
        self.supported_versions = supported_versions


def parse_response(buff):
    """Parses QUIC response.

    Args:
        buff (bytes): data received from the server - UDP packet.

    Returns:
        VersionNegotationPacket
    """
    versions = buff[9:]
    supported_versions = [versions[i:i+4].decode('ascii') \
        for i in range(0, len(versions), 4)]

    return VersionNegotationPacket(
        public_flags=int(buff[0]),
        connection_id=str(buff[1:9]),
        supported_versions=supported_versions,
    )
