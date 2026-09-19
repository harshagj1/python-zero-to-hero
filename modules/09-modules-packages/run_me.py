# Module 09 — run from this folder:
#   python run_me.py

from demo_package import shout, average
from demo_package.mathy import clamp


def main():
    print(shout("modules are power"))
    print("average:", average([2, 4, 6]))
    print("clamp 150 to 0..100:", clamp(150, 0, 100))


if __name__ == "__main__":
    main()
