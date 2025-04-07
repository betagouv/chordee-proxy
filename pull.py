import subprocess


def main():
    subprocess.run("git config -l | cat", shell=True)


if __name__ == "__main__":
    main()
