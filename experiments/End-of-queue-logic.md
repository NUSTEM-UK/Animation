# What happens when the queue is emptied?

```text
if (!_isMoving):
    if (next queue item):
        pop it
        execute it
    else:
        if angle != home:
            queue wait(3000)
            queue ease_to(home)
        else:
            detach servo

```


## Disregard below:

- Queue executes via update()
- When queue item finishes (!isMoving()):
  - pop the next queue item
- if no 'next queue item':
  - Wait 3 second
  - Queue a move home, slowly
    - Then: detach the servo


_isMoving
_queueEmptied
_goingHome
_reachedHomeAndStopped

if (!_isMoving):
    if _goingHome is set:
        set _goingHome
        detach servo
        unset _goingHome, _queueEmptied
        exit
    if no queue item:
        set _queueEmptied
        queue wait 3 seconds
        queue ease_to(home)
        exit
    else:
        pop next queue item
            unset _reachedHomeAndStopped


queue:
    1. easeto(0)
    2. easeto(-90)
    3. easeto(90)

set _queueEmptied True

    4. wait(3000)

set _goingHome True

    5. easeTo(home)

set _reachedHomeAndStopped
detach servo
set _goingHome False
set _queueEmptied False

