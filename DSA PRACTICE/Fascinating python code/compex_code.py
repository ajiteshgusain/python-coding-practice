import asyncio
from dataclasses import dataclass, field
import functools
import logging
from queue import PriorityQueue
import time
from typing import Any, Callable, Dict, Type

# Setup concise, structured logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("AdvancedPipeline")

class ValidatedType:
    """Custom Descriptor enforcing runtime type checking dynamically."""
    def __init__(self, expected_type: Type):
        self.expected_type = expected_type
        self.storage_name = f"_{expected_type.__name__}_field"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type.__name__}, got {type(value).__name__}")
        setattr(instance, self.storage_name, value)


@dataclass(order=True)
class AsyncTask:
    """Data structure representing a pipeline task with auto-sorting via priority."""
    priority: int = field(init=True)
    name: str = field(init=True, compare=False)
    payload: Dict[str, Any] = field(init=True, compare=False)
    retries: int = field(default=3, compare=False)


def retry_async_operation(retries_limit: int = 3, backoff_factor: float = 0.5):
    """Advanced decorator implementing exponential backoff for async functions."""
    def decorator(func: Callable):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries_limit:
                try:
                    return await func(*args, **kwargs)
                except Exception as exc:
                    attempt += 1
                    if attempt >= retries_limit:
                        logger.error(f"Execution failed after {attempt} attempts in '{func.__name__}'.")
                        raise exc
                    sleep_time = backoff_factor * (2 ** attempt)
                    logger.warning(f"Error in '{func.__name__}': {exc}. Retrying in {sleep_time}s...")
                    await asyncio.sleep(sleep_time)
        return wrapper
    return decorator


class ExecutionEngine:
    """Core processing engine deploying structural pattern matching (Python 3.10+)."""
    
    # Enforcing strict string rules on metadata processing via our custom descriptor
    metadata_status = ValidatedType(str)

    def __init__(self):
        self.metadata_status = "INITIALIZED"

    @retry_async_operation(retries_limit=3, backoff_factor=0.2)
    async def process(self, task: AsyncTask) -> str:
        """Processes a single task using advanced conditional structure matching."""
        logger.info(f"Executing Engine on Task: {task.name} (Priority Level: {task.priority})")
        
        # Simulate network or processing latency
        await asyncio.sleep(0.1)

        # Structural Pattern Matching over payloads
        match task.payload:
            case {"action": "compute", "data": list() as numbers}:
                result = sum(numbers)
                return f"Computed sum: {result}"
            
            case {"action": "transform", "text": str() as string_val}:
                return f"Transformed text: {string_val.upper()}"
            
            case {"action": "alert", "level": "critical"}:
                raise RuntimeError("Critical system alert triggered a simulated failure!")
                
            case _:
                return "Unknown routine fallback executed successfully."


class AsyncPipelineManager:
    """Manages concurrent workflow loops using a Priority Queue engine."""
    def __init__(self, workers_count: int = 2):
        self.task_queue = asyncio.PriorityQueue()
        self.workers_count = workers_count
        self.engine = ExecutionEngine()

    async def submit_task(self, task: AsyncTask):
        """Asynchronously enqueues a new item sorted by priority weight."""
        await self.task_queue.put(task)
        logger.info(f"Queued task: '{task.name}'")

    async def _worker_loop(self, worker_id: int):
        """An individual concurrent worker consuming items from the shared queue."""
        logger.info(f"Worker-{worker_id} safely spawned.")
        while True:
            task: AsyncTask = await self.task_queue.get()
            try:
                result = await self.engine.process(task)
                logger.info(f"Worker-{worker_id} finalized '{task.name}' -> Result: {result}")
            except Exception as final_err:
                logger.critical(f"Worker-{worker_id} crashed handling '{task.name}': {final_err}")
            finally:
                self.task_queue.task_done()

    async def execute_pipeline(self):
        """Assembles workers pool, executes processing queue, and cleans up resources."""
        workers = [
            asyncio.create_task(self._worker_loop(i)) 
            for i in range(self.workers_count)
        ]
        
        # Block until the queue is completely emptied
        await self.task_queue.join()
        
        # Cleanly cancel worker loops once processing completes
        for worker in workers:
            worker.cancel()
        await asyncio.gather(*workers, return_exceptions=True)
        logger.info("Pipeline manager shutdown cleanly.")


# Main Async Event Orchestrator
async def main():
    manager = AsyncPipelineManager(workers_count=3)

    # Seed the engine with tasks across different priorities
    # Low numerical value = High priority in standard Priority Queues
    await manager.submit_task(AsyncTask(priority=3, name="Task_Alpha", payload={"action": "transform", "text": "hello complex python"}))
    await manager.submit_task(AsyncTask(priority=1, name="Task_Beta", payload={"action": "compute", "data": [10, 20, 30, 40]}))
    await manager.submit_task(AsyncTask(priority=0, name="Task_Gamma", payload={"action": "alert", "level": "critical"})) # Will trigger retry decorator
    await manager.submit_task(AsyncTask(priority=2, name="Task_Delta", payload={"action": "unknown_type"}))

    logger.info("Starting pipeline engine execution loop...")
    start_time = time.perf_counter()
    
    await manager.execute_pipeline()
    
    logger.info(Total processing duration: {time.perf_counter() - start_time:.4f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
