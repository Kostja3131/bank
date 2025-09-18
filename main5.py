class Task:
    idtask = 0 

    def __init__(self, name, description, status):
        self.name = name
        self.description = description
        self.status = status
        self.id = Task.idtask  
        Task.idtask += 1  

    def complitedTask(self):
    	self.status = True

task1 = Task("cleaning", "clean bathroom", False)


def main():
	"""точка входа в функцию"""
	iterationIndex = 0
	tasks = {}

	print("hello choose action")
	
	index = 0
	def create_task(name, description, status=False):
		nonlocal index
		taskiter = index
		task = Task(name, description, status)
		tasks[f"task{taskiter}"] = [task.name, task.description, task.status]
		index +=1

	def edit_task(task, element, edit):
		tasks[task][element] = edit

	def remove_task(task):
		del tasks[task]

	def task_complited(task, element=2, status=True):
		tasks[task][element] = status


	create_task("name", "description")
	create_task("name1", "d1escription")
	edit_task("task0", 1, "narkotiki")
	task_complited("task0", element=2, status=True)
	for k,v in tasks.items():
		print(k,v)

	remove_task("task0")
	
	# iterationIndex+= 1
	# if action == 1:
	# 	pass
	# else if action == 2:
	# 	pass
	# else if action == 3:
	# 	pass




if __name__ == "__main__":
	main() 