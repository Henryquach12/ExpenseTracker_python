import argparse
import executeCommand
# Required the number to be greater than 0
def validInt(value):
    value = int(value)
    if value <= 0:
        raise argparse.ArgumentTypeError('The number must be greater than 0!')
    return value
def main():
    # Main parser: defines the CLI program and shows help info (--help)
    parser = argparse.ArgumentParser(description="Tracking expense", epilog="Ex: python expenseTracker.py add --description 'eat out' --amount 20")

    # Subparsers: define subcommands (add, delete, update, etc.)
    # Dest="command": stores the subcommand name in args.command
    subparsers = parser.add_subparsers(dest="command")

    # Process 'add' argument
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('--description', type=str, required=True, help="Description of the expense('Coffee, gym,...')")
    add_parser.add_argument('--amount', type=validInt, required=True, help="Amount of money")

    # Process 'list' argument
    add_parser = subparsers.add_parser('list')

    # Process 'summary' argument
    add_parser = subparsers.add_parser('summary')
    add_parser.add_argument('--month', type=validInt, nargs='+', help="(Optional) total expense of a specific month")

    # Process 'delete' argument
    add_parser = subparsers.add_parser('delete')
    add_parser.add_argument('--id' , type=validInt, required=True, help="Id of the expense")


    args = parser.parse_args()

    execute = executeCommand.expenseTracker()
    if args.command == 'add':
        execute.newExpense(data=args.description, amount=args.amount)

if __name__ == '__main__':
    main()


