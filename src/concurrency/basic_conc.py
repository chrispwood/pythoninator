import itertools
import time
from threading import Thread, Event

def spin(msg: str, done: Event, pause: Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        if pause.is_set():
            # Clear the current spinner line so the prompt is clean
            print('\r' + ' ' * (len(msg) + 2) + '\r', end='', flush=True)
            while pause.is_set():
                if done.wait(.1):
                    break
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

def slow() -> int:
    time.sleep(3)
    return 42

def supervisor() -> int:
    done = Event()
    pause = Event()
    spinner = Thread(target=spin, args=('thinking!', done, pause))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = slow()

    while True:
        # pause is needed to stop printing during user input
        pause.set()

        # need to add this because spinner might print one more time
        time.sleep(.1)

        user_input = input("\rKeep waiting? y/N: ").strip().lower()

        # break if user doesn't want to wait
        if user_input != 'y':
            break

        # resume printing
        pause.clear()
        # wait on main thread
        result = slow()

    # user no longer waiting. Wrap up the thread worker (simulated)
    done.set()

    # wait for the thread to finish
    spinner.join()
    
    return result

def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()