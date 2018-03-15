import counter_logic
import validation
import argument_parser
import sys


def main_logic():
    args = argument_parser.set_parser().parse_args()

    file = args.file
    if not (validation.file_exist_validate(file)):
        print(args.file + "file not provided or does not exist")
        sys.exit()

    if args.lines:
        print(counter_logic.count_lines(file), " lines")
    if args.chars:
        print(counter_logic.count_chars(file), " characters")
    if args.words:
        print(counter_logic.count_words(file), " words")


if __name__ == '__main__':
    main_logic()

