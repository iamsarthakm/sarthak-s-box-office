import threading

import requests

url = "http://localhost:8000/api/hold/"
payload = {"event_id": 3, "qty": 90}  # 
headers = {"Content-Type": "application/json"}

# Barrier makes threads wait until all are ready
start_barrier = threading.Barrier(2)  


def make_request(thread_id):
    start_barrier.wait() 
    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"Thread {thread_id}: Status {response.status_code}")
        print(f"Thread {thread_id}: Response {response.text}")
        print("-" * 50)
    except Exception as e:
        print(f"Thread {thread_id}: Error {e}")


def test_concurrent_holds():
    print("Testing concurrent hold requests...")
    print(f"URL: {url}")
    print(f"Payload: {payload}")
    print("Number of concurrent requests: 2")
    print("=" * 60)

    # Create threads
    threads = [threading.Thread(target=make_request, args=(i,)) for i in range(2)]

    # Start all threads
    for t in threads:
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("All concurrent requests completed!")
    print("Check your server logs to see how row-level locking handled these requests.")


if __name__ == "__main__":
    test_concurrent_holds()
