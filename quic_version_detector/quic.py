"""QUIC protocol related facilities."""

import random


class Packet:
    """QUIC packet class.

    Used to send queries to server.
    """

    def __init__(self, public_flags: bytes, connection_id: bytes,
                 version: bytes) -> None:
        self.public_flags = public_flags
        self.connection_id = connection_id
        self.version = version

    def to_buff(self) -> bytes:
        """
        Returns:
            QUIC packet encoded as bytes.
        """
        return self.public_flags + \
            self.connection_id + self.version + bytes.fromhex('01')


class VersionNegotationPacket:
    """Used to hold data for recieved version negotation packets."""

    def __init__(self, public_flags, connection_id, supported_versions):
        self.public_flags = public_flags
        self.connection_id = connection_id
        self.supported_versions = supported_versions


def parse_response(buff: bytes) -> VersionNegotationPacket:
    """Parses QUIC response.

    Args:
        buff: data received from the server - UDP packet.
    """
    versions = buff[9:]
    supported_versions = [versions[i:i+4].decode('ascii') \
        for i in range(0, len(versions), 4)]

    return VersionNegotationPacket(
        public_flags=int(buff[0]),
        connection_id=str(buff[1:9]),
        supported_versions=supported_versions,
    )


def dummy_version_packet() -> Packet:
    """Constructs a packet with a dummy version.

    Such packet makes the server return "Version Negotation Packet".

    Returns:
        quic.Packet
    """
    connection_id = bytes([random.getrandbits(8) for _ in range(8)])
    return Packet(public_flags=bytes.fromhex('0d'),
                  connection_id=connection_id,
                  version=bytes.fromhex('0a0a0a0a'))
