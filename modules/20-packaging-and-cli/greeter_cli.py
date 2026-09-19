# Module 20 — CLI demo
# Run:
#   python greeter_cli.py Ada
#   python greeter_cli.py Ada --loud
#   python greeter_cli.py Ada --times 3

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple greeter CLI")
    parser.add_argument("name", help="Who to greet")
    parser.add_argument("--loud", action="store_true", help="Uppercase output")
    parser.add_argument("--times", type=int, default=1, help="Repeat count")
    args = parser.parse_args()

    msg = f"Hello, {args.name}!"
    if args.loud:
        msg = msg.upper()

    for _ in range(args.times):
        print(msg)


if __name__ == "__main__":
    main()
