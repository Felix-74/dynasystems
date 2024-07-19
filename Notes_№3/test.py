import aiohttp
import asyncio
import time

async def test_performance(add_ratio, total_operations):
    base_url = "http://localhost:8000/api/"
    headers = {'Content-Type': 'application/json'}
    note_data = {"note": "Performance Test Note", "description": "This is a test note for performance testing."}

    add_operations = int(total_operations * add_ratio)
    delete_operations = total_operations - add_operations

    add_times = []
    delete_times = []

    async with aiohttp.ClientSession() as session:
        # Add notes
        for _ in range(add_operations):
            start_time = time.time()
            async with session.post(base_url + 'notes/', json=note_data, headers=headers) as response:
                end_time = time.time()
                add_times.append(end_time - start_time)

                if response.status != 201:
                    print(f"Failed to add note: {await response.json()}")

        # Delete notes
        for note_id in range(1, delete_operations + 1):
            start_time = time.time()
            async with session.delete(base_url + f'tasks/{note_id}/', headers=headers) as response:
                end_time = time.time()
                delete_times.append(end_time - start_time)

                if response.status != 204:
                    print(f"Failed to delete note with ID {note_id}")

    print(f"Average add time: {sum(add_times) / len(add_times):.6f} seconds")
    print(f"Average delete time: {sum(delete_times) /  len(delete_times):.6f} seconds")

if __name__ == "__main__":
    add_ratio = float(input("Enter the ratio of add operations (0-1): "))
    total_operations = int(input("Enter the total number of operations: "))
    asyncio.run(test_performance(add_ratio, total_operations))
