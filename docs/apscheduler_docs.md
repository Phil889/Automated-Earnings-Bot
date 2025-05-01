# APScheduler Documentation

This document contains code snippets and examples for using APScheduler, a task scheduling library for Python.

## Basic Usage

### Running a Scheduler in the Foreground (Synchronous)

```python
from apscheduler import Scheduler

with Scheduler() as scheduler:
    # Add schedules, configure tasks here
    scheduler.run_until_stopped()
```

### Running a Scheduler in the Background (Synchronous)

```python
from apscheduler import Scheduler

with Scheduler() as scheduler:
    # Add schedules, configure tasks here
    scheduler.start_in_background()
```

### Alternative Background Scheduler (for WSGI compatibility)

```python
from apscheduler import Scheduler

scheduler = Scheduler()
# Add schedules, configure tasks here
scheduler.start_in_background()
```

### Running an AsyncScheduler in the Foreground (Asyncio)

```python
import asyncio

from apscheduler import AsyncScheduler

async def main():
    async with AsyncScheduler() as scheduler:
        # Add schedules, configure tasks here
        await scheduler.run_until_stopped()

asyncio.run(main())
```

### Running an AsyncScheduler in the Background (Asyncio)

```python
import asyncio

from apscheduler import AsyncScheduler

async def main():
    async with AsyncScheduler() as scheduler:
        # Add schedules, configure tasks here
        await scheduler.start_in_background()

asyncio.run(main())
```

## Task Configuration

### Task Settings Inheritance

```python
from apscheduler import Scheduler, TaskDefaults, task

@task(max_running_jobs=3, metadata={"foo": ["taskfunc"]})
def mytaskfunc():
    print("running stuff")

task_defaults = TaskDefaults(
    misfire_grace_time=15,
    job_executor="processpool",
    metadata={"global": 3, "foo": ["bar"]}
)
with Scheduler(task_defaults=task_defaults) as scheduler:
    scheduler.configure_task(
        "sometask",
        func=mytaskfunc,
        job_executor="threadpool",
        metadata={"direct": True}
    )
```

### Accessing Current Job Context

```python
from apscheduler import current_job

def my_task_function():
    job_info = current_job.get().id
    print(
        f"This is job {job_info.id} and was spawned from schedule "
        f"{job_info.schedule_id}"
    )
```

## Triggers

### Combining Triggers with OrTrigger

```python
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger

trigger = OrTrigger(
    CronTrigger(day_of_week="mon-fri", hour=10),
    CronTrigger(day_of_week="sat-sun", hour=11),
)
```

### Combining Triggers with AndTrigger

```python
from apscheduler.triggers.calendarinterval import CalendarIntervalTrigger
from apscheduler.triggers.combining import AndTrigger
from apscheduler.triggers.cron import CronTrigger

trigger = AndTrigger(
    CalendarIntervalTrigger(months=2, hour=10),
    CronTrigger(day_of_week="mon-fri", hour=10),
)
```

## Event Handling

### Subscribing to Synchronous Scheduler Events

```python
from apscheduler import Event, JobAcquired, JobReleased

def listener(event: Event) -> None:
    print(f"Received {event.__class__.__name__}")

scheduler.subscribe(listener, {JobAcquired, JobReleased})
```

### Subscribing to Asynchronous Scheduler Events

```python
from apscheduler import Event, JobAcquired, JobReleased

async def listener(event: Event) -> None:
    print(f"Received {event.__class__.__name__}")

scheduler.subscribe(listener, {JobAcquired, JobReleased})
```

## Web Framework Integration

### WSGI Application Integration

```python
from apscheduler import Scheduler

def app(environ, start_response):
    """Trivial example of a WSGI application."""
    response_body = b"Hello, World!"
    response_headers = [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(response_body))),
    ]
    start_response(200, response_headers)
    return [response_body]

scheduler = Scheduler()
scheduler.start_in_background()
```

### Running a WSGI Application with uWSGI

```bash
uwsgi --enable-threads --http :8080 --wsgi-file example.py
```

### ASGI Application Integration

```python
from apscheduler import AsyncScheduler

async def app(scope, receive, send):
    """Trivial example of an ASGI application."""
    if scope["type"] == "http":
        await receive()
        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [
                    [b"content-type", b"text/plain"],
                ],
            }
        )
        await send(
            {
                "type": "http.response.body",
                "body": b"Hello, world!",
                "more_body": False,
            }
        )
    elif scope["type"] == "lifespan":
        while True:
            message = await receive()
            if message["type"] == "lifespan.startup":
                await send({"type": "lifespan.startup.complete"})
            elif message["type"] == "lifespan.shutdown":
                await send({"type": "lifespan.shutdown.complete"})
                return


async def scheduler_middleware(scope, receive, send):
    if scope['type'] == 'lifespan':
        async with AsyncScheduler() as scheduler:
            await app(scope, receive, send)
    else:
        await app(scope, receive, send)
```

### Running an ASGI Application with Hypercorn

```bash
hypercorn example:scheduler_middleware
```

## Extending APScheduler

### Defining a Custom Trigger

```python
from __future__ import annotations

from apscheduler.abc import Trigger

class MyCustomTrigger(Trigger):
    def next() -> datetime | None:
        ... # Your custom logic here

    def __getstate__():
        ... # Return the serializable state here

    def __setstate__(state):
        ... # Restore the state from the return value of __getstate__()
```

### Implementing a Basic Thread Job Executor

```python
from contextlib import AsyncExitStack
from functools import partial

from anyio import to_thread
from apscheduler import Job
from apscheduler.abc import JobExecutor

class ThreadJobExecutor(JobExecutor):
    async def run_job(self, func: Callable[..., Any], job: Job) -> Any:
        wrapped = partial(func, *job.args, **job.kwargs)
        return await to_thread.run_sync(wrapped)
```

### Implementing a Thread Pool Job Executor with Capacity Limiter

```python
from contextlib import AsyncExitStack
from functools import partial

from anyio import CapacityLimiter, to_thread
from apscheduler import Job
from apscheduler.abc import JobExecutor

class ThreadJobExecutor(JobExecutor):
    _limiter: CapacityLimiter

    def __init__(self, max_threads: int):
        self.max_threads = max_threads

    async def start(self, exit_stack: AsyncExitStack) -> None:
        self._limiter = CapacityLimiter(self.max_workers)

    async def run_job(self, func: Callable[..., Any], job: Job) -> Any:
        wrapped = partial(func, *job.args, **job.kwargs)
        return await to_thread.run_sync(wrapped, limiter=self._limiter)
```

## Distributed Scheduling

### Running a Separate Scheduler Process

```bash
python sync_scheduler.py
```

### Running a Separate Worker Process

```bash
python sync_worker.py
