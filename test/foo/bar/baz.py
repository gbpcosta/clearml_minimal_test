import argparse
from clearml import Task


def parse_args():
    parser = argparse.ArgumentParser('clearml execute remotely minimal')

    parser.add_argument('--arg1-str', type=str, required=True)
    parser.add_argument('--arg2-str', type=str, required=True)

    parser.add_argument('--arg3-int', type=int, default=75)

    parser.add_argument('--arg4-float', type=float, default=1e-3)

    parser.add_argument('--arg5-str-list', type=str, nargs='+', default=[])

    parser.add_argument('--execute-remotely', action='store_true')
    parser.add_argument('--remote-queue', type=str, default='high-priority')

    return parser.parse_args()


def main():
    args = parse_args()

    task = Task.init(project_name='clearml_debug',
                     task_name='minimal_example',
                     output_uri=True,
                     reuse_last_task_id=False)

    if args.execute_remotely:
        task.execute_remotely(queue_name=args.remote_queue, clone=False, exit_process=True)


if __name__ == '__main__':
    main()
