import sys

from quic_version_detector import quic, net, cli


def print_results(host, port ,version_negotation_packet):
    """Prints retrieved results.

    Args:
        host (str): queried hostname.
        port (int): queried port.
        version_negotation_packet (quic.VersionNegotationPacket)
    """
    print('"{}:{}" supported versions:'.format(host, port))
    for version in version_negotation_packet.supported_versions:
        print('    ', version)


def main():
    """Main entry point."""
    args = cli.parse_args(sys.argv[1:])

    server_addr = net.resolve_hostname(args.host)

    print_results(
        args.host,
        args.port,
        quic.parse_response(net.send_recv_packet(
            server_addr, args.port, quic.dummy_version_packet()))
    )


if __name__ == '__main__':
    main()
