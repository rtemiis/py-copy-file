def copy_file(command: str) -> None:
    command_words = command.split()
    print(command_words)
    try:
        if command_words[0].lower() == "cp":
            file_source = command_words[1].lower()
            file_dest = command_words[2].lower()
            with (
                open(file_source, "r") as file_source,
                open(file_dest, "w") as file_dest
            ):
                file_dest.write(file_source.read())
    except IndexError as e:
        print(f"{e}: Not enough arguments")
    except FileNotFoundError as e:
        print(f"{e}: File not found")
