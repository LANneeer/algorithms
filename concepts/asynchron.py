class EventLoop():
    def __init__(self, tasks_list):
        self.tasks_list = tasks_list
        self.pending_tasks = []

    def start_event_loop(self):
        while True:
            if not tasks_list and not self.pending_tasks:  
            # if both pending and tasks lists are empty -> stop event loop
                break
            
            if tasks_list:
            # take next tasks
            # remove from task_list
            # run until 'await'
            # deligate I/O task to the OS with self.run_await
            # add to pending_list
            # when the result is ready, 
            #      make_select_system_call will show it
                current_task = self.tasks_list.pop()
                run_until_await(current_task)
                self.run_await(current_task) 
                self.pending_tasks.append(current_task)
            
            # get completed I/O tasks
            # iterate trough them and run the code that comes after 'await'
            finished_tasks = make_select_system_call()
            for finished_task in finished_tasks:
                run_after_await(finished_task)
                self.pending_tasks.remove(task)     

    def run_await(self, task):
        return make_system_call_to_run_io_task(task)


async def fetch_and_process_a_long_text():
    res = []
    url = 'https://example.com/some_long_text'
    await content = fetch_text(url)
    res = content.split()
    return res


if __name__ == '__main__':
    tasks = [fetch_and_process_a_long_text]
    event_loop = EventLoop(tasks)
    event_loop.start_event_loop()
