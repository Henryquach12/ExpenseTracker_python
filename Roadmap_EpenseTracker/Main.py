import argparse
import Service

# Requirements
def validInt(value):
    try:
        value = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError('The input must be a number!')
    if value <= 0:
        raise argparse.ArgumentTypeError('The number must be greater than 0!')
    return value

# Call service
def handleAdd(args, service):
    service.newExpense(note=args.description, amount=args.amount)
def handleList(args, service):
    service.showExpense()
def handleSum(args, service):
    service.sumExpense(month=args.month)
def handleDelete(args, service):
    service.deleteExpense(id=args.id)

def main():
    # Main parser
    parser = argparse.ArgumentParser(
        description="Tracking expense", 
        epilog="Ex: python expenseTracker.py add --description 'eat out' --amount 20"
        )

    # Subcommands (add, delete, update, etc.)
    subparsers = parser.add_subparsers(dest="command")

    # 'add' comand
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('--description', type=str, required=True, help="Description of the expense('Coffee, gym,...')")
    add_parser.add_argument('--amount', type=validInt, required=True, help="Amount of money")
    add_parser.set_defaults(func=handleAdd)

    # 'list' command
    list_parser = subparsers.add_parser('list')
    list_parser.set_defaults(func=handleList)

    # 'summary' command
    summary_parser = subparsers.add_parser('summary')
    summary_parser.add_argument('--month', type=validInt, nargs='+', help="(Optional) total expense of a specific month")
    summary_parser.set_defaults(func=handleSum)

    # 'delete' command
    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument('--id' , type=validInt, required=True, help="Id of the expense")
    delete_parser.set_defaults(func=handleDelete)

    # Read and validate CLI arguments, then store them in args
    args = parser.parse_args()

    # Object for expenseTracker class
    service = Service.serviceOperation()

    # Transfer parameters and command
    if hasattr(args, 'func'):
        args.func(args, service)
    else:
        parser.print_help()

# Main file
if __name__ == '__main__':
    main()


