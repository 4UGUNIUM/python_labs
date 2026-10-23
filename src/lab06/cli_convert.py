import argparse
import sys

from src.lab05.json_csv import csv_to_json, json_to_csv


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Конвертеры JSON, CSV и XLSX")
    commands = parser.add_subparsers(dest="command", required=True)

    for command_name, help_text in (
        ("json2csv", "JSON в CSV"),
        ("csv2json", "CSV в JSON"),
        ("csv2xlsx", "CSV в XLSX"),
    ):
        command = commands.add_parser(command_name, help=help_text)
        command.add_argument("--in", dest="input_path", required=True, help="входной файл")
        command.add_argument("--out", dest="output_path", required=True, help="выходной файл")

    args = parser.parse_args(argv)

    try:
        if args.command == "json2csv":
            json_to_csv(args.input_path, args.output_path)
        elif args.command == "csv2json":
            csv_to_json(args.input_path, args.output_path)
        else:
            from src.lab05.csv_xlsx import csv_to_xlsx

            csv_to_xlsx(args.input_path, args.output_path)
    except (OSError, UnicodeError, ValueError, RuntimeError) as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        return 1
    except ModuleNotFoundError as error:
        if error.name != "openpyxl":
            raise
        print("Ошибка: для csv2xlsx установите зависимость: python -m pip install openpyxl", file=sys.stderr)
        return 1

    print(f"Готово: {args.output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
